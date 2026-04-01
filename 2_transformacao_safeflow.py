import pandas as pd
import hashlib

def processar_safeflow():
    print("🔧 Processando dados e aplicando regras de segurança...")
    
    # 1. Leitura
    df = pd.read_csv('dados_brutos_safeflow.csv')
    
    # 2. ANONIMIZAÇÃO (LGPD) - Mascarando o código do cliente
    # Isso prova que você sabe lidar com dados sensíveis
    df['cod_cliente_mascarado'] = df['cod_cliente'].apply(
        lambda x: hashlib.md5(x.encode()).hexdigest()[:8]
    )
    
    # 3. REGRA DE FRAUDE (Business Intelligence)
    # Transações acima de 9k são marcadas para revisão manual
    df['status_auditoria'] = df['valor_transacao'].apply(
        lambda x: 'REVISAO_URGENTE' if x > 9000 else 'NORMAL'
    )
    
    # 4. CRIANDO UM RESUMO PARA O DASHBOARD (Aquela visão das fotos!)
    resumo = df.groupby('status_auditoria')['valor_transacao'].agg(['count', 'sum']).reset_index()
    
    # 5. SALVANDO O RESULTADO FINAL
    df.drop(columns=['cod_cliente'], inplace=True) # Remove o dado original por segurança
    df.to_csv('dados_finais_safeflow.csv', index=False)
    
    print("\n--- RELATÓRIO DE PROCESSAMENTO ---")
    print(resumo)
    print("\n🚀 Pipeline finalizado! Dados prontos para o Dashboard.")

if __name__ == "__main__":
    processar_safeflow()