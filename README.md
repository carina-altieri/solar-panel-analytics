# Solar Panel Analytics

Projeto de simulação e análise de dados de painéis solares, utilizando Python, MySQL e visualização de dados para gerar insights sobre produção de energia e falhas operacionais.

---

## Objetivo

Desenvolver um pipeline de dados que:

1. Simula dados de operação de painéis solares
2. Armazena os dados em um banco MySQL
3. Realiza análises exploratórias para geração de insights

---

## Funcionalidades

###  Geração de Dados Simulados

* Criação de uma base de dados realista de painéis solares
* Simulação de variáveis como:

  * Temperatura do painel
  * Irradiação solar
  * Hora do dia
  * Status do painel (normal ou falha)

---

### Integração com Banco de Dados

* Conexão com MySQL utilizando `mysql.connector`
* Criação automática do banco e tabelas
* Inserção dos dados simulados no banco

---

### Exportação de Dados

* Geração de arquivo `.csv` com os dados simulados
* Possibilidade de uso dos dados para análises externas

---

### Análise Exploratória de Dados

* Cálculo da energia gerada (Wh)
* Análise da produção ao longo do tempo

---

### Visualização de Dados

* Geração de gráficos como:

  * Energia gerada por dia
  * Meses mais produtivos
  * Distribuição por horário
  * Frequência de falhas

---

### Análise de Falhas

* Identificação de horários com maior incidência de falhas
* Relação entre temperatura do painel e falhas
* Porcentagem de falhas por faixa de temperatura

---

### Pipeline

* Simulação → Exportação (.csv) → Armazenamento (MySQL) → Análise

---

### Flexibilidade de Fonte de Dados

* Leitura dos dados via CSV
* Possibilidade de leitura direta do MySQL

---

## Tecnologias e Bibliotecas

### Análise de dados

* pandas
* matplotlib
* seaborn
* mysql.connector

### Backend / geração de dados

* numpy
* datetime
* python-dateutil

### Banco de dados

* MySQL

---

##  Estrutura do Projeto

### `config_py`
Arquivo oculto contendo a senha do seu servidor MySQL local.

```python
MYSQL_PASSWORD = "sua_senha_aqui"
```

> Este arquivo não está incluído no repositório por conter informações sensíveis.
> Certifique-se de criá-lo manualmente antes de executar o projeto.

> Recomenda-se adicionar o arquivo ao `.gitignore` para evitar o envio de credenciais.

---

###  `db_connection.py`

Responsável por criar a conexão com o banco de dados MySQL.

* Utiliza a biblioteca `mysql.connector`
* Importa credenciais do arquivo `config.py`
* Função principal: `get_connection()`

---

### `criar_banco.py`

Script para criação do banco de dados e tabela.

* Importa `get_connection`
* Executa comandos SQL de inicialização

---

### `main.py`

Arquivo principal do projeto.

Responsável por:

* Gerar dados simulados
* Exportar dados para CSV
* Inserir dados no MySQL

---

### Notebook de Análise (`analises.ipynb`)

Responsável pelas análises e visualizações.

* Leitura dos dados via CSV
* Geração de gráficos e métricas

> Obs: Também é possível conectar diretamente ao banco de dados.

---

## Como Executar

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd solar-panel-analytics
```

---

### 2. Instale as dependências

```bash
pip install pandas matplotlib seaborn numpy python-dateutil mysql-connector-python
```

---

### 3. Configure o banco

Crie um arquivo `config.py`:

```python
MYSQL_PASSWORD = "sua_senha_aqui"
```

---

### 4. Crie o banco de dados

```bash
python criar_banco.py
```

---

### 5. Gere os dados

```bash
python main.py
```

---

### 6. Execute as análises

```bash
jupyter notebook
```

Abra o notebook e execute as células.

---

## Insights Gerados

* Identificação dos horários com maior geração de energia
* Análise dos meses mais produtivos
* Relação entre temperatura e desempenho
* Identificação de padrões de falha

---

## Melhorias Futuras

* Conexão direta do notebook com MySQL
* Implementação de modelos de Machine Learning
* Criação de dashboards interativos (Streamlit / Power BI)
* Uso de dados reais

---

## Licença

Projeto de código aberto desenvolvido para fins educacionais e portfólio. 

