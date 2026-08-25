# Validador de Faturas de Telecom

Script em Python que valida faturas de telefonia a partir de uma planilha Excel (operadora, telefone, valor) e gera um relatório apontando o que está errado.

Projeto propositalmente simples e direto ao ponto - sem a complexidade dos outros dois repositórios.

## Funcionalidades

- Lê uma planilha Excel com faturas
- Valida três regras: valor da fatura maior que zero, telefone com formato básico, e operadora preenchida
- Gera um relatório Excel com 3 abas: problemas encontrados, dados OK, e um resumo

## Pré-requisitos

- Python 3.10 ou superior
- pip

## Instalação

pip install pandas openpyxl xlsxwriter

## Como usar

Gerar uma planilha de exemplo (opcional, só se você não tiver uma planilha real):

python dados/criar_exemplo.py

Rodar o validador (sempre a partir da pasta raiz do projeto):

python src/main.py

Isso lê dados/faturas_input.xlsx e gera dados/relatorio_validacao_<data_hora>.xlsx.

## Estrutura da planilha de entrada

| Coluna | Tipo | Exemplo |
| --- | --- | --- |
| Operadora | texto | Vivo |
| Linha_Telefone | texto | (11) 99999-1111 |
| Valor_Fatura | número | 150.50 |
| Data_Vencimento | data | 2026-05-15 |
| Status | texto | Pago |

## Estrutura do projeto

validador-faturas-telecom/
├── src/
│   ├── main.py
│   ├── validador.py
│   └── gerar_relatorio.py
├── dados/
│   ├── criar_exemplo.py
│   └── faturas_input.xlsx
└── .gitignore
