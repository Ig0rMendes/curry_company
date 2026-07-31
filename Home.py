import streamlit as st

st.set_page_config(
    page_title="Dashboard Logística",
    layout="wide"
)

# =====================
# HEADER
# =====================
st.title("📦 Dashboard de Logística e Entregas")

st.markdown(
"""
Este dashboard foi desenvolvido para analisar operações de entrega, permitindo
acompanhar indicadores estratégicos e operacionais sob diferentes perspectivas.

Através das visões disponíveis, é possível entender o desempenho da empresa,
dos entregadores e dos restaurantes parceiros.
"""
)

st.divider()

# =====================
# PROBLEMA DE NEGÓCIO
# =====================
st.header("🎯 Problema de Negócio")

st.markdown(
"""
Empresas de delivery precisam monitorar constantemente sua operação para garantir:

- Eficiência nas entregas  
- Satisfação do cliente  
- Balanceamento entre demanda e capacidade  
- Impacto de fatores externos como trânsito e clima  

Este dashboard ajuda a responder perguntas como:

- Quantos pedidos estão sendo realizados?
- Qual o tempo médio de entrega?
- Quais fatores impactam a performance?
- Quais entregadores e restaurantes se destacam?
- Qual o impacto na avaliação do usuário
"""
)

# =====================
# DATASET
# =====================
st.header("📊 Dataset")

st.markdown(
"""
O conjunto de dados contém informações sobre:

- Pedidos realizados  
- Restaurantes  
- Entregadores  
- Tempo de entrega  
- Condições climáticas  
- Nível de trânsito  
- Avaliações dos clientes

Os dados foram tratados para garantir consistência e confiabilidade nas análises.
"""
)

# =====================
# VISÕES DO DASHBOARD
# =====================
st.header("📈 Visões Disponíveis")

st.markdown(
"""
O dashboard está dividido em três principais visões:

### 📊 Empresa
- Volume de pedidos  
- Tempo médio de entrega  
- Análise por cidade, trânsito e clima  

### 🛵 Entregadores
- Quantidade de entregas por entregador  
- Performance individual  
- Distribuição de idade e veículos  

### 🍽️ Restaurantes
- Volume de pedidos por restaurante  
- Tempo médio de preparo/entrega  
- Comparação entre restaurantes  
### 🔎 Operacional
- Análise no volume de pedidos
- Avaliação do tempo de entrega
- Observar a eficiÊncia em múltiplas entregas
### ⭐ Rating
- Avaliação média distribuída no tempo de entrega
- Observar avaliações em cada região
- Compreender impacto de condições externas nas avaliações
- Avaliar o impacto da experiÊncia do entregador nas avaliações
"""
)

# =====================
# COMO USAR
# =====================
st.header("🧭 Como Utilizar")

st.markdown(
"""
Use os filtros disponíveis na barra lateral para:

- Selecionar intervalo de datas  
- Filtrar por condições de trânsito  
- Filtrar por condições climáticas  

As visualizações serão atualizadas automaticamente com base nos filtros aplicados.
"""
)

# =====================
# FOOTER
# =====================
st.divider()

st.markdown(
"""
Desenvolvido como projeto de análise de dados com foco em tomada de decisão.

🚀 Tecnologias utilizadas:
- Python
- Pandas
- Plotly
- Streamlit

Desenvolvido por [Igor Mendes](https://github.com/Ig0rMendes) ·
    [LinkedIn](www.linkedin.com/in/igor-mendes-a50550239) ·
    [Código-fonte](https://github.com/Ig0rMendes/curry_company)
"""
)
