<div style="background-color: #000000; color: #ffffff; padding: 20px; border-radius: 10px;">

# 🚀 Teste Técnico - Estágio Growth AI-Native | Méliuz

## 📌 Apresentação

Este repositório contém a solução desenvolvida para o teste técnico da vaga de **Estágio Growth AI-Native** da Méliuz.

A proposta foi criar uma solução reutilizável para analisar testes A/B de cashback e indicar qual grupo deve ser escalado para 100% do tráfego com base nos resultados obtidos.

---

## ⚙️ Como a solução funciona

O script recebe um arquivo CSV contendo os dados do teste A/B.

A partir desses dados, ele:

* 📥 realiza a leitura dos dados;
* 🧹 faz o tratamento e limpeza das informações;
* 💰 converte os valores monetários para formato numérico;
* 📊 agrupa os resultados por variante;
* 🧮 calcula as principais métricas;
* 📈 calcula o lucro líquido (comissão - cashback);
* 🏆 identifica o grupo vencedor;
* 📝 gera um resumo da análise;
* 📋 registra o resultado em uma planilha CSV de acompanhamento.

A mesma solução pode ser utilizada para qualquer arquivo que siga o formato disponibilizado no teste.

---

## 📂 Estrutura do projeto

```text
datasets/
scripts/
relatorios/
resultados/

README.md
requirements.txt
```

---

## ▶️ Como executar

### 1. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o script

```bash
python scripts/analisar_teste.py
```

---

## 📊 Resultados

Após a execução são gerados:

* 📄 Relatórios individuais para cada parceiro analisado;
* 📈 Arquivo de acompanhamento contendo o histórico das análises realizadas.

---

## 🎯 Conclusões obtidas

### Parceiro A

🏆 Grupo recomendado: **Grupo 1**

### Parceiro B

🏆 Grupo recomendado: **Grupo 1**

### Parceiro C

🏆 Grupo recomendado: **Grupo 1**

A recomendação foi baseada no lucro líquido obtido por cada variante durante o período analisado.

---

## 🗂️ Arquivo de acompanhamento

O arquivo `historico_testes.csv` contém o resumo dos testes executados, incluindo:

* nome do teste;
* resultado;
* decisão recomendada.

---

## 🛠️ Tecnologias utilizadas

* Python
* Pandas
* CSV 
* GitHub

---

## 👨‍💻 Autor

**Gabriel Rodrigues Martins**

</div>
