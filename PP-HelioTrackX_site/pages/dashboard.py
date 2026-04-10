import streamlit as st


DASHBOARD_URL = (
    "http://192.168.1.2:3000/d/ad7jndw/solarpanel-timeseries"
    "?orgId=1&from=now-6h&to=now&timezone=browser&refresh=5s&kiosk"
)
DASHBOARD_URL_HTML = DASHBOARD_URL.replace("&", "&amp;")

st.markdown(
    """
    <style>
      .dx {
        font-family: 'Figtree', sans-serif;
        color: var(--text);
      }

      /* ── HEADER ───────────────────────── */
      .dash-header {
        margin-bottom: 2rem;
        padding-bottom: 1.3rem;
        border-bottom: 1px solid var(--border);
      }

      .dash-label {
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.2em;
        color: var(--gold);
        text-transform: uppercase;
        margin-bottom: 0.55rem;
      }

      .dash-label::before {
        content: '';
        display: inline-block;
        width: 18px;
        height: 2px;
        background: var(--gold);
        flex-shrink: 0;
      }

      .dash-title {
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: clamp(1.8rem, 3.5vw, 2.7rem);
        margin: 0 0 0.3rem 0;
        letter-spacing: -0.01em;
      }

      .dash-sub {
        color: var(--muted);
        font-size: 0.97rem;
        margin: 0;
      }

      /* ── LAUNCH CARD ──────────────────── */
      .launch-card {
        border: 1px solid var(--border-g);
        border-radius: 22px;
        background: linear-gradient(
          135deg,
          rgba(245,158,11,0.1) 0%,
          rgba(7,31,43,0.8) 60%
        );
        padding: 2.4rem 2rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        gap: 1.4rem;
        position: relative;
        overflow: hidden;
      }

      .launch-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent 5%, var(--gold) 50%, transparent 95%);
      }

      .launch-icon {
        width: 64px;
        height: 64px;
        border-radius: 16px;
        border: 1px solid var(--border-g);
        background: rgba(245,158,11,0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.7rem;
      }

      .launch-heading {
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: 1.4rem;
        margin: 0;
        letter-spacing: -0.01em;
      }

      .launch-desc {
        color: var(--muted);
        font-size: 0.94rem;
        line-height: 1.65;
        max-width: 46ch;
        margin: 0;
      }

      .launch-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        border-radius: 10px;
        padding: 0.8rem 1.6rem;
        font-family: 'Figtree', sans-serif;
        font-size: 0.92rem;
        font-weight: 700;
        text-decoration: none;
        letter-spacing: 0.01em;
        background: linear-gradient(90deg, var(--gold), var(--gold-bright));
        color: #0D1F10;
        box-shadow: 0 8px 28px rgba(245,158,11,0.3);
        transition: box-shadow 0.25s, transform 0.2s;
      }

      .launch-btn:hover {
        box-shadow: 0 12px 36px rgba(245,158,11,0.45);
        transform: translateY(-2px);
        color: #0D1F10;
      }

      /* ── INFO STRIP ───────────────────── */
      .info-strip {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        border: 1px solid var(--border);
        border-radius: 16px;
        background: rgba(7,31,43,0.4);
        overflow: hidden;
        margin-top: 1rem;
      }

      .info-item {
        padding: 1rem 1.2rem;
        border-right: 1px solid var(--border);
      }

      .info-item:last-child { border-right: none; }

      .info-key {
        font-family: 'Space Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 0.14em;
        color: var(--dim);
        text-transform: uppercase;
        margin-bottom: 0.3rem;
      }

      .info-val {
        font-family: 'Space Mono', monospace;
        font-size: 0.88rem;
        color: var(--emerald);
        font-weight: 700;
      }

      /* ── ANIMATIONS ───────────────────── */
      .fade-up { animation: fadeUp 0.75s cubic-bezier(0.22,1,0.36,1) both; }
      .d1 { animation-delay: 0.1s; }
      .d2 { animation-delay: 0.22s; }

      @keyframes fadeUp {
        from { transform: translateY(16px); opacity: 0; }
        to   { transform: translateY(0);    opacity: 1; }
      }

      @media (max-width: 700px) {
        .info-strip { grid-template-columns: 1fr; }
        .info-item  { border-right: none; border-bottom: 1px solid var(--border); }
        .info-item:last-child { border-bottom: none; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="dx">
      <div class="dash-header fade-up">
        <div class="dash-label">Live-Monitoring</div>
        <h1 class="dash-title">Solarpanel Timeseries Dashboard</h1>
        <p class="dash-sub">Echtzeit-Daten aus dem laufenden Betrieb — gehostet auf Grafana</p>
      </div>

      <div class="launch-card fade-up d1">
        <div class="launch-icon">⚡</div>
        <h2 class="launch-heading">Grafana-Dashboard öffnen</h2>
        <p class="launch-desc">
          Das interaktive Dashboard zeigt Leistungsdaten, Ausrichtungsverläufe und
          Systemtelemetrie der letzten 6 Stunden in Echtzeit.
        </p>
        <a class="launch-btn" href="{DASHBOARD_URL_HTML}" target="_blank" rel="noopener noreferrer">
          Dashboard öffnen &nbsp;↗
        </a>
      </div>

      <div class="info-strip fade-up d2">
        <div class="info-item">
          <div class="info-key">Zeitraum</div>
          <div class="info-val">Letzte 6 Stunden</div>
        </div>
        <div class="info-item">
          <div class="info-key">Aktualisierung</div>
          <div class="info-val">Alle 5 Sekunden</div>
        </div>
        <div class="info-item">
          <div class="info-key">Quelle</div>
          <div class="info-val">Grafana @ 192.168.1.2</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
