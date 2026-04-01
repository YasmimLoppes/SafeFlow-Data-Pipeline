import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_dados_mercado():
    print("🚀 Iniciando geração de dados para SafeFlow...")
    categorias = ['Alimentação', 'Tecnologia', 'Saúde', 'Transporte', 'Lazer']
    moedas = ['BRL', 'USD']
    dados = []
    
    for i in range(300):
        valor = round(random.uniform(5.0, 12000.0), 2)
        # Gerando datas dos últimos 15 dias
        data = (datetime.now() - timedelta(days=random.randint(0, 15), minutes=random.randint(0, 1440)))
        
        dados.append({
            'transacao_id': f'SFL-{202600 + i}',
            'data_hora': data.strftime('%Y-%m-%d %H:%M:%S'),
            'valor_transacao': valor,
            'moeda': random.choice(moedas),
            'categoria': random.choice(categorias),
            'cod_cliente': f'USER-{random.randint(10, 99)}'
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('dados_brutos_safeflow.csv', index=False)
    print("✅ Sucesso: 'dados_brutos_safeflow.csv' criado!")

if __name__ == "__main__":
    gerar_dados_mercado()