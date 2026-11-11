from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parent
STATIC_URL = "/app/static"


def asset_url(filename: str) -> str:
    """URL for an image in the project's static/ directory."""
    path = ROOT / "static" / filename
    if not path.is_file():
        return ""
    return f"{STATIC_URL}/{filename}"


def apply_theme(is_intro: bool = False):
    """
    Trang giới thiệu: nền HCMUTE rõ nét như thiết kế hiện tại.
    Các trang chức năng: nền HCMUTE được làm mờ và giảm độ đậm 50%;
    lớp nội dung phía trước vẫn rõ nét.
    """
    background = asset_url("background_hcmute.png")

    if is_intro:
        background_css = (
            f'background-image: url("{background}");'
            if background
            else "background-image: linear-gradient(135deg, #b9e5ff, #effaff);"
        )
        background_layer_css = ""
    else:
        background_css = "background-image: none;"
        background_layer_css = f"""
        .stApp::before {{
            content: "";
            position: fixed;
            inset: -14px;
            z-index: 0;
            pointer-events: none;
            background-image: url("{background}");
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            filter: blur(7px);
            opacity: 0.50;
            transform: scale(1.025);
        }}
        """

    st.markdown(
        f"""
        <style>
        #MainMenu, footer {{ visibility: hidden; }}

        .stApp {{
            {background_css}
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            position: relative;
        }}

        {background_layer_css}

        [data-testid="stAppViewContainer"],
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"] {{
            background: transparent !important;
        }}

        [data-testid="stAppViewContainer"] {{
            position: relative;
            z-index: 1;
        }}

        [data-testid="stMainBlockContainer"] {{
            max-width: 100% !important;
            padding: 1rem 1.5rem 2rem 1.5rem !important;
            position: relative;
            z-index: 1;
        }}

        /* Sidebar luôn rõ nét, không áp dụng hiệu ứng mờ của nền */
        [data-testid="stSidebar"] {{
            display: block !important;
            visibility: visible !important;
            min-width: 260px;
            width: 260px;
            background: rgba(248,250,252,0.98) !important;
            border-right: 1px solid #dce5ee;
            position: relative;
            z-index: 2;
        }}
        [data-testid="stSidebar"] > div,
        [data-testid="stSidebarContent"] {{
            background: rgba(248,250,252,0.98) !important;
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
            background: #d9edff;
            color: #0754a5;
            font-weight: 700;
        }}
        [data-testid="collapsedControl"] {{
            display: flex !important;
            visibility: visible !important;
        }}

        /* Trang giới thiệu */
        .home-wrap {{
            width: 100%;
            min-height: calc(100vh - 2rem);
            display: flex;
            align-items: center;
            justify-content: center;
            box-sizing: border-box;
            padding: 0.6rem;
        }}
        .home-card {{
            width: 100%;
            max-width: 1600px;
            min-height: 90vh;
            box-sizing: border-box;
            padding: clamp(30px, 4.5vh, 58px) clamp(22px, 4vw, 58px);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            text-align: center;
            background: rgba(225,245,255,0.78);
            border: 1px solid rgba(255,255,255,0.9);
            border-radius: 42px;
            box-shadow: 0 8px 32px rgba(0,65,130,0.18),
                        inset 0 0 22px rgba(255,255,255,0.25);
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
        }}
        .school-logo {{
            display: block;
            width: min(900px, 92%);
            height: clamp(125px, 16vh, 180px);
            object-fit: contain;
            margin: 0 auto clamp(24px, 3.5vh, 42px);
        }}
        .faculty-logo {{
            display: block;
            width: min(440px, 78%);
            height: clamp(130px, 17vh, 185px);
            object-fit: contain;
            margin: 0 auto 18px;
        }}
        .faculty-title {{
            color: #0754d9;
            font-size: clamp(27px, 2.8vw, 43px);
            font-weight: 850;
            line-height: 1.35;
            text-shadow: 1px 2px 2px rgba(255,255,255,.95);
        }}
        .welcome-title {{
            color: #0750d5;
            font-size: clamp(27px, 2.5vw, 40px);
            font-weight: 750;
            line-height: 1.5;
            margin-top: clamp(38px, 6.5vh, 76px);
            text-shadow: 1px 2px 3px rgba(255,255,255,.95);
        }}
        .student-title {{
            color: #0750d5;
            font-size: clamp(25px, 2.35vw, 38px);
            font-weight: 750;
            line-height: 1.5;
            margin-top: 5px;
            text-shadow: 1px 2px 3px rgba(255,255,255,.95);
        }}
        .page-panel {{
            background: rgba(255,255,255,0.94);
            border: 1px solid rgba(255,255,255,0.9);
            border-radius: 20px;
            padding: 1.25rem 1.5rem;
            box-shadow: 0 5px 22px rgba(0,55,110,0.10);
        }}

        @media (max-width: 768px) {{
            [data-testid="stMainBlockContainer"] {{ padding: .6rem !important; }}
            .home-wrap {{ min-height: 88vh; padding: .3rem; }}
            .home-card {{ min-height: 90vh; border-radius: 25px; padding: 28px 14px; }}
            .school-logo {{ height: 115px; }}
            .faculty-logo {{ height: 120px; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, description: str | None = None):
    safe_title = title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    safe_description = ""
    if description:
        safe_description = (
            '<p style="margin:.5rem 0 0;color:#38556d;">'
            + description.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            + "</p>"
        )
    st.markdown(
        f"""
        <div class="page-panel">
            <h2 style="color:#0754a5; margin:0;">{safe_title}</h2>
            {safe_description}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
