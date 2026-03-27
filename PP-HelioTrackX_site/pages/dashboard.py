import streamlit as st


DASHBOARD_URL = (
    "http://192.168.1.2:3000/d/ad7jndw/solarpanel-timeseries"
    "?orgId=1&from=now-6h&to=now&timezone=browser&refresh=5s&kiosk"
)

st.title("Solarpanel Timeseries Dashboard")
st.caption("Dashboard wird in einem neuen Tab geöffnet")
st.link_button(
    "Grafana-Dashboard in neuem Tab öffnen",
    DASHBOARD_URL,
    use_container_width=False,
    type="primary",
)
