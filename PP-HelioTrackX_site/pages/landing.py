from pathlib import Path
import base64

import streamlit as st


ROOT_DIR = Path(__file__).resolve().parents[1]
LOGO_PATH = ROOT_DIR / "assets" / "Logo.png"


def image_to_base64(path: Path) -> str:
    if not path.exists():
        return ""
    return base64.b64encode(path.read_bytes()).decode("utf-8")


logo_base64 = image_to_base64(LOGO_PATH)
logo_html = (
    f'<img class="brand-logo" src="data:image/png;base64,{logo_base64}" alt="HelioTrackX Logo" />'
    if logo_base64
    else '<div class="brand-fallback">HELIOTRACKX</div>'
)

st.markdown(
    """
    <style>
      /* ── BASE ──────────────────────────── */
      .lx {
        font-family: 'Figtree', sans-serif;
        color: var(--text);
      }

      /* ── HERO ──────────────────────────── */
      .hero {
        display: grid;
        grid-template-columns: 1.4fr 1fr;
        gap: 1.1rem;
        align-items: stretch;
        margin-bottom: 0.9rem;
      }

      .panel {
        border: 1px solid var(--border);
        border-radius: 20px;
        background: rgba(7,31,43,0.65);
        backdrop-filter: blur(14px);
        padding: 1.7rem;
        position: relative;
        overflow: hidden;
      }

      .panel::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(245,158,11,0.05) 0%, transparent 55%);
        border-radius: inherit;
        pointer-events: none;
      }

      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 0.55rem;
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        color: var(--gold);
        margin-bottom: 1.2rem;
        text-transform: uppercase;
      }

      .eyebrow::before {
        content: '';
        display: inline-block;
        width: 20px;
        height: 2px;
        background: var(--gold);
        flex-shrink: 0;
      }

      .headline {
        margin: 0;
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: clamp(2rem, 4.2vw, 3.4rem);
        line-height: 1.07;
        letter-spacing: -0.01em;
        color: var(--text);
      }

      .headline em {
        font-style: normal;
        color: var(--gold);
      }

      .subline {
        margin: 1.1rem 0 1.7rem;
        color: var(--muted);
        font-size: 1.03rem;
        line-height: 1.72;
        max-width: 50ch;
      }

      .cta-row {
        display: flex;
        gap: 0.75rem;
        align-items: center;
        flex-wrap: wrap;
      }

      .btn {
        display: inline-flex;
        align-items: center;
        border-radius: 8px;
        padding: 0.68rem 1.2rem;
        font-family: 'Figtree', sans-serif;
        font-size: 0.88rem;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.2s ease;
        letter-spacing: 0.01em;
      }

      .btn-secondary {
        border: 1px solid var(--border-g);
        background: var(--gold-dim);
        color: var(--gold);
      }

      .btn-secondary:hover {
        background: rgba(245,158,11,0.22);
        border-color: var(--gold);
        color: var(--gold-bright);
      }

      .micro {
        margin-top: 1.1rem;
        color: var(--dim);
        font-size: 0.78rem;
        font-family: 'Space Mono', monospace;
      }

      /* ── BRAND PANEL ──────────────────── */
      .brand-panel {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        gap: 1.1rem;
        height: 100%;
      }

      .brand-orbit-wrap {
        position: relative;
        width: 220px;
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .brand-logo {
        width: 160px;
        height: 160px;
        object-fit: contain;
        position: relative;
        z-index: 2;
        filter: drop-shadow(0 0 28px rgba(245,158,11,0.5));
      }

      .brand-fallback {
        font-family: 'Archivo Black', sans-serif;
        font-size: 1.3rem;
        color: var(--gold);
        position: relative;
        z-index: 2;
      }

      .pulse-ring {
        position: absolute;
        border-radius: 50%;
        border: 1.5px solid var(--gold);
        width: 60px;
        height: 60px;
        top: calc(50% - 30px);
        left: calc(50% - 30px);
        transform-origin: center;
        animation: pulse-expand 3s ease-out infinite;
      }

      .pulse-ring:nth-child(2) { animation-delay: 1s; }
      .pulse-ring:nth-child(3) { animation-delay: 2s; }

      @keyframes pulse-expand {
        0%   { transform: scale(0.8); opacity: 0.7; }
        100% { transform: scale(3);   opacity: 0;   }
      }

      .brand-text {
        color: var(--muted);
        font-size: 0.9rem;
        line-height: 1.62;
        max-width: 28ch;
      }

      /* ── STATS BAR ────────────────────── */
      .stats-bar {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        border: 1px solid var(--border);
        border-radius: 16px;
        background: rgba(7,31,43,0.5);
        overflow: hidden;
        margin-bottom: 1.6rem;
      }

      .stat {
        padding: 1.3rem 1.5rem;
        border-right: 1px solid var(--border);
      }

      .stat:last-child { border-right: none; }

      .stat-kpi {
        font-family: 'Space Mono', monospace;
        font-size: 2.1rem;
        font-weight: 700;
        color: var(--gold);
        margin: 0 0 0.3rem 0;
        letter-spacing: -0.02em;
        line-height: 1;
      }

      .stat-text {
        color: var(--muted);
        font-size: 0.87rem;
        line-height: 1.45;
        margin: 0;
      }

      /* ── SECTIONS ─────────────────────── */
      .section { margin-top: 2rem; }

      .section-header {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        margin-bottom: 1.1rem;
      }

      .section-title {
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: clamp(1.25rem, 2.4vw, 1.75rem);
        margin: 0;
        letter-spacing: -0.01em;
        white-space: nowrap;
      }

      .section-line {
        flex: 1;
        height: 1px;
        background: linear-gradient(to right, var(--border-g), transparent);
      }

      /* ── FEATURE CARDS ────────────────── */
      .grid-2 {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.85rem;
      }

      .feature-card {
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.2rem 1.35rem;
        background: rgba(7,31,43,0.5);
        position: relative;
        transition: border-color 0.25s, background 0.25s;
      }

      .feature-card::before,
      .feature-card::after {
        content: '';
        position: absolute;
        width: 10px;
        height: 10px;
        border-color: var(--gold);
        border-style: solid;
        opacity: 0;
        transition: opacity 0.25s;
      }

      .feature-card::before {
        top: -1px; left: -1px;
        border-width: 2px 0 0 2px;
        border-radius: 2px 0 0 0;
      }

      .feature-card::after {
        bottom: -1px; right: -1px;
        border-width: 0 2px 2px 0;
        border-radius: 0 0 2px 0;
      }

      .feature-card:hover {
        border-color: rgba(245,158,11,0.3);
        background: rgba(10,40,55,0.7);
      }

      .feature-card:hover::before,
      .feature-card:hover::after { opacity: 1; }

      .feature-title {
        margin: 0 0 0.4rem 0;
        font-weight: 700;
        font-size: 0.95rem;
        color: var(--text);
      }

      .feature-copy {
        margin: 0;
        color: var(--muted);
        line-height: 1.62;
        font-size: 0.88rem;
      }

      /* ── STEPS ────────────────────────── */
      .steps {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.85rem;
      }

      .step {
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.1rem 1.2rem;
        background: rgba(7,31,43,0.5);
        position: relative;
        transition: border-color 0.25s;
      }

      .step:hover { border-color: rgba(52,211,153,0.3); }

      .step-index {
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        letter-spacing: 0.14em;
        color: var(--emerald);
        margin-bottom: 0.55rem;
        text-transform: uppercase;
      }

      .step-title {
        margin: 0 0 0.35rem 0;
        font-weight: 700;
        font-size: 0.95rem;
        color: var(--text);
      }

      .step-copy {
        margin: 0;
        color: var(--muted);
        line-height: 1.58;
        font-size: 0.87rem;
      }

      /* ── CHIPS ────────────────────────── */
      .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
      }

      .chip {
        border: 1px solid rgba(52,211,153,0.28);
        color: #A7F3D0;
        border-radius: 6px;
        padding: 0.36rem 0.72rem;
        background: rgba(52,211,153,0.07);
        font-size: 0.82rem;
        font-weight: 500;
        font-family: 'Space Mono', monospace;
      }

      /* ── CTA BANNER ───────────────────── */
      .cta {
        margin-top: 2rem;
        border: 1px solid var(--border-g);
        border-radius: 20px;
        background: linear-gradient(
          135deg,
          rgba(245,158,11,0.1) 0%,
          rgba(7,31,43,0.75) 55%
        );
        padding: 1.6rem 1.8rem;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1.5rem;
        flex-wrap: wrap;
      }

      .cta-text h3 {
        margin: 0 0 0.35rem 0;
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: 1.25rem;
      }

      .cta-text p {
        margin: 0;
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.58;
        max-width: 54ch;
      }

      .cta-chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
      }

      .note {
        margin-top: 0.75rem;
        color: var(--dim);
        font-size: 0.74rem;
        font-family: 'Space Mono', monospace;
      }

      /* ── ANIMATIONS ───────────────────── */
      .fade-up { animation: fadeUp 0.75s cubic-bezier(0.22,1,0.36,1) both; }
      .d1 { animation-delay: 0.08s; }
      .d2 { animation-delay: 0.18s; }
      .d3 { animation-delay: 0.30s; }

      @keyframes fadeUp {
        from { transform: translateY(18px); opacity: 0; }
        to   { transform: translateY(0);    opacity: 1; }
      }

      /* ── RESPONSIVE ───────────────────── */
      @media (max-width: 900px) {
        .hero        { grid-template-columns: 1fr; }
        .stats-bar   { grid-template-columns: 1fr; }
        .stat        { border-right: none; border-bottom: 1px solid var(--border); }
        .stat:last-child { border-bottom: none; }
        .grid-2      { grid-template-columns: 1fr; }
        .steps       { grid-template-columns: 1fr; }
        .cta         { flex-direction: column; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="lx">
      <section class="hero">
        <div class="panel fade-up">
          <div class="eyebrow">Autonome Solartechnologie</div>
          <h1 class="headline">HelioTrackX richtet Solarzellen automatisch zum <em>stärksten Licht</em> aus.</h1>
          <p class="subline">
            Die adaptive Nachführung steigert den Energieertrag über den gesamten Tagesverlauf
            und reduziert Leistungsverluste bei wechselnder Einstrahlung.
          </p>
          <div class="cta-row">
            <a class="btn btn-secondary" href="#funktion">Funktionsweise ansehen →</a>
          </div>
          <p class="micro">// Für Industrie, Gewerbe und dezentrale Energiesysteme</p>
        </div>
        <div class="panel fade-up d1">
          <div class="brand-panel">
            <div class="brand-orbit-wrap">
              <div class="pulse-ring"></div>
              <div class="pulse-ring"></div>
              <div class="pulse-ring"></div>
              {logo_html}
            </div>
            <p class="brand-text">
              Sensorik + Motorik + Steuerlogik: Das Modul reagiert in Echtzeit auf Lichtveränderungen.
            </p>
          </div>
        </div>
      </section>

      <div class="stats-bar fade-up d2">
        <div class="stat">
          <p class="stat-kpi">+32%</p>
          <p class="stat-text">Mehr Tagesertrag durch dynamische Lichtausrichtung</p>
        </div>
        <div class="stat">
          <p class="stat-kpi">24/7</p>
          <p class="stat-text">Automatisierter Betrieb ohne manuelle Nachjustierung</p>
        </div>
        <div class="stat">
          <p class="stat-kpi">360°</p>
          <p class="stat-text">Kontinuierliche Anpassung an Sonnenstand und Reflexionslicht</p>
        </div>
      </div>

      <section class="section fade-up d3">
        <div class="section-header">
          <h2 class="section-title">Warum HelioTrackX?</h2>
          <div class="section-line"></div>
        </div>
        <div class="grid-2">
          <article class="feature-card">
            <h3 class="feature-title">Hoher Ertrag bei wechselndem Wetter</h3>
            <p class="feature-copy">Das System folgt nicht nur dem geometrischen Sonnenpfad, sondern auch den stärksten realen Lichtquellen bei Wolken und diffuser Einstrahlung.</p>
          </article>
          <article class="feature-card">
            <h3 class="feature-title">Schnelle Integration</h3>
            <p class="feature-copy">Die Architektur passt in neue Anlagen und kann als Upgrade in vorhandene Systeme integriert werden.</p>
          </article>
          <article class="feature-card">
            <h3 class="feature-title">Intelligente Schutzlogik</h3>
            <p class="feature-copy">Bei Windspitzen oder technischen Grenzwerten wechselt HelioTrackX automatisch in definierte Sicherheitspositionen.</p>
          </article>
          <article class="feature-card">
            <h3 class="feature-title">Datentransparenz in Echtzeit</h3>
            <p class="feature-copy">Alle Bewegungs- und Leistungsdaten sind für Monitoring, Reporting und Optimierung zentral abrufbar.</p>
          </article>
        </div>
      </section>

      <section class="section" id="funktion">
        <div class="section-header">
          <h2 class="section-title">So funktioniert das System</h2>
          <div class="section-line"></div>
        </div>
        <div class="steps">
          <article class="step">
            <div class="step-index">// Schritt 01</div>
            <h3 class="step-title">Licht messen</h3>
            <p class="step-copy">Lichtsensoren erfassen Richtung und Intensität der Einstrahlung in kurzen Intervallen.</p>
          </article>
          <article class="step">
            <div class="step-index">// Schritt 02</div>
            <h3 class="step-title">Ausrichtung berechnen</h3>
            <p class="step-copy">Die Steuerlogik ermittelt den optimalen Winkel für maximalen Energieeintrag.</p>
          </article>
          <article class="step">
            <div class="step-index">// Schritt 03</div>
            <h3 class="step-title">Modul nachführen</h3>
            <p class="step-copy">Die Motorik richtet das Panel präzise aus und validiert den Effekt in Echtzeit.</p>
          </article>
        </div>
      </section>

      <section class="section">
        <div class="section-header">
          <h2 class="section-title">Einsatzbereiche</h2>
          <div class="section-line"></div>
        </div>
        <div class="chips">
          <span class="chip">Solarparks</span>
          <span class="chip">Dachflächen Gewerbe</span>
          <span class="chip">Inselnetze</span>
          <span class="chip">Smart-City-Infrastruktur</span>
          <span class="chip">Agrivoltaik</span>
          <span class="chip">Ladeinfrastruktur</span>
        </div>
      </section>

      <section class="cta">
        <div class="cta-text">
          <h3>HelioTrackX im praktischen Einsatz</h3>
          <p>Ob Neuinstallation oder Nachrüstung: HelioTrackX sorgt für maximale Lichtausnutzung und stabile Leistung über den gesamten Tagesverlauf.</p>
          <p class="note">* Potenzialwerte sind standort- und systemabhängig.</p>
        </div>
        <div class="cta-chips">
          <span class="chip">Automatische Ausrichtung</span>
          <span class="chip">Sicherheitslogik integriert</span>
          <span class="chip">Skalierbar</span>
        </div>
      </section>
    </div>
    """,
    unsafe_allow_html=True,
)
