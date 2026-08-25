# criar_exemplo.py - Cria nossa planilha de exemplo
import pandas as pd

# Dados de exemplo com alguns problemas propositais
dados_exemplo = {
    'Operadora': ['Vivo', 'Tim', 'Claro', 'Oi', 'Vivo'],
    'Linha_Telefone': ['(11) 99999-1111', '(21) 88888-2222', '(31) 77777-3333', '(41) 66666-4444', 'abc123'],
    'Valor_Fatura': [150.50, 89.90, 220.00, -50.00, 0.00],
    'Data_Vencimento': ['2024-05-15', '2024-05-20', '2024-05-25', '2024-05-30', '2024-06-05'],
    'Status': ['Pago', 'Pendente', 'Pago', 'Pendente', 'Pendente']
}

# Cria o DataFrame
df = pd.DataFrame(dados_exemplo)

# Salva como Excel
df.to_excel('dados/faturas_input.xlsx', index=False)

print("✅ Arquivo 'faturas_input.xlsx' criado com sucesso!")
print("📊 Dados criados:")
print(df)
