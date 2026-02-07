import streamlit as st
import plotly.graph_objects as go

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="IMC PRO | Fabre",
    page_icon="💪",
    layout="centered"
)

# ==========================================
# TEMA ESCURO PERSONALIZADO
# ==========================================
st.markdown("""
    <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        h1, h2, h3 {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# FUNÇÃO DE CLASSIFICAÇÃO
# ==========================================
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso", "#3498db"
    elif imc < 25:
        return "Peso normal", "#2ecc71"
    elif imc < 30:
        return "Sobrepeso", "#f39c12"
    elif imc < 35:
        return "Obesidade Grau I", "#e74c3c"
    elif imc < 40:
        return "Obesidade Grau II", "#c0392b"
    else:
        return "Obesidade Grau III", "#7f0000"

# ==========================================
# INTERFACE
# ==========================================
st.title("💪 IMC PRO")
st.markdown("### Dashboard Corporal Inteligente")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)

with col2:
    altura = st.number_input("Altura (m)", min_value=0.0, step=0.01)

st.markdown("")

# ==========================================
# CÁLCULO
# ==========================================
if st.button("🚀 Calcular IMC"):

    if peso > 0 and altura > 0:

        imc = peso / (altura ** 2)
        classificacao, cor = classificar_imc(imc)

        st.markdown("## 📊 Resultado")
        st.metric("Seu IMC", f"{imc:.2f}")

        st.markdown(
            f"<h3 style='color:{cor}'>Classificação: {classificacao}</h3>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        # ==========================================
        # GRÁFICO INTERATIVO (PLOTLY)
        # ==========================================
        st.markdown("### 📈 Indicador Visual Interativo")

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=imc,
            title={'text': "IMC"},
            gauge={
                'axis': {'range': [0, 45]},
                'bar': {'color': cor},
                'steps': [
                    {'range': [0, 18.5], 'color': "#1f4e79"},
                    {'range': [18.5, 25], 'color': "#145a32"},
                    {'range': [25, 30], 'color': "#7d6608"},
                    {'range': [30, 35], 'color': "#78281f"},
                    {'range': [35, 45], 'color': "#4a0404"}
                ],
            }
        ))

        fig.update_layout(
            paper_bgcolor="#0E1117",
            font={'color': "white"}
        )

        st.plotly_chart(fig)

        st.markdown("---")

        # ==========================================
        # FEEDBACK PERSONALIZADO
        # ==========================================
        if classificacao == "Peso normal":
            st.success("Excelente! Continue mantendo hábitos saudáveis 💪")
        elif classificacao == "Sobrepeso":
            st.warning("Atenção! Pequenos ajustes já trazem grandes resultados.")
        else:
            st.error("Recomenda-se procurar orientação profissional.")

    else:
        st.error("Digite valores válidos maiores que zero.")

# ==========================================
# RODAPÉ PROFISSIONAL
# ==========================================
st.markdown("---")
st.markdown(
    "<center>Desenvolvido por: <b>Fabre</b> 💻🚀</center>",
    unsafe_allow_html=True
)
