# SafeFlow-Data-Pipeline: Processamento e Auditoria de Dados

Projeto focado na construção de uma arquitetura de dados moderna para o setor de fintechs e transações financeiras, priorizando a automação de fluxos e a segurança da informação.

## 🎯 Contexto do Projeto
Este projeto simula um cenário real de negócio onde é necessário o processamento seguro de transações financeiras e o monitoramento automatizado de conformidade.

**A solução permite:**
* Centralizar dados operacionais de transações.
* Automatizar o processamento e a limpeza de dados em escala.
* Garantir conformidade com a LGPD através de técnicas de anonimização.
* Apoiar a tomada de decisão estratégica via dashboards analíticos.

## 🧠 Decisões Técnicas (O "Porquê" das Ferramentas)
Para este projeto, escolhi ferramentas que equilibram performance e segurança, simulando um ambiente real de produção:

* **Por que Python e Pandas?** Escolhi essa stack pela versatilidade no tratamento de diferentes formatos de arquivos e pela facilidade em implementar regras de negócio complexas (como o filtro de auditoria) de forma rápida e eficiente.
* **Por que Hashing (SHA-256) para LGPD?** Implementei o Hashing para garantir que a empresa identifique que uma transação pertence a um cliente único para fins estatísticos, sem nunca expor a identidade real dele. É o equilíbrio perfeito entre análise de dados e privacidade.
* **Por que Plotly para o Dashboard?** Optei pelo Plotly por permitir a criação de visualizações interativas que podem ser facilmente integradas em aplicações web, entregando valor direto para a tomada de decisão.
* **Por que Git/GitHub?** Para garantir o versionamento do código e a rastreabilidade de cada alteração, prática indispensável em qualquer time de engenharia moderno.

## 🚀 Objetivos do Pipeline
* **Ingestão:** Coleta automatizada de registros operacionais.
* **Filtro de Auditoria:** Identificação automática de transações críticas (acima de R$ 9.000,00) para revisão imediata.
* **Segurança:** Mascaramento de dados sensíveis para proteção da privacidade.
* **Limpeza:** Tratamento de nulos e normalização de formatos para garantir a integridade.

## 📊 Entrega de Valor (Dashboard)
Estruturação de visão executiva para acompanhamento de:
* Receita total e volume transacionado.
* Distribuição de vendas por categoria de produto.
* Status de conformidade e risco (Normal vs. Revisão Urgente).

## 🛠️ Tecnologias Utilizadas
* **Python** (Linguagem Principal)
* **Pandas** (Manipulação e ETL)
* **Hashlib** (Segurança e Criptografia)
* **Plotly** (Visualização de Dados)
* **Git/GitHub** (Versionamento)

## 💡 Principais Aprendizados
* Construção de pipelines de dados fim a fim (End-to-End).
* Implementação de regras de negócio complexas via código.
* Modelagem de dados focada em segurança da informação (Security by Design).
* Automação de fluxos para redução de processos manuais e erros humanos.

---
**Autora: Yasmim Lopes**
*Engenharia de Dados | Desenvolvedora Python & SQL*