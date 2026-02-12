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
        avatar = f'<div class="avatar-placeholder">{initials_from_name(member["name"])}</div>'

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
      @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Space+Grotesk:wght@500;700&display=swap');

      :root {
        --bg-main: #04151d;
        --bg-alt: #0a2733;
        --card-soft: rgba(10, 39, 51, 0.72);
        --line: rgba(255, 255, 255, 0.12);
        --line-strong: rgba(255, 255, 255, 0.22);
        --text: #f4fbff;
        --muted: #b5c9d6;
        --sun: #f7b731;
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

      .org-shell {
        font-family: "Manrope", sans-serif;
        color: var(--text);
      }

      .org-title {
        margin: 0 0 0.35rem 0;
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(1.9rem, 4vw, 2.9rem);
        font-weight: 700;
      }

      .org-subtitle {
        margin: 0 0 1.35rem 0;
        color: var(--muted);
        font-size: 1.03rem;
      }

      .org-chart {
        width: min(950px, 100%);
        margin: 0 auto;
      }

      .row-center {
        display: flex;
        justify-content: center;
      }

      .line {
        margin: 0 auto;
        background: var(--line-strong);
      }

      .line-vertical-top {
        width: 2px;
        height: 46px;
      }

      .line-vertical-branch {
        width: 2px;
        height: 24px;
      }

      .line-horizontal {
        width: min(74%, 760px);
        height: 2px;
      }

      .line-bottom-connector {
        width: 2px;
        height: 28px;
      }

      .row-bottom {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 1.2rem;
        margin-top: 0;
      }

      .bottom-node {
        display: flex;
        flex-direction: column;
        align-items: center;
      }

      .node-card {
        border: 1px solid var(--line);
        border-radius: 18px;
        background: var(--card-soft);
        backdrop-filter: blur(6px);
        text-align: center;
        padding: 0.9rem 0.9rem 1rem 0.9rem;
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
      }

      .node-card--top {
        width: 250px;
      }

      .node-card--middle {
        width: 300px;
      }

      .node-card--bottom {
        width: 100%;
      }

      .avatar-wrap {
        display: flex;
        justify-content: center;
        margin-bottom: 0.55rem;
      }

      .avatar-wrap img,
      .avatar-placeholder {
        width: 84px;
        height: 84px;
        border-radius: 50%;
        border: 2px solid rgba(255, 255, 255, 0.24);
        object-fit: cover;
        background: rgba(255, 255, 255, 0.08);
      }

      .avatar-placeholder {
        display: grid;
        place-items: center;
        font-weight: 700;
        font-size: 1.05rem;
        color: var(--text);
      }

      .node-name {
        margin: 0;
        font-size: 1.18rem;
        font-weight: 800;
        line-height: 1.15;
        color: var(--text);
      }

      .node-role {
        margin: 0.15rem 0 0 0;
        color: var(--muted);
        font-size: 0.98rem;
        line-height: 1.2;
      }

      @media (max-width: 980px) {
        .line-horizontal {
          display: none;
        }

        .line-vertical-branch {
          height: 20px;
        }

        .line-bottom-connector {
          display: none;
        }

        .row-bottom {
          grid-template-columns: 1fr;
          max-width: 320px;
          margin: 0 auto;
          gap: 0.95rem;
        }

        .node-card--top,
        .node-card--middle {
          width: min(320px, 100%);
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <section class="org-shell">
      <h1 class="org-title">Unser Team</h1>
      <p class="org-subtitle">Die Teamstruktur von HelioTrackX im Überblick.</p>

      <div class="org-chart">
        <div class="row-center">{top_card}</div>
        <div class="line line-vertical-top"></div>
        <div class="row-center">{middle_card}</div>
        <div class="line line-vertical-branch"></div>
        <div class="line line-horizontal"></div>
        <div class="row-bottom">{bottom_cards}</div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)
