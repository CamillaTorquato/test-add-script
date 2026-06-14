import fitz
import re
from pathlib import Path

PASTA = r"C:\Users\camil\OneDrive\Área de Trabalho\RENOMEAÇÃO\ilovepdf_split"

for arquivo in Path(PASTA).glob("*.pdf"):

    texto = ""

    pdf = fitz.open(arquivo)

    for pagina in pdf:
        texto += pagina.get_text()

    pdf.close()

    # BENEFICIÁRIO
    beneficiario = "SEM_BENEFICIARIO"

    m = re.search(
        r"Beneficiário:\s*(.*?)\s*CPF/CNPJ do beneficiário",
        texto,
        re.DOTALL
    )

    if m:
        beneficiario = " ".join(m.group(1).split())

    # DATA DE PAGAMENTO
    data_pagamento = "SEM_DATA"

    m = re.search(
        r"Data de pagamento:\s*(\d{2}/\d{2}/\d{4})",
        texto
    )

    if m:
        data_pagamento = m.group(1)

        dia, mes, ano = data_pagamento.split("/")
        data_pagamento = f"{ano}-{mes}-{dia}"

    # VALOR DO PAGAMENTO
    valor = "SEM_VALOR"

    m = re.search(
        r"Valor do pagamento.?(\d{1,3}(?:\.\d{3}),\d{2})",
        texto,
        re.DOTALL
    )

    if m:
        valor = m.group(1)
    # Limpa caracteres inválidos
    print("BENEFICIARIO:", beneficiario)
    print("DATA:", data_pagamento)
    print("VALOR:", valor)
    print("-" * 50)
    beneficiario = re.sub(r'[\\/*?:"<>|]', "", beneficiario)

    novo_nome = f"{data_pagamento} - {beneficiario} - {valor}.pdf"

    novo_caminho = arquivo.with_name(novo_nome)

    contador = 1

    while novo_caminho.exists():
        novo_nome = (
            f"{data_pagamento} - "
            f"{beneficiario} - "
            f"{valor} ({contador}).pdf"
        )

        novo_caminho = arquivo.with_name(novo_nome)
        contador += 1

    arquivo.rename(novo_caminho)

    print(f"Renomeado: {novo_nome}")