<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {
      background-color: #000000;
      color: #ffffff;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      line-height: 1.6;
    }
    .container {
      padding: 20px;
      border-radius: 10px;
      max-width: 900px;
      margin: 0 auto;
    }
    h1, h2, h3 {
      color: #ffffff;
      margin-top: 20px;
    }
    h1 {
      border-bottom: 2px solid #4CAF50;
      padding-bottom: 10px;
    }
    code {
      background-color: #1a1a1a;
      padding: 2px 6px;
      border-radius: 4px;
      color: #90EE90;
    }
    pre {
      background-color: #1a1a1a;
      padding: 15px;
      border-radius: 5px;
      overflow-x: auto;
    }
    hr {
      border: none;
      border-top: 1px solid #333;
      margin: 20px 0;
    }
    ul {
      list-style-position: inside;
    }
    li {
      margin: 8px 0;
    }
    strong {
      color: #4CAF50;
    }
  </style>
</head>
<body>
<div class="container">

<h1>🚀 Teste Técnico - Estágio Growth AI-Native | Méliuz</h1>

<h2>📌 Apresentação</h2>
<p>Este repositório contém a solução desenvolvida para o teste técnico da vaga de <strong>Estágio Growth AI-Native</strong> da Méliuz.</p>
<p>A proposta foi criar uma solução reutilizável para analisar testes A/B de cashback e indicar qual grupo deve ser escalado para 100% do tráfego com base nos resultados obtidos.</p>

<hr>

<h2>⚙️ Como a solução funciona</h2>
<p>O script recebe um arquivo CSV contendo os dados do teste A/B.</p>
<p><strong>A partir desses dados, ele:</strong></p>
<ul>
  <li>📥 realiza a leitura dos dados;</li>
  <li>🧹 faz o tratamento e limpeza das informações;</li>
  <li>💰 converte os valores monetários para formato numérico;</li>
  <li>📊 agrupa os resultados por variante;</li>
  <li>🧮 calcula as principais métricas;</li>
  <li>📈 calcula o lucro líquido (comissão - cashback);</li>
  <li>🏆 identifica o grupo vencedor;</li>
  <li>📝 gera um resumo da análise;</li>
  <li>📋 registra o resultado em uma planilha CSV de acompanhamento.</li>
</ul>
<p>A mesma solução pode ser utilizada para qualquer arquivo que siga o formato disponibilizado no teste.</p>

<hr>

<h2>📂 Estrutura do projeto</h2>
<pre>datasets/
scripts/
relatorios/
resultados/

README.md
requirements.txt</pre>

<hr>

<h2>▶️ Como executar</h2>

<h3>1. Instalar as dependências</h3>
<pre>pip install -r requirements.txt</pre>

<h3>2. Executar o script</h3>
<pre>python scripts/analisar_teste.py</pre>

<hr>

<h2>📊 Resultados</h2>
<p><strong>Após a execução são gerados:</strong></p>
<ul>
  <li>📄 Relatórios individuais para cada parceiro analisado;</li>
  <li>📈 Arquivo de acompanhamento contendo o histórico das análises realizadas.</li>
</ul>

<hr>

<h2>🎯 Conclusões obtidas</h2>

<h3>Parceiro A</h3>
<p>🏆 Grupo recomendado: <strong>Grupo 1</strong></p>

<h3>Parceiro B</h3>
<p>🏆 Grupo recomendado: <strong>Grupo 1</strong></p>

<h3>Parceiro C</h3>
<p>🏆 Grupo recomendado: <strong>Grupo 1</strong></p>

<p>A recomendação foi baseada no lucro líquido obtido por cada variante durante o período analisado.</p>

<hr>

<h2>🗂️ Arquivo de acompanhamento</h2>
<p>O arquivo <code>historico_testes.csv</code> contém o resumo dos testes executados, incluindo:</p>
<ul>
  <li>nome do teste;</li>
  <li>resultado;</li>
  <li>decisão recomendada.</li>
</ul>

<hr>

<h2>🛠️ Tecnologias utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>CSV</li>
  <li>GitHub</li>
</ul>

<hr>

<h2>👨‍💻 Autor</h2>
<p><strong>Gabriel Rodrigues Martins</strong></p>

</div>
</body>
</html>