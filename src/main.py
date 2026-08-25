import sys
sys.path.append('src')

from validador import ler_planilha
from gerar_relatorio import validar_e_gerar_relatorio


def main():
    print("🏁 INICIANDO VALIDAÇÃO DE FATURAS")
    
    # Validar planilha
    problemas = ler_planilha()
    
    # Gerar relatório
    relatorio = validar_e_gerar_relatorio()
    
    print("✅ VALIDAÇÃO CONCLUÍDA!")

if __name__ == "__main__":
    main()
