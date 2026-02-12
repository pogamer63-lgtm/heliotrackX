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
      @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Space+Grotesk:wght@500;700&display=swap');

      :root {
        --bg-main: #04151d;
        --bg-alt: #0a2733;
        --card: #0f2f3e;
        --card-soft: rgba(10, 39, 51, 0.72);
        --line: rgba(255, 255, 255, 0.12);
        --text: #f4fbff;
        --muted: #b5c9d6;
        --sun: #f7b731;
        --mint: #58d68d;
      }

      .stApp {
        background:
          radial-gradient(circle at 15% 20%, rgba(88, 214, 141, 0.16), transparent 40%),
          radial-gradient(circle at 85% 10%, rgba(247, 183, 49, 0.18), transparent 30%),
          linear-gradient(140deg, var(--bg-main) 0%, var(--bg-alt) 100%);
      }

      .main .block-container {
        max-width: 1160px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
      }

      * {
        box-sizing: border-box;
      }

      .page-shell {
        color: var(--text);
        font-family: "Manrope", sans-serif;
      }

      .hero {
        display: grid;
        grid-template-columns: 1.3fr 1fr;
        gap: 1.4rem;
        align-items: stretch;
        margin-bottom: 1.2rem;
      }

      .panel {
        border: 1px solid var(--line);
        border-radius: 24px;
        background: var(--card-soft);
        backdrop-filter: blur(8px);
        padding: 1.5rem;
      }

      .eyebrow {
        display: inline-block;
        font-size: 0.76rem;
        font-weight: 800;
        letter-spacing: 0.16em;
        color: var(--sun);
        margin-bottom: 0.9rem;
      }

      .headline {
        margin: 0;
        font-family: "Space Grotesk", sans-serif;
        font-weight: 700;
        font-size: clamp(2rem, 4vw, 3.35rem);
        line-height: 1.08;
      }

      .subline {
        margin-top: 1rem;
        margin-bottom: 1.4rem;
        color: var(--muted);
        font-size: 1.05rem;
        line-height: 1.65;
      }

      .cta-row {
        display: flex;
        flex-wrap: wrap;
        gap: 0.8rem;
        align-items: center;
      }

      .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 999px;
        padding: 0.72rem 1.2rem;
        font-weight: 700;
        text-decoration: none;
        transition: transform .2s ease, box-shadow .2s ease;
      }

      .btn:hover {
        transform: translateY(-1px);
      }

      .btn-primary {
        background: linear-gradient(90deg, var(--sun), #ffd878);
        color: #102029;
        box-shadow: 0 8px 24px rgba(247, 183, 49, 0.28);
      }

      .btn-secondary {
        border: 1px solid var(--line);
        background: rgba(255, 255, 255, 0.04);
        color: var(--text);
      }

      .micro {
        margin-top: 1rem;
        color: var(--muted);
        font-size: 0.88rem;
      }

      .brand-box {
        height: 100%;
        display: grid;
        gap: 1.1rem;
        place-items: center;
        text-align: center;
        border-radius: 22px;
        border: 1px solid rgba(255, 255, 255, 0.14);
        background:
          radial-gradient(circle at 50% 0%, rgba(247, 183, 49, 0.15), transparent 55%),
          rgba(7, 24, 31, 0.62);
        padding: 1.4rem;
      }

      .brand-logo {
        width: min(340px, 85%);
        height: auto;
        filter: drop-shadow(0 18px 32px rgba(0, 0, 0, 0.35));
      }

      .brand-fallback {
        font-family: "Space Grotesk", sans-serif;
        letter-spacing: 0.18em;
        font-size: clamp(1.5rem, 3vw, 2.3rem);
        font-weight: 700;
        color: var(--sun);
      }

      .orbit {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 1px dashed rgba(247, 183, 49, 0.65);
        position: relative;
      }

      .orbit::before {
        content: "";
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: var(--sun);
        position: absolute;
        top: -7px;
        left: calc(50% - 7px);
        box-shadow: 0 0 18px rgba(247, 183, 49, 0.6);
        animation: spin 4s linear infinite;
        transform-origin: center 67px;
      }

      @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }

      .brand-text {
        color: var(--muted);
        max-width: 35ch;
        line-height: 1.55;
      }

      .stats {
        margin-top: 1.4rem;
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.85rem;
      }

      .stat {
        border: 1px solid var(--line);
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.03);
        padding: 1rem 1.1rem;
      }

      .stat-kpi {
        font-family: "Space Grotesk", sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--sun);
        margin: 0 0 0.2rem 0;
      }

      .stat-text {
        color: var(--muted);
        font-size: 0.94rem;
        line-height: 1.4;
      }

      .section {
        margin-top: 1.55rem;
      }

      .section-title {
        font-family: "Space Grotesk", sans-serif;
        margin: 0 0 0.85rem 0;
        font-size: clamp(1.4rem, 2.6vw, 2rem);
      }

      .grid-2 {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 0.95rem;
      }

      .feature-card {
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1.1rem;
        background: rgba(255, 255, 255, 0.04);
      }

      .feature-title {
        margin: 0 0 0.4rem 0;
        font-weight: 700;
        color: var(--text);
      }

      .feature-copy {
        margin: 0;
        color: var(--muted);
        line-height: 1.55;
        font-size: 0.95rem;
      }

      .steps {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.85rem;
      }

      .step {
        border: 1px solid var(--line);
        border-radius: 18px;
        padding: 1rem;
        background: rgba(8, 33, 43, 0.6);
      }

      .step-index {
        font-family: "Space Grotesk", sans-serif;
        font-size: 0.82rem;
        letter-spacing: 0.12em;
        color: var(--mint);
        margin-bottom: 0.5rem;
      }

      .step-title {
        margin: 0 0 0.3rem 0;
        font-weight: 700;
      }

      .step-copy {
        margin: 0;
        color: var(--muted);
        line-height: 1.5;
        font-size: 0.92rem;
      }

      .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 0.55rem;
      }

      .chip {
        border: 1px solid rgba(88, 214, 141, 0.35);
        color: #cdf5de;
        border-radius: 999px;
        padding: 0.42rem 0.8rem;
        background: rgba(88, 214, 141, 0.1);
        font-size: 0.85rem;
        font-weight: 600;
      }

      .cta {
        margin-top: 1.5rem;
        border: 1px solid rgba(247, 183, 49, 0.3);
        border-radius: 22px;
        background:
          radial-gradient(circle at 10% 0%, rgba(247, 183, 49, 0.17), transparent 55%),
          rgba(13, 44, 57, 0.72);
        padding: 1.2rem;
      }

      .cta h3 {
        margin: 0 0 0.4rem 0;
        font-family: "Space Grotesk", sans-serif;
      }

      .cta p {
        margin: 0 0 0.95rem 0;
        color: var(--muted);
      }

      .note {
        margin-top: 0.8rem;
        color: var(--muted);
        font-size: 0.78rem;
      }

      .fade-up {
        animation: fadeUp .65s ease both;
      }

      .delay-1 {
        animation-delay: 0.13s;
      }

      @keyframes fadeUp {
        from {
          transform: translateY(10px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }

      @media (max-width: 980px) {
        .hero {
          grid-template-columns: 1fr;
        }
        .stats {
          grid-template-columns: 1fr;
        }
        .grid-2 {
          grid-template-columns: 1fr;
        }
        .steps {
          grid-template-columns: 1fr;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="page-shell">
      <section class="hero">
        <div class="panel fade-up">
          <div class="eyebrow">AUTONOME SOLARTECHNOLOGIE</div>
          <h1 class="headline">HelioTrackX richtet Solarzellen automatisch zum stärksten Licht aus.</h1>
          <p class="subline">
            Die adaptive Nachführung steigert den Energieertrag über den gesamten Tagesverlauf
            und reduziert Leistungsverluste bei wechselnder Einstrahlung.
          </p>
          <div class="cta-row">
            <a class="btn btn-secondary" href="#funktion">Funktionsweise ansehen</a>
          </div>
          <div class="micro">Für Industrie, Gewerbe und dezentrale Energiesysteme.</div>
        </div>
        <div class="panel fade-up delay-1">
          <div class="brand-box">
            {logo_html}
            <div class="orbit"></div>
            <p class="brand-text">
              Sensorik + Motorik + Steuerlogik: Das Modul reagiert in Echtzeit auf Lichtveränderungen.
            </p>
          </div>
        </div>
      </section>

      <section class="stats">
        <div class="stat">
          <p class="stat-kpi">+32%</p>
          <p class="stat-text">Mehr Tagesertrag möglich durch dynamische Lichtausrichtung.</p>
        </div>
        <div class="stat">
          <p class="stat-kpi">24/7</p>
          <p class="stat-text">Automatisierter Betrieb ohne manuelle Nachjustierung.</p>
        </div>
        <div class="stat">
          <p class="stat-kpi">360°</p>
          <p class="stat-text">Kontinuierliche Anpassung an Sonnenstand und Reflexionslicht.</p>
        </div>
      </section>

      <section class="section">
        <h2 class="section-title">Warum HelioTrackX?</h2>
        <div class="grid-2">
          <article class="feature-card">
            <h3 class="feature-title">Hoher Ertrag bei wechselndem Wetter</h3>
            <p class="feature-copy">
              Das System folgt nicht nur dem geometrischen Sonnenpfad, sondern auch den stärksten
              realen Lichtquellen bei Wolken und diffuser Einstrahlung.
            </p>
          </article>
          <article class="feature-card">
            <h3 class="feature-title">Schnelle Integration</h3>
            <p class="feature-copy">
              Die Architektur passt in neue Anlagen und kann als Upgrade in vorhandene Systeme
              integriert werden.
            </p>
          </article>
          <article class="feature-card">
            <h3 class="feature-title">Intelligente Schutzlogik</h3>
            <p class="feature-copy">
              Bei Windspitzen oder technischen Grenzwerten wechselt HelioTrackX automatisch in
              definierte Sicherheitspositionen.
            </p>
          </article>
          <article class="feature-card">
            <h3 class="feature-title">Datentransparenz in Echtzeit</h3>
            <p class="feature-copy">
              Alle Bewegungs- und Leistungsdaten sind für Monitoring, Reporting und Optimierung
              zentral abrufbar.
            </p>
          </article>
        </div>
      </section>

      <section class="section" id="funktion">
        <h2 class="section-title">So funktioniert das System</h2>
        <div class="steps">
          <article class="step">
            <div class="step-index">SCHRITT 01</div>
            <h3 class="step-title">Licht messen</h3>
            <p class="step-copy">Sensoren erfassen Richtung und Intensität der Einstrahlung in kurzen Intervallen.</p>
          </article>
          <article class="step">
            <div class="step-index">SCHRITT 02</div>
            <h3 class="step-title">Ausrichtung berechnen</h3>
            <p class="step-copy">Die Steuerlogik ermittelt den optimalen Winkel für maximalen Energieeintrag.</p>
          </article>
          <article class="step">
            <div class="step-index">SCHRITT 03</div>
            <h3 class="step-title">Modul nachführen</h3>
            <p class="step-copy">Die Motorik richtet das Panel präzise aus und validiert den Effekt in Echtzeit.</p>
          </article>
        </div>
      </section>

      <section class="section">
        <h2 class="section-title">Einsatzbereiche</h2>
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
        <h3>HelioTrackX im praktischen Einsatz</h3>
        <p>
          Ob Neuinstallation oder Nachrüstung: HelioTrackX sorgt für maximale Lichtausnutzung
          und stabile Leistung über den gesamten Tagesverlauf.
        </p>
        <div class="cta-row">
          <span class="chip">Automatische Ausrichtung</span>
          <span class="chip">Sicherheitslogik integriert</span>
          <span class="chip">Skalierbar für jede Anlagengröße</span>
        </div>
        <div class="note">* Potenzialwerte sind standort- und systemabhängig.</div>
      </section>
    </div>
    """,
    unsafe_allow_html=True,
)
