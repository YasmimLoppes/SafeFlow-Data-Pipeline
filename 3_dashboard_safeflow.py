import pandas as pd
import plotly.express as px

# 1. Lendo os dados finais que VOCÊ gerou no pipeline
df = pd.read_csv('dados_finais_safeflow.csv')

# 2. Criando o gráfico estilo "Donut" (AJUSTADO: valor_transacao)
fig = px.pie(df, 
             names='status_auditoria', 
             values='valor_transacao',  # <--- Mudei aqui!
             hole=0.5,
             title='<b>SafeFlow-Pipeline: Análise de Risco Financeiro</b>',
             color='status_auditoria',
             color_discrete_map={'NORMAL':'#27AE60', 'REVISAO_URGENTE':'#C0392B'})

# 3. Deixando o visual limpo
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_x=0.5, font=dict(size=14))

# 4. Abrindo o gráfico
print("📊 Abrindo o dashboard interativo no seu navegador...")
fig.show()