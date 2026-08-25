# validador.py - Nosso código principal
import pandas as pd
from datetime import datetime

def ler_planilha():
    """Função que lê a planilha Excel"""
    print("📂 Lendo a planilha...")
    
    try:
        # Lê o arquivo Excel
        df = pd.read_excel('dados/faturas_input.xlsx')
        print(f"✅ Planilha lida com sucesso! {len(df)} linhas encontradas.")
        return df
    
    except FileNotFoundError:
        print("❌ ERRO: Arquivo 'faturas_input.xlsx' não encontrado!")
        return None
    except Exception as e:
        print(f"❌ ERRO ao ler planilha: {e}")
        return None

def validar_dados(df):
    """Função que valida os dados das faturas"""
    print("\n🔍 Iniciando validação dos dados...")
    
    problemas = []
    
    # Para cada linha da planilha
    for index, linha in df.iterrows():
        numero_linha = index + 2  # +2 porque Excel começa em 1 e tem cabeçalho
        
        # VALIDAÇÃO 1: Valor deve ser maior que zero
        if linha['Valor_Fatura'] <= 0:
            problemas.append({
                'Linha': numero_linha,
                'Problema': 'Valor inválido',
                'Detalhes': f"Valor {linha['Valor_Fatura']} é menor ou igual a zero"
            })
        
        # VALIDAÇÃO 2: Telefone deve ter formato correto
        telefone = str(linha['Linha_Telefone'])
        if not telefone.startswith('(') or ')' not in telefone:
            problemas.append({
                'Linha': numero_linha,
                'Problema': 'Telefone inválido',
                'Detalhes': f"Telefone {telefone} não está no formato correto"
            })
    
    print(f"✅ Validação concluída! {len(problemas)} problemas encontrados.")
    return problemas

if __name__ == "__main__":
    print("🚀 INICIANDO VALIDADOR DE FATURAS")
    print("=" * 40)
    
    # Passo 1: Ler planilha
    dados = ler_planilha()
    
    if dados is not None:
        # Passo 2: Validar dados
        problemas = validar_dados(dados)
        
        # Passo 3: Mostrar resultados
        if problemas:
            print(f"\n⚠️  PROBLEMAS ENCONTRADOS:")
            for problema in problemas:
                print(f"Linha {problema['Linha']}: {problema['Problema']} - {problema['Detalhes']}")
        else:
            print("\n🎉 Todos os dados estão corretos!")
    
    print("\n✅ Processo finalizado!")
