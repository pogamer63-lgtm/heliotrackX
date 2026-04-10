import streamlit as st

st.set_page_config(page_title="HelioTrackX", layout="wide")

st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Figtree:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

      :root {
        color-scheme: dark;
        --ink:         #020B10;
        --ink-2:       #071F2B;
        --ink-3:       #0D2E3F;
        --gold:        #F59E0B;
        --gold-dim:    rgba(245,158,11,0.12);
        --gold-glow:   rgba(245,158,11,0.06);
        --gold-bright: #FCD34D;
        --emerald:     #34D399;
        --em-dim:      rgba(52,211,153,0.10);
        --text:        #EDF6FA;
        --muted:       #7FA8BC;
        --dim:         #3E6879;
        --border:      rgba(255,255,255,0.07);
        --border-g:    rgba(245,158,11,0.22);
      }

      html, body,
      [data-testid="stAppViewContainer"],
      [data-testid="stHeader"] {
        background-color: var(--ink) !important;
        color: var(--text);
        font-family: 'Figtree', sans-serif;
      }

      .stApp {
        background-color: var(--ink) !important;
        background-image: radial-gradient(
          circle at 1px 1px,
          rgba(245,158,11,0.045) 1px,
          transparent 0
        ) !important;
        background-size: 28px 28px !important;
      }

      [data-testid="stSidebar"] {
        background-color: var(--ink-2) !important;
        border-right: 1px solid var(--border) !important;
      }

      [data-testid="stSidebarNavLink"],
      [data-testid="stSidebarNavLink"] * {
        color: #EDF6FA !important;
      }

      [data-testid="stSidebarNavLink"][aria-selected="true"] {
        background: rgba(245,158,11,0.12) !important;
      }

      .main .block-container {
        max-width: 1160px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
      }

      * { box-sizing: border-box; }
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
dashboard = st.Page(
    "pages/dashboard.py", title="Dashboard", icon=":material/monitoring:"
)
dokumente = st.Page(
    "pages/dokumente.py", title="Dokumente", icon=":material/description:"
)

pg = st.navigation({" ": [landing, product_info, team, dashboard, dokumente]})
pg.run()
