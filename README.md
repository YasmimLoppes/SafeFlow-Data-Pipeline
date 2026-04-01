# SafeFlow-Data-Pipeline: Processamento e Auditoria de Dados

Projeto integrador desenvolvido como estudo prático de Engenharia de Dados, simulando a construção de uma arquitetura moderna para o setor de fintechs e transações financeiras.

## 🎯 Contexto do Projeto
Este projeto simula um cenário real de negócio em que é solicitado o processamento seguro de transações financeiras e o monitoramento de auditoria.

**A solução permite:**
* Centralizar os dados operacionais de transações.
* Automatizar o processamento e limpeza de dados.
* Garantir a conformidade com a LGPD através de anonimização.
* Apoiar a tomada de decisão estratégica via dashboards.

## 🚀 Objetivos
O projeto tem como objetivo desenvolver uma arquitetura capaz de:
* Realizar ingestão automatizada de dados operacionais.
* Transformar e modelar dados para análise de risco.
* Garantir a segurança e privacidade dos dados sensíveis.
* Disponibilizar informações estruturadas em dashboards analíticos.

## 🔗 Conexão e Exploração de Dados
O pipeline inicia com o tratamento de fontes de dados simuladas para entender a estrutura antes da carga.
Nesta etapa foram realizadas:
* Exploração da estrutura dos dados brutos.
* Identificação de campos sensíveis (IDs de clientes).
* Entendimento do modelo operacional de transações.

## ⚙️ Pipeline de Dados
O pipeline foi construído utilizando uma abordagem **ETL (Extract, Transform, Load)**.
Durante essa etapa foram implementados:
* **Filtro de Auditoria:** Identificação automática de transações acima de R$ 9.000,00.
* **Segurança:** Mascaramento de dados via Hashing (SHA-256).
* **Limpeza:** Tratamento de nulos e padronização de formatos.
* **Diagnóstico:** Resolução de erros de execução e encoding (UTF-8).

## 📊 Dashboard Analítico
Para consumo dos dados, foi estruturada uma visão executiva com métricas como:
* Receita total e volume de transações.
* Distribuição de vendas por categoria.
* Status de auditoria (Normal vs. Revisão Urgente).

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal do pipeline.
* **Pandas:** Manipulação e transformação de dados.
* **Hashlib:** Criptografia e segurança (LGPD).
* **Plotly:** Visualização de dados e gráficos.
* **Git/GitHub:** Controle de versão e documentação.

## 💡 Principais Aprendizados
* Construção de pipelines de dados fim a fim.
* Implementação de regras de negócio em Python.
* Modelagem de dados para segurança da informação.
* Integração entre dados brutos e visões analíticas.

---
**Autora: Yasmim Lopes**
*Estudante de ADS - Unisanta | Foco em Engenharia de Dados*