#!/usr/bin/env python3
"""
Detector de cambios en la normativa ferroviaria europea.

Compara el estado anterior (JSON) con los datos frescos obtenidos por el scraper
y genera un informe en markdown con:
- Documentos nuevos
- Documentos derogados
- Documentos sustituidos / reemplazados
- Cambios de estado
- Modificaciones en documentos existentes
- Cambios en recursos adicionales de TSIs
- Resumen estadístico
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_JSON = SCRIPT_DIR / "era_regulacion_estados_miembros.json"
REPORTS_DIR = SCRIPT_DIR / "informes"

# Campos relevantes para detectar cambios significativos en documentos regulatorios
TRACKED_FIELDS = [
    "titulo", "titulo_en", "tipo", "estado", "descripcion",
    "numero_oficial", "referencia_celex", "fecha_publicacion",
    "deroga", "ambito", "subsistema", "categoria", "enmiendas",
    "notas", "plazos_implementacion",
]

# Palabras clave que indican derogación
DEROGATION_KEYWORDS = ["derogad", "repealed", "abrogat"]
# Palabras clave que indican sustitución
REPLACEMENT_KEYWORDS = ["reemplazad", "sustitu", "replaced", "superseded"]


def load_json(path: Path) -> dict:
    """Carga un fichero JSON."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(data: dict, path: Path) -> None:
    """Guarda datos a un fichero JSON."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def index_documents(docs: list[dict]) -> dict[str, dict]:
    """Indexa documentos por su campo 'id'."""
    return {d["id"]: d for d in docs if "id" in d}


def classify_status_change(old_status: str, new_status: str) -> str | None:
    """Clasifica el tipo de cambio de estado."""
    new_lower = new_status.lower()
    old_lower = old_status.lower()

    if any(kw in new_lower for kw in DEROGATION_KEYWORDS):
        if not any(kw in old_lower for kw in DEROGATION_KEYWORDS):
            return "derogado"

    if any(kw in new_lower for kw in REPLACEMENT_KEYWORDS):
        if not any(kw in old_lower for kw in REPLACEMENT_KEYWORDS):
            return "sustituido"

    if old_lower != new_lower:
        return "cambio_estado"

    return None


def diff_document(old_doc: dict, new_doc: dict) -> list[dict]:
    """Compara dos versiones de un documento y devuelve los cambios."""
    changes = []
    for field in TRACKED_FIELDS:
        old_val = old_doc.get(field)
        new_val = new_doc.get(field)
        if old_val != new_val:
            changes.append({
                "campo": field,
                "anterior": old_val,
                "nuevo": new_val,
            })
    return changes


def diff_resources(old_resources: list[dict], new_resources: list[dict]) -> dict:
    """Compara recursos adicionales de TSI."""
    def resource_key(r: dict) -> str:
        return r.get("url", r.get("titulo_en", ""))

    old_keys = {resource_key(r) for r in old_resources}
    new_keys = {resource_key(r) for r in new_resources}

    added = [r for r in new_resources if resource_key(r) not in old_keys]
    removed = [r for r in old_resources if resource_key(r) not in new_keys]

    return {"added": added, "removed": removed}


def detect_changes(old_data: dict, new_data: dict) -> dict:
    """Detecta todos los cambios entre el estado anterior y el nuevo."""
    old_docs = index_documents(old_data.get("documentos_regulatorios", []))
    new_docs = index_documents(new_data.get("documentos_regulatorios", []))

    old_ids = set(old_docs.keys())
    new_ids = set(new_docs.keys())

    result = {
        "fecha_analisis": datetime.now(timezone.utc).isoformat(),
        "fecha_estado_anterior": old_data.get("metadata", {}).get("fecha_generacion", "desconocida"),
        "fecha_estado_nuevo": new_data.get("metadata", {}).get("fecha_generacion", "desconocida"),
        "nuevos": [],
        "eliminados": [],
        "derogados": [],
        "sustituidos": [],
        "cambios_estado": [],
        "modificados": [],
        "recursos_tsi": {"añadidos": [], "eliminados": []},
        "resumen": {},
    }

    # 1. Documentos nuevos
    for doc_id in sorted(new_ids - old_ids):
        result["nuevos"].append(new_docs[doc_id])

    # 2. Documentos que ya no aparecen
    for doc_id in sorted(old_ids - new_ids):
        result["eliminados"].append(old_docs[doc_id])

    # 3. Documentos existentes: detectar cambios
    for doc_id in sorted(old_ids & new_ids):
        changes = diff_document(old_docs[doc_id], new_docs[doc_id])
        if not changes:
            continue

        # Clasificar cambio de estado
        status_changes = [c for c in changes if c["campo"] == "estado"]
        if status_changes:
            sc = status_changes[0]
            classification = classify_status_change(
                str(sc["anterior"] or ""), str(sc["nuevo"] or "")
            )
            entry = {
                "id": doc_id,
                "titulo": new_docs[doc_id].get("titulo", ""),
                "estado_anterior": sc["anterior"],
                "estado_nuevo": sc["nuevo"],
                "todos_los_cambios": changes,
            }
            if classification == "derogado":
                result["derogados"].append(entry)
            elif classification == "sustituido":
                result["sustituidos"].append(entry)
            else:
                result["cambios_estado"].append(entry)
        else:
            result["modificados"].append({
                "id": doc_id,
                "titulo": new_docs[doc_id].get("titulo", ""),
                "cambios": changes,
            })

    # 4. Recursos adicionales de TSI
    old_resources = old_data.get("recursos_adicionales_tsi", [])
    new_resources = new_data.get("recursos_adicionales_tsi", [])
    res_diff = diff_resources(old_resources, new_resources)
    result["recursos_tsi"]["añadidos"] = res_diff["added"]
    result["recursos_tsi"]["eliminados"] = res_diff["removed"]

    # 5. Resumen
    result["resumen"] = {
        "total_docs_anterior": len(old_docs),
        "total_docs_nuevo": len(new_docs),
        "nuevos": len(result["nuevos"]),
        "eliminados": len(result["eliminados"]),
        "derogados": len(result["derogados"]),
        "sustituidos": len(result["sustituidos"]),
        "cambios_estado": len(result["cambios_estado"]),
        "modificados": len(result["modificados"]),
        "recursos_tsi_añadidos": len(result["recursos_tsi"]["añadidos"]),
        "recursos_tsi_eliminados": len(result["recursos_tsi"]["eliminados"]),
    }

    return result


def has_meaningful_changes(changes: dict) -> bool:
    """Determina si hay cambios significativos que reportar."""
    s = changes["resumen"]
    return any([
        s["nuevos"], s["eliminados"], s["derogados"], s["sustituidos"],
        s["cambios_estado"], s["modificados"],
        s["recursos_tsi_añadidos"], s["recursos_tsi_eliminados"],
    ])


# ---------------------------------------------------------------------------
# Generación del informe markdown
# ---------------------------------------------------------------------------

def _doc_link(doc: dict) -> str:
    """Genera enlace markdown para un documento."""
    url = doc.get("url_eur_lex") or doc.get("url_era") or doc.get("url", "")
    title = doc.get("titulo") or doc.get("titulo_en", "Sin título")
    if url:
        return f"[{title}]({url})"
    return title


def _section_nuevos(docs: list[dict]) -> str:
    if not docs:
        return ""
    lines = ["## 📄 Documentos Nuevos", ""]
    for doc in docs:
        lines.append(f"### {_doc_link(doc)}")
        lines.append(f"- **Tipo**: {doc.get('tipo', 'N/A')}")
        lines.append(f"- **Referencia**: {doc.get('numero_oficial', 'N/A')}")
        lines.append(f"- **Fecha publicación**: {doc.get('fecha_publicacion', 'N/A')}")
        lines.append(f"- **Estado**: {doc.get('estado', 'N/A')}")
        lines.append(f"- **Subsistema**: {doc.get('subsistema', 'N/A')}")
        lines.append(f"- **Categoría**: {doc.get('categoria', 'N/A')}")
        desc = doc.get("descripcion", "")
        if desc:
            lines.append(f"- **Descripción**: {desc}")
        lines.append("")
    return "\n".join(lines)


def _section_derogados(docs: list[dict]) -> str:
    if not docs:
        return ""
    lines = ["## ⛔ Documentos Derogados", ""]
    for doc in docs:
        lines.append(f"- **{doc['titulo']}** (`{doc['id']}`)")
        lines.append(f"  - Estado anterior: {doc['estado_anterior']}")
        lines.append(f"  - Estado nuevo: {doc['estado_nuevo']}")
        lines.append("")
    return "\n".join(lines)


def _section_sustituidos(docs: list[dict]) -> str:
    if not docs:
        return ""
    lines = ["## 🔄 Documentos Sustituidos / Reemplazados", ""]
    for doc in docs:
        lines.append(f"- **{doc['titulo']}** (`{doc['id']}`)")
        lines.append(f"  - Estado anterior: {doc['estado_anterior']}")
        lines.append(f"  - Estado nuevo: {doc['estado_nuevo']}")
        lines.append("")
    return "\n".join(lines)


def _section_cambios_estado(docs: list[dict]) -> str:
    if not docs:
        return ""
    lines = ["## 🔀 Cambios de Estado", ""]
    for doc in docs:
        lines.append(f"- **{doc['titulo']}** (`{doc['id']}`)")
        lines.append(f"  - {doc['estado_anterior']} → {doc['estado_nuevo']}")
        lines.append("")
    return "\n".join(lines)


def _section_modificados(docs: list[dict]) -> str:
    if not docs:
        return ""
    lines = ["## ✏️ Documentos Modificados", ""]
    for doc in docs:
        lines.append(f"### {doc['titulo']} (`{doc['id']}`)")
        for change in doc["cambios"]:
            field = change["campo"]
            lines.append(f"- **{field}**:")
            lines.append(f"  - Antes: {change['anterior']}")
            lines.append(f"  - Ahora: {change['nuevo']}")
        lines.append("")
    return "\n".join(lines)


def _section_eliminados(docs: list[dict]) -> str:
    if not docs:
        return ""
    lines = ["## ❌ Documentos Eliminados del Catálogo", ""]
    for doc in docs:
        lines.append(f"- **{doc.get('titulo', doc.get('titulo_en', 'N/A'))}** (`{doc['id']}`)")
        lines.append(f"  - Tipo: {doc.get('tipo', 'N/A')}")
        lines.append(f"  - Último estado conocido: {doc.get('estado', 'N/A')}")
        lines.append("")
    return "\n".join(lines)


def _section_recursos_tsi(recursos: dict) -> str:
    added = recursos.get("añadidos", [])
    removed = recursos.get("eliminados", [])
    if not added and not removed:
        return ""
    lines = ["## 📚 Cambios en Recursos Adicionales de TSIs", ""]
    if added:
        lines.append(f"### Nuevos recursos ({len(added)})")
        for r in added:
            title = r.get("titulo_en", "Sin título")
            url = r.get("url", "")
            source = r.get("fuente_scraping", "")
            if url:
                lines.append(f"- [{title}]({url})")
            else:
                lines.append(f"- {title}")
            if source:
                lines.append(f"  - Fuente: {source}")
        lines.append("")
    if removed:
        lines.append(f"### Recursos eliminados ({len(removed)})")
        for r in removed:
            lines.append(f"- {r.get('titulo_en', 'Sin título')}")
        lines.append("")
    return "\n".join(lines)


def generate_report(changes: dict) -> str:
    """Genera el informe completo en markdown."""
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    s = changes["resumen"]

    lines = [
        f"# Informe de Cambios en Normativa Ferroviaria UE — {date_str}",
        "",
        "## Resumen",
        "",
        f"- **Período**: {changes['fecha_estado_anterior']} → {changes['fecha_estado_nuevo']}",
        f"- **Total documentos (anterior)**: {s['total_docs_anterior']}",
        f"- **Total documentos (actual)**: {s['total_docs_nuevo']}",
        "",
    ]

    if not has_meaningful_changes(changes):
        lines.append("### Sin cambios significativos")
        lines.append("")
        lines.append("No se han detectado cambios en la normativa desde la última revisión.")
        return "\n".join(lines)

    # Tabla resumen de cambios
    lines.extend([
        "### Desglose de cambios",
        "",
        f"- Documentos nuevos: **{s['nuevos']}**",
        f"- Documentos derogados: **{s['derogados']}**",
        f"- Documentos sustituidos: **{s['sustituidos']}**",
        f"- Otros cambios de estado: **{s['cambios_estado']}**",
        f"- Documentos modificados: **{s['modificados']}**",
        f"- Documentos eliminados del catálogo: **{s['eliminados']}**",
        f"- Recursos TSI añadidos: **{s['recursos_tsi_añadidos']}**",
        f"- Recursos TSI eliminados: **{s['recursos_tsi_eliminados']}**",
        "",
    ])

    # Secciones detalladas (solo si hay contenido)
    sections = [
        _section_nuevos(changes["nuevos"]),
        _section_derogados(changes["derogados"]),
        _section_sustituidos(changes["sustituidos"]),
        _section_cambios_estado(changes["cambios_estado"]),
        _section_modificados(changes["modificados"]),
        _section_eliminados(changes["eliminados"]),
        _section_recursos_tsi(changes["recursos_tsi"]),
    ]

    for section in sections:
        if section:
            lines.append(section)

    lines.extend([
        "---",
        f"*Informe generado automáticamente el {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}*",
        f"*Fuente: [ERA](https://www.era.europa.eu) / [EUR-Lex](https://eur-lex.europa.eu)*",
    ])

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detecta cambios en la normativa ferroviaria europea y genera un informe."
    )
    parser.add_argument(
        "--previous", "-p",
        type=Path,
        default=DEFAULT_JSON,
        help="Ruta al JSON con el estado anterior (por defecto: era_regulacion_estados_miembros.json)",
    )
    parser.add_argument(
        "--current", "-c",
        type=Path,
        default=None,
        help="Ruta al JSON con el estado actual. Si no se indica, se ejecuta el scraper.",
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=REPORTS_DIR,
        help="Directorio donde se guardan los informes (por defecto: informes/)",
    )
    parser.add_argument(
        "--update-baseline",
        action="store_true",
        help="Actualizar el JSON base con los datos nuevos tras generar el informe.",
    )
    args = parser.parse_args()

    # --- 1. Cargar estado anterior ---
    if not args.previous.exists():
        logger.error(f"No se encuentra el fichero de estado anterior: {args.previous}")
        sys.exit(1)

    logger.info(f"Cargando estado anterior: {args.previous}")
    old_data = load_json(args.previous)

    # --- 2. Obtener estado actual ---
    if args.current:
        logger.info(f"Cargando estado actual: {args.current}")
        new_data = load_json(args.current)
    else:
        logger.info("Ejecutando scraper para obtener datos frescos...")
        # Importar y ejecutar el scraper inline
        sys.path.insert(0, str(SCRIPT_DIR))
        import scrape_era_regulations as scraper

        import requests
        session = requests.Session()
        session.headers.update(scraper.HEADERS)

        all_documents: list[dict] = []
        all_resources: list[dict] = []

        all_documents.extend(scraper.get_fourth_railway_package_legislation())
        all_documents.extend(scraper.get_tsi_documents())
        all_documents.extend(scraper.get_implementing_regulations())
        all_documents.extend(scraper.get_csm_documents())
        all_documents.extend(scraper.get_base_directives())
        all_documents.extend(scraper.scrape_era_documents(session))

        for tsi_url in scraper.TSI_PAGES:
            resources = scraper.scrape_tsi_page(tsi_url, session)
            if resources:
                all_resources.extend(resources)

        new_data = {
            "metadata": {
                "titulo": "Documentación regulatoria de ERA para estados miembros de la UE",
                "descripcion": (
                    "Recopilación exhaustiva de la documentación normativa de la Agencia "
                    "Ferroviaria de la Unión Europea (ERA) que los estados miembros deben "
                    "tener en cuenta."
                ),
                "fuente_principal": "https://www.era.europa.eu",
                "fecha_generacion": datetime.now(timezone.utc).isoformat(),
                "total_documentos_regulatorios": len(all_documents),
                "total_recursos_adicionales": len(all_resources),
                "categorias": sorted(
                    set(d.get("categoria", "Sin categoría") for d in all_documents)
                ),
            },
            "documentos_regulatorios": all_documents,
            "recursos_adicionales_tsi": all_resources,
        }

    # --- 3. Detectar cambios ---
    logger.info("Comparando estados...")
    changes = detect_changes(old_data, new_data)

    # --- 4. Generar informe ---
    args.output_dir.mkdir(parents=True, exist_ok=True)
    date_stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = args.output_dir / f"informe_cambios_{date_stamp}.md"
    changes_json_path = args.output_dir / f"cambios_{date_stamp}.json"

    report_md = generate_report(changes)
    report_path.write_text(report_md, encoding="utf-8")
    logger.info(f"Informe markdown generado: {report_path}")

    save_json(changes, changes_json_path)
    logger.info(f"Datos de cambios guardados: {changes_json_path}")

    # --- 5. Actualizar baseline si se pide ---
    if args.update_baseline:
        save_json(new_data, args.previous)
        logger.info(f"Baseline actualizado: {args.previous}")

    # --- 6. Imprimir resumen ---
    s = changes["resumen"]
    if has_meaningful_changes(changes):
        print(f"\n{'='*60}")
        print(f"CAMBIOS DETECTADOS — {date_stamp}")
        print(f"{'='*60}")
        print(f"  Nuevos:                {s['nuevos']}")
        print(f"  Derogados:             {s['derogados']}")
        print(f"  Sustituidos:           {s['sustituidos']}")
        print(f"  Cambios de estado:     {s['cambios_estado']}")
        print(f"  Modificados:           {s['modificados']}")
        print(f"  Eliminados:            {s['eliminados']}")
        print(f"  Recursos TSI añadidos: {s['recursos_tsi_añadidos']}")
        print(f"  Recursos TSI retirados:{s['recursos_tsi_eliminados']}")
        print(f"{'='*60}")
        print(f"Informe completo: {report_path}")
    else:
        print(f"\nSin cambios significativos desde la última revisión ({date_stamp}).")
        print(f"Informe: {report_path}")


if __name__ == "__main__":
    main()
