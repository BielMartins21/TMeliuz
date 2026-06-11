import pandas as pd
import os

# =========================
# FUNÇÃO DE LIMPEZA
# =========================

def limpar_moeda(valor):
    if pd.isna(valor):
        return 0

    valor = str(valor)

    valor = (
        valor.replace("R$", "")
             .replace(".", "")
             .replace(",", ".")
             .strip()
    )

    return float(valor)

# =========================
# FUNÇÃO PRINCIPAL
# =========================

def analisar_teste(caminho_csv):

    df = pd.read_csv(caminho_csv)

    # Padronização dos nomes
    df.columns = [c.strip().lower() for c in df.columns]

    # Conversão monetária
    df["comissão"] = df["comissão"].apply(limpar_moeda)
    df["cashback"] = df["cashback"].apply(limpar_moeda)
    df["vendas totais"] = df["vendas totais"].apply(limpar_moeda)

    # Lucro
    df["lucro"] = df["comissão"] - df["cashback"]

    # Agrupamento por grupo
    resumo = df.groupby("grupos de usuários").agg({
        "compradores": "sum",
        "comissão": "sum",
        "cashback": "sum",
        "vendas totais": "sum",
        "lucro": "sum"
    })

    resumo = resumo.sort_values("lucro", ascending=False)

    vencedor = resumo.index[0]

    parceiro = df["parceiro"].iloc[0]

    print("\n==============================")
    print(f"PARCEIRO {parceiro}")
    print("==============================\n")

    print(resumo)

    print("\nGRUPO VENCEDOR:")
    print(vencedor)

    return {
        "Parceiro": parceiro,
        "Vencedor": vencedor,
        "Lucro": resumo.iloc[0]["lucro"]
    }

# =========================
# EXECUÇÃO
# =========================

arquivos = [
    "dataset_01_parceiroA.csv",
    "dataset_02_parceiroB.csv",
    "dataset_03_parceiroC.csv"
]

resultados = []

for arquivo in arquivos:
    resultado = analisar_teste(arquivo)
    resultados.append(resultado)

# =========================
# PLANILHA CONSOLIDADA
# =========================

planilha = pd.DataFrame(resultados)

planilha.to_csv(
    "historico_testes.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo historico_testes.csv gerado com sucesso!")