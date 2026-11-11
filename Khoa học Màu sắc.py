
import streamlit as st
import base64
import mimetypes
from pathlib import Path

# ==========================================
# 1. CẤU HÌNH STREAMLIT
# ==========================================

st.set_page_config(
    page_title="Khoa học Màu sắc | HCMUTE",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. HÀM ĐỌC HÌNH ẢNH
# ==========================================

def get_image(path):

    file = Path(path)

    if not file.exists():
        st.error(f"Không tìm thấy hình ảnh: {path}")
        st.stop()

    mime, _ = mimetypes.guess_type(str(file))

    if not mime:
        mime = "image/png"

    with open(file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime};base64,{encoded}"


# ==========================================
# 3. NẠP HÌNH ẢNH
# ==========================================

background = get_image("background_hcmute.png")
logo_hcmute = get_image("logo_hcmute.png")
logo_khoa = get_image("logo_khoa.png")


# ==========================================
# 4. THÔNG TIN SINH VIÊN
# ==========================================

ten_sinh_vien = "Nguyễn Hoàng Khiêm"
mssv = "23458009"

ten_khoa = "KHOA MỸ THUẬT VÀ TRUYỀN THÔNG"

loi_chao = (
    "Chào mừng bạn đến với project "
    "Khoa học Màu sắc của mình!"
)


# ==========================================
# 5. HTML + CSS
# ==========================================

html_code = f"""
<style>

/* XÓA GIAO DIỆN MẶC ĐỊNH */

#MainMenu,
footer,
header,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stSidebar"],
[data-testid="stSidebarNav"],
[data-testid="collapsedControl"] {{
    display: none !important;
    visibility: hidden !important;
}}

/* NỀN TOÀN TRANG */

html, body {{
    margin: 0 !important;
    padding: 0 !important;
}}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main {{
    background: transparent !important;
}}

.stApp {{
    background-image: url("{background}") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
    min-height: 100vh;
}}

/* KHU VỰC CHÍNH */

[data-testid="stMainBlockContainer"] {{
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}}

/* KHUNG BAO */

.main-wrapper {{

    width: 100%;
    min-height: 100vh;

    display: flex;
    align-items: center;
    justify-content: center;

    padding: 3.5%;
    box-sizing: border-box;
}}

/* KHUNG TRONG SUỐT */

.content-card {{

    width: 100%;
    max-width: 1450px;

    min-height: 86vh;

    box-sizing: border-box;

    padding: 40px 35px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;

    text-align: center;

    background: rgba(225, 245, 255, 0.76);

    border: 1px solid rgba(255,255,255,0.8);

    border-radius: 55px;

    box-shadow:
        0 8px 30px rgba(0, 70, 140, 0.20),
        inset 0 0 20px rgba(255,255,255,0.25);

    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
}}

/* LOGO TRƯỜNG */

.school-logo {{

    width: min(760px, 85%);
    height: 145px;

    object-fit: contain;

    margin-bottom: 35px;
}}

/* LOGO KHOA */

.faculty-logo {{

    width: 360px;
    max-width: 80%;

    height: 150px;

    object-fit: contain;

    margin-bottom: 15px;
}}

/* TÊN KHOA */

.faculty-title {{

    color: #0754D9;

    font-size: clamp(22px, 2.5vw, 38px);

    font-weight: 850;

    line-height: 1.4;

    text-shadow: 1px 2px 2px white;
}}

/* LỜI CHÀO */

.welcome-title {{

    color: #0750D5;

    font-size: clamp(20px, 2.35vw, 37px);

    font-weight: 750;

    line-height: 1.5;

    margin-top: 65px;

    text-shadow: 1px 2px 3px white;
}}

/* THÔNG TIN SINH VIÊN */

.student-name {{

    color: #0750D5;

    font-size: clamp(19px, 2.35vw, 37px);

    font-weight: 750;

    line-height: 1.5;

    margin-top: 5px;

    text-shadow: 1px 2px 3px white;
}}

/* RESPONSIVE TABLET */

@media (max-width: 768px) {{

    .main-wrapper {{
        padding: 18px;
    }}

    .content-card {{
        min-height: 90vh;
        padding: 35px 15px;
        border-radius: 30px;
    }}

    .school-logo {{
        height: 105px;
        margin-bottom: 25px;
    }}

    .faculty-logo {{
        height: 110px;
    }}

    .welcome-title {{
        margin-top: 40px;
    }}
}}

/* RESPONSIVE MOBILE */

@media (max-width: 480px) {{

    .content-card {{
        padding: 25px 12px;
    }}

    .school-logo {{
        height: 85px;
    }}

    .faculty-logo {{
        height: 95px;
    }}

    .welcome-title {{
        margin-top: 30px;
    }}
}}

</style>


<div class="main-wrapper">

    <div class="content-card">

        <img
            src="{logo_hcmute}"
            class="school-logo"
            alt="Logo HCMUTE"
        >

        <img
            src="{logo_khoa}"
            class="faculty-logo"
            alt="Faculty of Arts and Media"
        >

        <div class="faculty-title">
            {ten_khoa}
        </div>

        <div class="welcome-title">
            {loi_chao}
        </div>

        <div class="student-name">
            Mình tên là {ten_sinh_vien},
            MSSV: {mssv}
        </div>

    </div>

</div>
"""

# ==========================================
# 6. HIỂN THỊ WEBSITE
# ==========================================

st.html(html_code)
