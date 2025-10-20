import sys
import sys
from pathlib import Path
import csv

try:
    import xlsxwriter
except ImportError:
    print("Erro: xlsxwriter não encontrado. Instale com pip install xlsxwriter.")
    sys.exit(1)

# Config
ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "docs" / "MATRIZ_TRIANGULACAO.csv"
XLSX_PATH = ROOT / "docs" / "TRIANGULACAO_ANALITICA.xlsx"

LISTAS_SUGERIDAS = {
    "tema": [
        "Saúde e bem-estar",
        "Participação social",
        "Acessibilidade digital",
        "Políticas públicas",
        "Qualidade de vida",
        "Segurança e privacidade",
    ],
    "codigo": [
        "servicos_digitais",
        "videochamada",
        "usabilidade",
        "politicas",
        "autonomia",
        "seguranca",
    ],
    "fonte": ["IBGE", "ONU", "ITU", "Outras"],
    "filtro_faixa_etaria": ["60+", "60-64", "65-69", "70-74", "75-79", "80+"],
    "filtro_renda": ["Q1", "Q2", "Q3", "Q4", "Q5", "Todos"],
    "filtro_escolaridade": ["Fundamental", "Médio+", "Superior", "Todos"],
    "filtro_raca_cor": ["Brancos", "Negros/Pardos", "Indígenas", "Amarelos", "Todos"],
}

DEFAULT_COLS = [
    "tema",
    "trecho_qualitativo",
    "codigo",
    "indicador_quantitativo",
    "valor",
    "filtro_faixa_etaria",
    "filtro_renda",
    "filtro_escolaridade",
    "filtro_raca_cor",
    "fonte",
    "observacoes",
]


def read_csv_rows() -> tuple[list[str], list[dict]]:
    if not CSV_PATH.exists():
        return DEFAULT_COLS, []
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or DEFAULT_COLS
        rows = [r for r in reader]
    return cols, rows


def autofit_columns(worksheet, headers: list[str], rows: list[dict]):
    widths = [len(h) for h in headers]
    for r in rows:
        for i, h in enumerate(headers):
            val_str = str(r.get(h, ""))
            if len(val_str) > widths[i]:
                widths[i] = len(val_str)
    for i, w in enumerate(widths):
        worksheet.set_column(i, i, min(w + 2, 60))


def write_listas(workbook) -> dict:
    sheet = workbook.add_worksheet("Listas")
    named_ranges = {}
    start_col = 0
    for key, values in LISTAS_SUGERIDAS.items():
        sheet.write(0, start_col, key)
        for idx, val in enumerate(values, start=1):
            sheet.write(idx, start_col, val)
        last_row = len(values) + 1
        col_letter = chr(65 + start_col)
        named = f"list_{key}"
        workbook.define_name(named, f"=Listas!${col_letter}$2:${col_letter}${last_row}")
        named_ranges[key] = named
        start_col += 1
    return named_ranges


def main():
    headers, rows = read_csv_rows()
    XLSX_PATH.parent.mkdir(parents=True, exist_ok=True)

    workbook = xlsxwriter.Workbook(str(XLSX_PATH))
    header_fmt = workbook.add_format({"bold": True, "bg_color": "#E9EFF7"})

    # Triangulacao
    ws = workbook.add_worksheet("Triangulacao")
    for c, h in enumerate(headers):
        ws.write(0, c, h, header_fmt)
    for r_idx, row in enumerate(rows, start=1):
        for c, h in enumerate(headers):
            ws.write(r_idx, c, row.get(h, ""))
    autofit_columns(ws, headers, rows)

    # Listas e validações
    named_ranges = write_listas(workbook)
    map_headers = {
        "tema": "tema",
        "codigo": "codigo",
        "fonte": "fonte",
        "filtro_faixa_etaria": "filtro_faixa_etaria",
        "filtro_renda": "filtro_renda",
        "filtro_escolaridade": "filtro_escolaridade",
        "filtro_raca_cor": "filtro_raca_cor",
    }
    max_rows = max(len(rows) + 200, 200)
    for col_idx, h in enumerate(headers):
        key = map_headers.get(h)
        if key and key in named_ranges:
            ws.data_validation(1, col_idx, max_rows, col_idx, {
                'validate': 'list',
                'source': f'={named_ranges[key]}'
            })

    # Dicionario
    ws_dic = workbook.add_worksheet("Dicionario")
    dic_headers = ["indicador_quantitativo", "definicao", "fonte", "periodo", "observacoes"]
    for c, h in enumerate(dic_headers):
        ws_dic.write(0, c, h, header_fmt)
    autofit_columns(ws_dic, dic_headers, [])

    # Fontes
    ws_f = workbook.add_worksheet("Fontes")
    fontes_headers = ["fonte", "escopo", "granularidade", "observacoes"]
    for c, h in enumerate(fontes_headers):
        ws_f.write(0, c, h, header_fmt)
    fontes_rows = [
        {"fonte": "IBGE", "escopo": "Brasil/regiões", "granularidade": "pessoas/domicílios", "observacoes": "PNAD/PNADC/Tabelas"},
        {"fonte": "ONU", "escopo": "Brasil/Internacional (1990-2010)", "granularidade": "país/região/ano", "observacoes": "Demografia/socioeconômicos"},
        {"fonte": "ITU", "escopo": "Internacional (2000-2024)", "granularidade": "país/ano", "observacoes": "Indicadores ICT"},
    ]
    for r_idx, row in enumerate(fontes_rows, start=1):
        for c, h in enumerate(fontes_headers):
            ws_f.write(r_idx, c, row[h])
    autofit_columns(ws_f, fontes_headers, fontes_rows)

    # Resumo
    ws_r = workbook.add_worksheet("Resumo")
    ws_r.write(0, 0, "tema", header_fmt)
    ws_r.write(0, 1, "ocorrencias", header_fmt)
    counts = {}
    for r in rows:
        tema = (r.get("tema") or "").strip()
        if tema:
            counts[tema] = counts.get(tema, 0) + 1
    for idx, (tema, cnt) in enumerate(sorted(counts.items(), key=lambda x: x[0]), start=1):
        ws_r.write(idx, 0, tema)
        ws_r.write(idx, 1, cnt)
    autofit_columns(ws_r, ["tema", "ocorrencias"], [{"tema": k, "ocorrencias": v} for k, v in counts.items()])

    workbook.close()
    print(f"Planilha criada em: {XLSX_PATH}")


if __name__ == "__main__":
    sys.exit(main())
