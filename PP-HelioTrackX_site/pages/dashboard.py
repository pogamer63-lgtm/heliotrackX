import streamlit as st
import streamlit.components.v1 as components


DASHBOARD_URL = (
    "http://192.168.1.2:3000/d/ad7jndw/solarpanel-timeseries"
    "?orgId=1&from=now-6h&to=now&timezone=browser&refresh=5s&kiosk"
)

st.title("Solarpanel Timeseries Dashboard")
st.caption("Eingebettete Ansicht des externen Dashboards")
st.link_button("Dashboard in neuem Tab öffnen", DASHBOARD_URL, use_container_width=False)

components.iframe(DASHBOARD_URL, height=900, scrolling=True)
