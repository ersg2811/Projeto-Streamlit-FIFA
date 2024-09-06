import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title='Fifa 2023 - Home',
    page_icon='⚽',
    layout='wide'
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA23 OFFICIAL DATASET!⚽')
st.sidebar.markdown('Desenvolvido por @ERSG2811')

btn = st.link.button(
    'Acesse os dados no Kaggle',
    'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    <div style='text-align: justify; line-height: 1.6; margin-bottom: 20px;'>
    Este dataset contém informações abrangentes sobre jogadores de futebol profissionais, cobrindo os anos de 2017 a 2023. Com mais de <b>17.000 registros</b>, ele oferece detalhes sobre dados demográficos dos jogadores, como idade, nacionalidade e características físicas. Também inclui estatísticas relacionadas ao desempenho, como a classificação geral de habilidades, potencial de desenvolvimento, e o clube atual de cada jogador, além de detalhes sobre o valor de mercado e salário semanal. O conjunto de dados também contempla informações sobre as habilidades técnicas dos jogadores, como o pé preferido, reputação internacional, e o número de movimentos de habilidade.
    </div>

    <div style='text-align: justify; line-height: 1.6; margin-bottom: 20px;'>
    Além disso, o dataset oferece dados contratuais e de filiação a clubes, incluindo a posição preferida do jogador, altura, peso, número da camisa e cláusulas de liberação contratual. Essas informações tornam o dataset útil para análises diversas, como avaliações de desempenho, estudo de jogadores em diferentes posições, bem como a comparação de valores de mercado e desenvolvimento de talentos ao longo do tempo.
    </div>
    """, 
    unsafe_allow_html=True
)