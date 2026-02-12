import streamlit as st


st.title("HelioTrackX Produktdaten")
st.caption("Technischer Überblick über die adaptive Solarzellen-Nachführung")

col1, col2 = st.columns([1.25, 1], gap="large")

with col1:
    st.subheader("Systemkern")
    st.markdown(
        """
        - Adaptive Lichtsensorik mit kontinuierlicher Messung
        - Motorisierte 2-Achsen-Steuerung für präzise Nachführung
        - Betriebsmodi: Performance, Balanced, Safety
        - Telemetrie für Monitoring, Diagnose und Reporting
        """
    )

    st.subheader("Mehrwert im Betrieb")
    st.markdown(
        """
        - Höherer Ertrag bei diffuser Einstrahlung
        - Reduktion manueller Wartungsaufwände
        - Reproduzierbare Betriebsdaten für Optimierung
        - Skalierbar von Pilotanlagen bis Solarpark
        """
    )

with col2:
    st.subheader("Technische Eckdaten")
    st.metric("Nachführung", "360 Grad", "dynamisch")
    st.metric("Reaktionszeit", "< 2 s", "typisch")
    st.metric("Betriebsmodus", "24/7", "automatisiert")

st.divider()
st.subheader("Integrationspfade")
st.markdown(
    """
    1. Neubau: Direkte Auslegung auf HelioTrackX-Komponenten.
    2. Retrofit: Nachrüstung in bestehende Solarstrukturen.
    3. Hybrid: Kombination aus starrer und adaptiver Fläche.
    """
)
st.caption("Die Auslegung erfolgt projektspezifisch je nach Standort und Anlagenkonzept.")
