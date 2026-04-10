import streamlit as st

st.markdown(
    """
    <style>
      .px { font-family: 'Figtree', sans-serif; color: var(--text); }

      .page-header { margin-bottom: 1.8rem; padding-bottom: 1.3rem; border-bottom: 1px solid var(--border); }

      .page-label {
        display: inline-flex; align-items: center; gap: 0.55rem;
        font-family: 'Space Mono', monospace; font-size: 0.7rem;
        letter-spacing: 0.2em; color: var(--gold); text-transform: uppercase; margin-bottom: 0.55rem;
      }
      .page-label::before {
        content: ''; display: inline-block; width: 18px; height: 2px;
        background: var(--gold); flex-shrink: 0;
      }
      .page-title {
        font-family: 'Archivo Black', sans-serif; font-weight: 400;
        font-size: clamp(1.8rem, 3.5vw, 2.7rem); margin: 0 0 0.3rem 0; letter-spacing: -0.01em;
      }
      .page-sub { color: var(--muted); font-size: 0.97rem; margin: 0; }

      .card {
        border: 1px solid var(--border); border-radius: 18px;
        background: rgba(7,31,43,0.6); padding: 1.4rem 1.5rem;
        position: relative; overflow: hidden;
      }
      .card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, var(--gold), transparent 70%);
      }
      .card-label {
        font-family: 'Space Mono', monospace; font-size: 0.68rem;
        letter-spacing: 0.18em; color: var(--gold); text-transform: uppercase; margin-bottom: 1rem;
      }
      .feature-list { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 0.7rem; }
      .feature-list li { display: flex; align-items: flex-start; gap: 0.65rem; color: var(--muted); font-size: 0.92rem; line-height: 1.55; }
      .feature-list li::before { content: '→'; color: var(--gold); font-family: 'Space Mono', monospace; font-size: 0.78rem; flex-shrink: 0; margin-top: 0.1rem; }

      .metric-card {
        border: 1px solid var(--border-g); border-radius: 18px;
        background: linear-gradient(135deg, rgba(245,158,11,0.1) 0%, rgba(7,31,43,0.7) 70%);
        padding: 1.4rem; display: flex; flex-direction: column;
        justify-content: center; align-items: center; text-align: center; gap: 0.2rem; height: 100%;
      }
      .metric-value {
        font-family: 'Space Mono', monospace; font-size: 2.6rem; font-weight: 700;
        color: var(--gold); line-height: 1; letter-spacing: -0.02em;
      }
      .metric-label { color: var(--text); font-size: 0.9rem; font-weight: 600; margin-top: 0.25rem; }
      .metric-sub { font-family: 'Space Mono', monospace; font-size: 0.68rem; color: var(--dim); text-transform: uppercase; letter-spacing: 0.12em; }

      .feature-list-2col { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.7rem 2rem; }

      .integration-section { border: 1px solid var(--border); border-radius: 18px; background: rgba(7,31,43,0.5); overflow: hidden; }
      .integration-header { padding: 0.95rem 1.4rem; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 0.75rem; }
      .integration-header h2 { margin: 0; font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 1.05rem; letter-spacing: -0.01em; }
      .integration-header-line { flex: 1; height: 1px; background: linear-gradient(to right, var(--border-g), transparent); }
      .integration-items { display: grid; grid-template-columns: repeat(3, 1fr); }
      .integration-item { padding: 1.15rem 1.3rem; border-right: 1px solid var(--border); transition: background 0.2s; }
      .integration-item:last-child { border-right: none; }
      .integration-item:hover { background: rgba(245,158,11,0.04); }
      .integration-num { font-family: 'Space Mono', monospace; font-size: 0.68rem; color: var(--emerald); letter-spacing: 0.14em; margin-bottom: 0.45rem; text-transform: uppercase; }
      .integration-title { font-weight: 700; font-size: 0.93rem; margin-bottom: 0.3rem; color: var(--text); }
      .integration-desc { color: var(--muted); font-size: 0.86rem; line-height: 1.55; }

      .footer-note { margin-top: 0.85rem; color: var(--dim); font-size: 0.74rem; font-family: 'Space Mono', monospace; }

      .fade-up { animation: fadeUp 0.75s cubic-bezier(0.22,1,0.36,1) both; }
      .d1 { animation-delay: 0.08s; }
      .d2 { animation-delay: 0.18s; }
      .d3 { animation-delay: 0.28s; }
      @keyframes fadeUp { from { transform: translateY(16px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

      @media (max-width: 900px) {
        .feature-list-2col { grid-template-columns: 1fr; }
        .integration-items { grid-template-columns: 1fr; }
        .integration-item { border-right: none; border-bottom: 1px solid var(--border); }
        .integration-item:last-child { border-bottom: none; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page header
st.markdown(
    """
    <div class="page-header fade-up">
      <div class="page-label">Produktdaten</div>
      <h1 class="page-title">HelioTrackX — Technischer Überblick</h1>
      <p class="page-sub">Adaptive Solarzellen-Nachführung für maximale Energieausbeute</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Two-column layout via Streamlit columns
col1, col2 = st.columns([1.1, 0.9], gap="medium")

with col1:
    st.markdown(
        """
        <div class="card fade-up d1">
          <div class="card-label">Systemkern</div>
          <ul class="feature-list">
            <li>Adaptive Lichtsensorik mit kontinuierlicher Messung</li>
            <li>Motorisierte 1-Achsen-Steuerung für präzise Nachführung</li>
            <li>Telemetrie für Monitoring, Diagnose und Reporting</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="metric-card fade-up d1">
          <div class="metric-value">unter 2s</div>
          <div class="metric-label">Reaktionszeit</div>
          <div class="metric-sub">typisch</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Full-width Mehrwert card
st.markdown(
    """
    <div class="card fade-up d2" style="margin-top: 0.85rem;">
      <div class="card-label">Mehrwert im Betrieb</div>
      <ul class="feature-list feature-list-2col">
        <li>Höherer Ertrag bei diffuser Einstrahlung</li>
        <li>Reproduzierbare Betriebsdaten für Optimierung</li>
        <li>Reduktion manueller Wartungsaufwände</li>
        <li>Skalierbar von Pilotanlagen bis Solarpark</li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True,
)

# Integration section
st.markdown(
    """
    <div class="integration-section fade-up d3" style="margin-top: 0.85rem;">
      <div class="integration-header">
        <h2>Integrationspfade</h2>
        <div class="integration-header-line"></div>
      </div>
      <div class="integration-items">
        <div class="integration-item">
          <div class="integration-num">// 01 — Neubau</div>
          <div class="integration-title">Direkte Auslegung</div>
          <div class="integration-desc">Direkte Auslegung auf HelioTrackX-Komponenten für optimale Performance von Anfang an.</div>
        </div><div class="integration-item">
          <div class="integration-num">// 02 — Retrofit</div>
          <div class="integration-title">Nachrüstung</div>
          <div class="integration-desc">Nachrüstung in bestehende Solarstrukturen mit minimalem Aufwand und kurzer Ausfallzeit.</div>
        </div><div class="integration-item">
          <div class="integration-num">// 03 — Hybrid</div>
          <div class="integration-title">Kombination</div>
          <div class="integration-desc">Kombination aus starrer und adaptiver Fläche für maximale Flexibilität im Anlagenkonzept.</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="footer-note">* Die Auslegung erfolgt projektspezifisch je nach Standort und Anlagenkonzept.</p>',
    unsafe_allow_html=True,
)
