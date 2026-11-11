import base64
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]


@st.cache_data(show_spinner=False)
def _image_data_uri(path_string: str) -> str:
    path = Path(path_string)
    if not path.is_file():
        return ""
    extension = path.suffix.lower()
    mime_type = "image/png" if extension == ".png" else "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def asset_uri(filename: str) -> str:
    return _image_data_uri(str(ROOT / filename))


def apply_theme():
    background = asset_uri("background_hcmute.png")
    background_css = (
        f'background-image: url("{background}");'
        if background
        else "background-image: linear-gradient(135deg, #b9e5ff, #effaff);"
    )

    st.markdown(
        f"""
        <style>
        /* --------------- Global page --------------- */
        #MainMenu, footer {{ visibility: hidden; }}
        [data-testid="stHeader"] {{
            background: rgba(255,255,255,0.08);
        }}
        .stApp {{
            {background_css}
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {{
            background: transparent !important;
        }}
        [data-testid="stMainBlockContainer"] {{
            width: 100%;
            max-width: 100% !important;
            padding: 1.1rem 1.5rem 2rem 1.5rem !important;
        }}

        /* --------------- Keep the left navigation --------------- */
        [data-testid="stSidebar"] {{
            display: block !important;
            visibility: visible !important;
            min-width: 260px;
            width: 260px;
            background: rgba(248,250,252,0.98) !important;
            border-right: 1px solid #dce5ee;
        }}
        [data-testid="stSidebar"] > div {{
            background: rgba(248,250,252,0.98) !important;
        }}
        [data-testid="stSidebarContent"] {{
            background: rgba(248,250,252,0.98) !important;
            padding-top: 1rem;
        }}
        [data-testid="stSidebarNav"] {{
            display: block !important;
            visibility: visible !important;
        }}
        [data-testid="stSidebarNav"] a {{
            border-radius: 8px;
            margin: 2px 8px;
        }}
        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background: #e5efff;
            color: #0754a5;
            font-weight: 700;
        }}
        [data-testid="collapsedControl"] {{
            display: flex !important;
            visibility: visible !important;
        }}

        /* --------------- Home glass panel --------------- */
        .home-wrap {{
            width: 100%;
            min-height: calc(100vh - 3.2rem);
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
            padding: 0.8rem;
        }}
        .home-card {{
            width: 100%;
            max-width: 1450px;
            min-height: 84vh;
            box-sizing: border-box;
            padding: clamp(24px, 4vh, 48px) clamp(16px, 3vw, 42px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            text-align: center;
            background: rgba(225,245,255,0.76);
            border: 1px solid rgba(255,255,255,0.88);
            border-radius: 42px;
            box-shadow:
                0 8px 32px rgba(0,65,130,0.18),
                inset 0 0 22px rgba(255,255,255,0.25);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
        }}
        .school-logo {{
            display: block;
            width: min(760px, 88%);
            height: clamp(95px, 13vh, 145px);
            object-fit: contain;
            margin: 0 auto clamp(18px, 3vh, 32px);
        }}
        .faculty-logo {{
            display: block;
            width: min(360px, 72%);
            height: clamp(100px, 14vh, 155px);
            object-fit: contain;
            margin: 0 auto 12px;
        }}
        .faculty-title {{
            color: #0754d9;
            font-size: clamp(20px, 2.4vw, 36px);
            font-weight: 850;
            line-height: 1.35;
            text-shadow: 1px 2px 2px rgba(255,255,255,0.95);
        }}
        .welcome-title {{
            color: #0750d5;
            font-size: clamp(19px, 2.15vw, 34px);
            font-weight: 750;
            line-height: 1.5;
            margin-top: clamp(32px, 6vh, 62px);
            text-shadow: 1px 2px 3px rgba(255,255,255,0.95);
        }}
        .student-title {{
            color: #0750d5;
            font-size: clamp(18px, 2.1vw, 33px);
            font-weight: 750;
            line-height: 1.5;
            margin-top: 5px;
            text-shadow: 1px 2px 3px rgba(255,255,255,0.95);
        }}

        /* --------------- Inner pages --------------- */
        .page-panel {{
            background: rgba(255,255,255,0.93);
            border: 1px solid rgba(255,255,255,0.88);
            border-radius: 20px;
            padding: 1.25rem 1.5rem;
            box-shadow: 0 5px 22px rgba(0,55,110,0.10);
        }}

        /* --------------- Responsive --------------- */
        @media (max-width: 768px) {{
            [data-testid="stMainBlockContainer"] {{
                padding: 0.8rem !important;
            }}
            .home-wrap {{
                min-height: 88vh;
                padding: 0.4rem;
            }}
            .home-card {{
                min-height: 86vh;
                border-radius: 26px;
                padding: 28px 14px;
            }}
            .school-logo {{
                height: 100px;
            }}
            .faculty-logo {{
                height: 105px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, description: str | None = None):
    st.markdown(
        f"""
        <div class="page-panel">
            <h2 style="color:#0754a5; margin:0;">{title}</h2>
            {f'<p style="margin:.5rem 0 0;color:#38556d;">{description}</p>' if description else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
