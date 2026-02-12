import streamlit as st

st.set_page_config(page_title="HelioTrackX", layout="wide")


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
