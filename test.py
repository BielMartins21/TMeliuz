import pandas as pd


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


def analisar_teste(caminho_csv):

    df = pd.read_csv(caminho_csv)

    df.columns = [c.strip().lower() for c in df.columns]

    df["comissão"] = df["comissão"].apply(limpar_moeda)
    df["cashback"] = df["cashback"].apply(limpar_moeda)
    df["vendas totais"] = df["vendas totais"].apply(limpar_moeda)

    df["lucro"] = df["comissão"] - df["cashback"]

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
    lucro = resumo.iloc[0]["lucro"]

    resultado = f"{vencedor} apresentou o maior lucro"
    decisao = f"Escalar {vencedor} para 100% do tráfego"

    print(f"\nParceiro: {parceiro}")
    print(resumo)

    print(f"\nResultado: {resultado}")
    print(f"Decisão: {decisao}")

    with open(f"relatorio_{parceiro}.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Parceiro: {parceiro}\n")
        arquivo.write(f"Grupo vencedor: {vencedor}\n")
        arquivo.write(f"Lucro: R$ {lucro:.2f}\n")
        arquivo.write(f"Resultado: {resultado}\n")
        arquivo.write(f"Decisão: {decisao}\n")

    return {
        "Nome do teste": parceiro,
        "Descrição": "Teste A/B de cashback",
        "Resultado": resultado,
        "Decisão": decisao
    }


arquivos = [
    "dataset_01_parceiroA.csv",
    "dataset_02_parceiroB.csv",
    "dataset_03_parceiroC.csv"
]

resultados = []

for arquivo in arquivos:
    resultado = analisar_teste(arquivo)
    resultados.append(resultado)

historico = pd.DataFrame(resultados)

historico.to_csv(
    "historico_testes.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArquivo historico_testes.csv gerado com sucesso!")