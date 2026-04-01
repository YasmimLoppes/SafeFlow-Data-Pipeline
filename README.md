# SafeFlow-Data-Pipeline: Processamento e Auditoria de Dados

Este projeto é um pipeline de Engenharia de Dados focado em resolver problemas reais de uma fintech: o volume de transações e a segurança da informação. O objetivo aqui foi construir um fluxo de ETL que não só move o dado, mas entrega inteligência para o negócio.

## O que o projeto resolve na prática
No dia a dia de um banco, você não pode ter alguém filtrando transações no Excel. O SafeFlow automatiza isso em três frentes:
1. **Filtro de Risco:** O código identifica sozinho qualquer transação de valor alto e já marca para revisão urgente. Isso poupa o tempo que o time de auditoria gastaria filtrando planilhas manualmente.
2. **Segurança e LGPD:** Para proteger a privacidade do cliente, apliquei uma camada de anonimização. O nome ou ID real do cliente é transformado em um código seguro, garantindo que o dado sensível nunca fique exposto.
3. **Automação de Relatórios:** O sistema processa centenas de registros em segundos e já gera um resumo pronto para análise, transformando números brutos em informação útil.

## Ferramentas que utilizei
Para montar essa estrutura, usei Python e a biblioteca Pandas para toda a parte de limpeza e filtros. Também usei a biblioteca Hashlib para garantir a segurança dos dados e o Plotly para gerar a visualização final do projeto.

Durante o desenvolvimento, lidei com desafios reais de infraestrutura, como a gestão de ambientes virtuais e erros de leitura de arquivos no Windows, o que me ajudou a entender melhor os bastidores da Engenharia de Dados.

## Como o pipeline está organizado
Dividi o código em etapas para ficar fácil de manter:
1. `1_ingestao_safeflow.py`: Onde eu gero e recebo os dados brutos.
2. `2_transformacao_safeflow.py`: É onde o processamento acontece (Limpeza + Regras de Risco + LGPD).
3. `3_dashboard_safeflow.py`: Onde eu gero a visão executiva do projeto.

---
**Desenvolvido por Yasmim Lopes**
*Estudante de ADS - Unisanta | Foco em Engenharia de Dados*
