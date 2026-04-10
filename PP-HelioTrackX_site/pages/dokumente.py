from pathlib import Path
import datetime

import streamlit as st

try:
    import mammoth
    MAMMOTH_AVAILABLE = True
except ImportError:
    MAMMOTH_AVAILABLE = False

ROOT_DIR = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT_DIR / "documents"
DOCS_DIR.mkdir(exist_ok=True)

if "selected_doc" not in st.session_state:
    st.session_state["selected_doc"] = None


def format_size(bytes_: int) -> str:
    if bytes_ < 1024:
        return f"{bytes_} B"
    elif bytes_ < 1024 ** 2:
        return f"{bytes_ / 1024:.1f} KB"
    return f"{bytes_ / 1024 ** 2:.1f} MB"


def load_documents() -> list[Path]:
    return sorted(DOCS_DIR.glob("*.docx"), key=lambda p: p.name.lower())


def convert_to_html(path: Path) -> str:
    if not MAMMOTH_AVAILABLE:
        return "<p>mammoth ist nicht installiert. Bitte <code>pip install mammoth</code> ausführen.</p>"
    with open(path, "rb") as f:
        result = mammoth.convert_to_html(f)
    return result.value


def build_viewer_html(body: str, filename: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; }}
  body {{
    background: #071F2B;
    color: #B0CDD8;
    font-family: 'Figtree', sans-serif;
    font-size: 0.97rem;
    line-height: 1.75;
    padding: 1.6rem 2rem 2.5rem;
    margin: 0;
  }}
  .doc-filename {{
    font-family: 'Space Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.16em;
    color: #F59E0B;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}
  .doc-filename::before {{
    content: '';
    display: inline-block;
    width: 16px;
    height: 2px;
    background: #F59E0B;
    flex-shrink: 0;
  }}
  h1, h2, h3, h4, h5, h6 {{
    font-family: 'Archivo Black', sans-serif;
    font-weight: 400;
    color: #EDF6FA;
    line-height: 1.2;
    margin-top: 1.6rem;
    margin-bottom: 0.5rem;
  }}
  h1 {{ font-size: 1.55rem; }}
  h2 {{ font-size: 1.25rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 0.4rem; }}
  h3 {{ font-size: 1.05rem; }}
  h4 {{ font-size: 0.97rem; color: #F59E0B; }}
  p {{ margin: 0.55rem 0; }}
  strong, b {{ color: #EDF6FA; font-weight: 700; }}
  em, i {{ color: #C8DDE5; }}
  a {{ color: #F59E0B; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 1.2rem 0;
    font-size: 0.92rem;
  }}
  th, td {{
    border: 1px solid rgba(255,255,255,0.1);
    padding: 0.55rem 0.85rem;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: rgba(245,158,11,0.12);
    color: #F59E0B;
    font-family: 'Archivo Black', sans-serif;
    font-weight: 400;
    font-size: 0.85rem;
    letter-spacing: 0.03em;
  }}
  tr:nth-child(even) td {{ background: rgba(255,255,255,0.02); }}
  ul, ol {{
    padding-left: 1.5rem;
    margin: 0.6rem 0;
    color: #B0CDD8;
  }}
  li {{ margin: 0.3rem 0; }}
  blockquote {{
    border-left: 3px solid #F59E0B;
    margin: 1rem 0;
    padding: 0.5rem 1rem;
    background: rgba(245,158,11,0.05);
    color: #7FA8BC;
    font-style: italic;
  }}
  hr {{
    border: none;
    border-top: 1px solid rgba(255,255,255,0.1);
    margin: 1.8rem 0;
  }}
  code {{
    font-family: 'Space Mono', monospace;
    font-size: 0.85em;
    background: rgba(255,255,255,0.06);
    padding: 0.15em 0.4em;
    border-radius: 4px;
    color: #34D399;
  }}
  img {{ max-width: 100%; border-radius: 8px; }}
</style>
</head>
<body>
<div class="doc-filename">{filename}</div>
{body}
</body>
</html>"""


# ── CSS ──────────────────────────────────────────────────────
st.markdown(
    """
    <style>
      .dk { font-family: 'Figtree', sans-serif; color: var(--text); }

      .page-header { margin-bottom: 1.6rem; padding-bottom: 1.2rem; border-bottom: 1px solid var(--border); }
      .page-label {
        display: inline-flex; align-items: center; gap: 0.55rem;
        font-family: 'Space Mono', monospace; font-size: 0.7rem;
        letter-spacing: 0.2em; color: var(--gold); text-transform: uppercase; margin-bottom: 0.55rem;
      }
      .page-label::before { content: ''; display: inline-block; width: 18px; height: 2px; background: var(--gold); flex-shrink: 0; }
      .page-title { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: clamp(1.8rem, 3.5vw, 2.7rem); margin: 0 0 0.3rem 0; letter-spacing: -0.01em; }
      .page-sub { color: var(--muted); font-size: 0.97rem; margin: 0; }

      .file-list-header {
        font-family: 'Space Mono', monospace; font-size: 0.68rem;
        letter-spacing: 0.16em; color: var(--dim); text-transform: uppercase;
        margin-bottom: 0.7rem;
      }

      .empty-state {
        border: 1px dashed rgba(245,158,11,0.25); border-radius: 16px;
        padding: 2rem 1.5rem; text-align: center;
        background: rgba(245,158,11,0.03);
      }
      .empty-state-icon { font-size: 2rem; margin-bottom: 0.6rem; }
      .empty-state-title { font-family: 'Archivo Black', sans-serif; font-weight: 400; font-size: 1.05rem; margin: 0 0 0.4rem; }
      .empty-state-text { color: var(--muted); font-size: 0.88rem; line-height: 1.6; margin: 0; }
      .empty-state-code { font-family: 'Space Mono', monospace; font-size: 0.78rem; color: var(--gold); background: rgba(245,158,11,0.08); border-radius: 6px; padding: 0.3rem 0.6rem; display: inline-block; margin-top: 0.6rem; }

      .viewer-placeholder {
        border: 1px solid var(--border); border-radius: 16px;
        padding: 3rem 2rem; text-align: center;
        background: rgba(7,31,43,0.4); color: var(--dim);
        font-size: 0.9rem; line-height: 1.6;
      }
      .viewer-placeholder-icon { font-size: 2.5rem; margin-bottom: 0.8rem; opacity: 0.5; }

      .fade-up { animation: fadeUp 0.6s cubic-bezier(0.22,1,0.36,1) both; }
      @keyframes fadeUp { from { transform: translateY(14px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

      /* Override Streamlit button defaults for file entries */
      div[data-testid="stButton"] button {
        background: rgba(7,31,43,0.5) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        color: var(--text) !important;
        font-family: 'Figtree', sans-serif !important;
        text-align: left !important;
        width: 100% !important;
        padding: 0.7rem 0.9rem !important;
        transition: border-color 0.2s, background 0.2s !important;
      }
      div[data-testid="stButton"] button:hover {
        border-color: rgba(245,158,11,0.4) !important;
        background: rgba(10,40,55,0.7) !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── PAGE HEADER ───────────────────────────────────────────────
st.markdown(
    """
    <div class="page-header fade-up">
      <div class="page-label">Dokumentation</div>
      <h1 class="page-title">Dokumente</h1>
      <p class="page-sub">Interne Dokumente & Berichte — direkt im Browser lesbar</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── LOAD FILES ────────────────────────────────────────────────
docs = load_documents()

if not docs:
    st.markdown(
        """
        <div class="empty-state fade-up">
          <div class="empty-state-icon">📁</div>
          <p class="empty-state-title">Noch keine Dokumente vorhanden</p>
          <p class="empty-state-text">Lege <strong>.docx</strong>-Dateien in den folgenden Ordner,<br>damit sie hier automatisch erscheinen:</p>
          <span class="empty-state-code">documents/</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    col_list, col_view = st.columns([1, 2.5], gap="medium")

    with col_list:
        st.markdown('<div class="file-list-header">Dateien</div>', unsafe_allow_html=True)
        for doc_path in docs:
            stat = doc_path.stat()
            size_str = format_size(stat.st_size)
            modified = datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%d.%m.%Y")
            label = f"📄  {doc_path.stem}\n{size_str} · {modified}"
            if st.button(label, key=str(doc_path)):
                st.session_state["selected_doc"] = str(doc_path)
                st.rerun()

    with col_view:
        selected = st.session_state.get("selected_doc")
        if selected is None:
            st.markdown(
                """
                <div class="viewer-placeholder fade-up">
                  <div class="viewer-placeholder-icon">📄</div>
                  Wähle links ein Dokument aus,<br>um es hier anzuzeigen.
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            selected_path = Path(selected)
            if not selected_path.exists():
                st.error("Datei nicht gefunden.")
                st.session_state["selected_doc"] = None
            else:
                html_body = convert_to_html(selected_path)
                viewer_html = build_viewer_html(html_body, selected_path.stem)
                st.components.v1.html(viewer_html, height=720, scrolling=True)
