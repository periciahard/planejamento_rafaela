from docx import Document
from datetime import datetime, timedelta
import os

DAYS = ["SEGUNDA","TERCA","QUARTA","QUINTA","SEXTA"]

def safe(v):
    if isinstance(v, list):
        return "\n".join(v)
    return str(v or "")

def gerar(data, template="templates/template.docx"):

    doc = Document(template)

    inicio = data.get("semana_inicio")
    fim = data.get("semana_fim")

    if inicio and fim:
        try:
            d1 = datetime.strptime(inicio, "%Y-%m-%d")
            d2 = datetime.strptime(fim, "%Y-%m-%d")

            dias = []
            while d1 <= d2:
                dias.append(d1.strftime("%d/%m/%Y"))
                d1 += timedelta(days=1)
        except:
            dias = DAYS
    else:
        dias = DAYS

    plano = f"""DISCIPLINA: {data.get('disciplina','')}

CONTEUDO:
{safe(data.get('conteudo'))}

OBJETIVOS:
{safe(data.get('objetivos'))}

HABILIDADES:
{safe(data.get('habilidades'))}

METODOLOGIA:
{safe(data.get('metodologia'))}

RECURSOS:
{safe(data.get('recursos'))}
"""

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for d in DAYS:
                    if f"{{{{{d}}}}}" in cell.text:
                        cell.text = cell.text.replace(f"{{{{{d}}}}}", plano)

    out = "output/PLANO_V4.docx"
    doc.save(out)
    return out
