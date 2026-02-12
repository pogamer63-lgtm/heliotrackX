import streamlit as st

st.set_page_config(page_title="HelioTrackX", layout="wide")

st.markdown(
    """
    <style>
      :root {
        color-scheme: dark;
        --background-color: #04151d;
        --secondary-background-color: #0a2733;
        --text-color: #f4fbff;
        --primary-color: #f7b731;
      }

      html,
      body,
      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stHeader"] {
        background-color: #04151d;
        color: #f4fbff;
      }

      [data-testid="stSidebar"] {
        background-color: #0a2733;
      }

      [data-testid="stSidebar"] * {
        color: #f4fbff;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

landing = st.Page(
    "pages/landing.py", title="Start", icon=":material/sunny:", default=True
)
product_info = st.Page(
    "pages/product_info.py", title="Produkt", icon=":material/bolt:"
)
team = st.Page(
    "pages/team.py", title="Team", icon=":material/groups:"
)

pg = st.navigation({" ": [landing, product_info, team]})
pg.run()
