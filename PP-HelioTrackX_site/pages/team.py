from io import BytesIO
from pathlib import Path
import base64
import html

import streamlit as st

try:
    from PIL import Image
except ImportError:
    Image = None


ROOT_DIR = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT_DIR / "assets"
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
IGNORED_FILES = {"logo.png"}

TEAM_LAYOUT = [
    {
        "keys": ["tobias_wurm"],
        "name": "Tobias Wurm",
        "role": "Project Manager",
        "class_name": "node-card--top",
    },
    {
        "keys": ["christoph_panhofer"],
        "name": "Christoph Panhofer",
        "role": "Deputy Project Manager",
        "class_name": "node-card--middle",
    },
    {
        "keys": ["elias_flör", "elias_flor"],
        "name": "Elias Flör",
        "role": "Technical Project Management",
        "class_name": "node-card--bottom",
    },
    {
        "keys": ["moritz_fischböck", "moritz_fischboeck", "moritz_fischbock"],
        "name": "Moritz Fischböck",
        "role": "Requirements Engineer",
        "class_name": "node-card--bottom",
    },
    {
        "keys": ["leon_trautz"],
        "name": "Leon Trautz",
        "role": "Developer",
        "class_name": "node-card--bottom",
    },
]


def normalize_key(value: str) -> str:
    return value.strip().lower().replace("-", "_")


def load_team_images() -> dict[str, Path]:
    image_paths = [
        path
        for path in ASSETS_DIR.iterdir()
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
        and path.name.lower() not in IGNORED_FILES
    ]
    return {normalize_key(path.stem): path for path in image_paths}


def image_to_data_uri(path: Path | None) -> str:
    if path is None or not path.exists():
        return ""

    if Image is None:
        mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
        encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
        return f"data:{mime};base64,{encoded}"

    with Image.open(path) as image:
        image = image.convert("RGB")
        image.thumbnail((200, 200))
        buffer = BytesIO()
        image.save(buffer, format="JPEG", quality=88, optimize=True)

    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"


def find_image_path(image_map: dict[str, Path], keys: list[str]) -> Path | None:
    for key in keys:
        normalized = normalize_key(key)
        if normalized in image_map:
            return image_map[normalized]
    return None


def initials_from_name(name: str) -> str:
    parts = [part for part in name.split(" ") if part]
    return "".join(part[0] for part in parts[:2]).upper()


def build_member_card(member: dict, image_uri: str) -> str:
    member_name = html.escape(member["name"])
    member_role = html.escape(member["role"])
    class_name = member["class_name"]

    if image_uri:
        avatar = f'<img src="{image_uri}" alt="{member_name}" />'
    else:
        initials = initials_from_name(member["name"])
        avatar = f'<div class="avatar-placeholder">{initials}</div>'

    return f"""
      <article class="node-card {class_name}">
        <div class="avatar-wrap">{avatar}</div>
        <h3 class="node-name">{member_name}</h3>
        <p class="node-role">{member_role}</p>
      </article>
    """


team_image_map = load_team_images()
members_with_images = []
for member in TEAM_LAYOUT:
    path = find_image_path(team_image_map, member["keys"])
    members_with_images.append({**member, "image_uri": image_to_data_uri(path)})

top_member = members_with_images[0]
middle_member = members_with_images[1]
bottom_members = members_with_images[2:]

top_card = build_member_card(top_member, top_member["image_uri"])
middle_card = build_member_card(middle_member, middle_member["image_uri"])
bottom_cards = "".join(
    f"""
    <div class="bottom-node">
      <div class="line line-bottom-connector"></div>
      {build_member_card(member, member["image_uri"])}
    </div>
    """
    for member in bottom_members
)

