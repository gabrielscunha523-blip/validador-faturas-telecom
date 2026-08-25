# gerar_relatorio.py - Gera relatório detalhado
import pandas as pd
from datetime import datetime

def validar_e_gerar_relatorio():
    """Valida dados e gera relatório em Excel"""
    
    # Lê a planilha
    try:
        df = pd.read_excel('dados/faturas_input.xlsx')
        print(f"📂 Planilha lida: {len(df)} linhas")
    except Exception as e:
        print(f"❌ Erro: {e}")
        return
    
    # Lista para problemas encontrados
    relatorio = []
    dados_ok = []
    
    # Valida cada linha
    for index, linha in df.iterrows():
        numero_linha = index + 2
        problemas_linha = []
        
        # Validação 1: Valor
        if linha['Valor_Fatura'] <= 0:
            problemas_linha.append('Valor inválido')
        
        # Validação 2: Telefone
        telefone = str(linha['Linha_Telefone'])
        if not telefone.startswith('(') or ')' not in telefone:
            problemas_linha.append('Telefone inválido')
        
        # Validação 3: Operadora
        if pd.isna(linha['Operadora']) or linha['Operadora'].strip() == '':
            problemas_linha.append('Operadora em branco')
        
        # Se tem problemas, adiciona ao relatório
        if problemas_linha:
            relatorio.append({
                'Linha_Excel': numero_linha,
                'Operadora': linha['Operadora'],
                'Telefone': linha['Linha_Telefone'],
                'Valor': linha['Valor_Fatura'],
                'Problemas': ' | '.join(problemas_linha)
            })
        else:
            # Se não tem problemas, está OK
            dados_ok.append({
                'Linha_Excel': numero_linha,
                'Operadora': linha['Operadora'],
                'Telefone': linha['Linha_Telefone'],
                'Valor': linha['Valor_Fatura'],
                'Status': 'OK'
            })
    
    # Cria DataFrames
    df_problemas = pd.DataFrame(relatorio)
    df_ok = pd.DataFrame(dados_ok)
    
    # Salva relatório em Excel
    nome_arquivo = f'dados/relatorio_validacao_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    
    with pd.ExcelWriter(nome_arquivo, engine='xlsxwriter') as writer:
        df_problemas.to_excel(writer, sheet_name='Problemas', index=False)
        df_ok.to_excel(writer, sheet_name='Dados_OK', index=False)
        
        # Cria planilha de resumo
        resumo = pd.DataFrame({
            'Métrica': ['Total de linhas', 'Linhas com problemas', 'Linhas OK', 'Taxa de erro'],
            'Valor': [len(df), len(df_problemas), len(df_ok), f"{len(df_problemas)/len(df)*100:.1f}%"]
        })
        resumo.to_excel(writer, sheet_name='Resumo', index=False)
    
    print(f"📊 Relatório salvo em: {nome_arquivo}")
    print(f"📈 Resumo: {len(df_problemas)} problemas de {len(df)} linhas")
    
    return nome_arquivo

if __name__ == "__main__":
    print("📋 GERADOR DE RELATÓRIO DE VALIDAÇÃO")
    print("=" * 40)
    gerar_relatorio = validar_e_gerar_relatorio()