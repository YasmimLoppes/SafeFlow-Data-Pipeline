# SafeFlow-Data-Pipeline: Processamento e Auditoria de Dados

Projeto focado na construção de uma arquitetura de dados moderna para o setor de fintechs e transações financeiras, priorizando a automação de fluxos e a segurança da informação.

## 🎯 Contexto do Projeto
Este projeto simula um cenário real de negócio onde é necessário o processamento seguro de transações financeiras e o monitoramento automatizado de conformidade.

**A solução permite:**
* Centralizar dados operacionais de transações.
* Automatizar o processamento e a limpeza de dados em escala.
* Garantir conformidade com a LGPD através de técnicas de anonimização.
* Apoiar a tomada de decisão estratégica via dashboards analíticos.

## 🚀 Objetivos
Desenvolver uma arquitetura capaz de:
* Realizar ingestão automatizada de dados operacionais.
* Transformar e modelar dados para análise de risco e auditoria.
* Garantir a segurança e privacidade de dados sensíveis.
* Disponibilizar métricas estruturadas para o negócio.

## ⚙️ Pipeline de Dados
O pipeline segue a abordagem **ETL (Extract, Transform, Load)** com as seguintes implementações:
* **Filtro de Auditoria:** Identificação automática de transações críticas (acima de R$ 9.000,00) para revisão imediata.
* **Segurança:** Mascaramento de dados sensíveis via Hashing (SHA-256), garantindo que a identidade do cliente seja protegida durante todo o processamento.
* **Limpeza e Padronização:** Tratamento de valores nulos e normalização de formatos de arquivos.

## 📊 Dashboard Analítico
Estruturação de visão executiva para acompanhamento de:
* Receita total e volume transacionado.
* Distribuição de vendas por categoria de produto.
* Status de conformidade e risco (Normal vs. Revisão Urgente).

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal para desenvolvimento do pipeline.
* **Pandas:** Manipulação, limpeza e transformação de dados.
* **Hashlib:** Implementação de segurança e criptografia (LGPD).
* **Plotly:** Geração de visualizações e indicadores de desempenho.
* **Git/GitHub:** Controle de versão e documentação técnica.

## 💡 Principais Aprendizados Técnicos
* Construção de pipelines de dados fim a fim (End-to-End).
* Implementação de regras de negócio complexas via código.
* Modelagem de dados focada em segurança da informação.
* Automação de fluxos de trabalho para redução de processos manuais.

---
**Autora: Yasmin Lopes**
*Engenharia de Dados | Desenvolvedora Python & SQL*