st.markdown(
    """
    <style>
      .tx {
        font-family: 'Figtree', sans-serif;
        color: var(--text);
      }

      /* ── HEADER ───────────────────────── */
      .org-header {
        margin-bottom: 1.8rem;
        padding-bottom: 1.3rem;
        border-bottom: 1px solid var(--border);
      }

      .org-label {
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

      .org-label::before {
        content: '';
        display: inline-block;
        width: 18px;
        height: 2px;
        background: var(--gold);
        flex-shrink: 0;
      }

      .org-title {
        margin: 0 0 0.3rem 0;
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: clamp(1.8rem, 3.5vw, 2.7rem);
        letter-spacing: -0.01em;
      }

      .org-subtitle {
        margin: 0;
        color: var(--muted);
        font-size: 0.97rem;
      }

      /* ── ORG CHART ────────────────────── */
      .org-chart {
        width: min(960px, 100%);
        margin: 0 auto;
      }

      .row-center {
        display: flex;
        justify-content: center;
      }

      .line {
        margin: 0 auto;
        background: rgba(245,158,11,0.3);
      }

      .line-vertical-top    { width: 2px; height: 44px; }
      .line-vertical-branch { width: 2px; height: 22px; }
      .line-horizontal      { width: min(72%, 740px); height: 2px; }
      .line-bottom-connector { width: 2px; height: 26px; }

      .row-bottom {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1rem;
        margin-top: 0;
      }

      .bottom-node {
        display: flex;
        flex-direction: column;
        align-items: center;
      }

      /* ── NODE CARDS ───────────────────── */
      .node-card {
        border: 1px solid var(--border);
        border-radius: 18px;
        background: rgba(7,31,43,0.65);
        backdrop-filter: blur(10px);
        text-align: center;
        padding: 1rem 1rem 1.1rem;
        box-shadow: 0 16px 32px rgba(0,0,0,0.25);
        position: relative;
        overflow: hidden;
        transition: border-color 0.25s, box-shadow 0.25s;
      }

      .node-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--gold), transparent);
        opacity: 0;
        transition: opacity 0.25s;
      }

      .node-card:hover {
        border-color: rgba(245,158,11,0.3);
        box-shadow: 0 20px 40px rgba(0,0,0,0.35), 0 0 0 1px rgba(245,158,11,0.1);
      }

      .node-card:hover::before { opacity: 1; }

      .node-card--top    { width: 240px; }
      .node-card--middle { width: 290px; }
      .node-card--bottom { width: 100%; }

      /* ── AVATARS ──────────────────────── */
      .avatar-wrap {
        display: flex;
        justify-content: center;
        margin-bottom: 0.65rem;
      }

      .avatar-wrap img,
      .avatar-placeholder {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        border: 2px solid rgba(245,158,11,0.35);
        object-fit: cover;
        background: rgba(245,158,11,0.08);
      }

      .avatar-placeholder {
        display: grid;
        place-items: center;
        font-weight: 700;
        font-size: 1rem;
        color: var(--gold);
        font-family: 'Space Mono', monospace;
      }

      .node-name {
        margin: 0;
        font-family: 'Archivo Black', sans-serif;
        font-weight: 400;
        font-size: 1rem;
        line-height: 1.2;
        color: var(--text);
        letter-spacing: -0.01em;
      }

      .node-role {
        margin: 0.2rem 0 0 0;
        color: var(--muted);
        font-size: 0.84rem;
        line-height: 1.3;
        font-family: 'Space Mono', monospace;
      }

      /* ── ANIMATIONS ───────────────────── */
      .fade-up { animation: fadeUp 0.75s cubic-bezier(0.22,1,0.36,1) both; }
      .d1 { animation-delay: 0.08s; }
      .d2 { animation-delay: 0.18s; }

      @keyframes fadeUp {
        from { transform: translateY(16px); opacity: 0; }
        to   { transform: translateY(0);    opacity: 1; }
      }

      /* ── RESPONSIVE ───────────────────── */
      @media (max-width: 900px) {
        .line-horizontal      { display: none; }
        .line-vertical-branch { height: 18px; }
        .line-bottom-connector { display: none; }
        .row-bottom {
          grid-template-columns: 1fr;
          max-width: 300px;
          margin: 0 auto;
          gap: 0.85rem;
        }
        .node-card--top,
        .node-card--middle { width: min(300px, 100%); }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="tx">
      <div class="org-header fade-up">
        <div class="org-label">Organisation</div>
        <h1 class="org-title">Unser Team</h1>
        <p class="org-subtitle">Die Teamstruktur von HelioTrackX im Überblick.</p>
      </div>

      <div class="org-chart fade-up d1">
        <div class="row-center">{top_card}</div>
        <div class="line line-vertical-top"></div>
        <div class="row-center">{middle_card}</div>
        <div class="line line-vertical-branch"></div>
        <div class="line line-horizontal"></div>
        <div class="row-bottom">{bottom_cards}</div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
