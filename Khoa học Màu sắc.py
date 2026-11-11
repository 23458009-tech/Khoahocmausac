
import streamlit as st
import base64
import mimetypes
from pathlib import Path

# ==================================================
# 1. CẤU HÌNH TRANG WEB
# ==================================================

st.set_page_config(
    page_title="Khoa học Màu sắc | HCMUTE",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# 2. ĐỌC VÀ CHUYỂN HÌNH ẢNH SANG BASE64
# ==================================================

def image_to_base64(filename):

    path = Path(filename)

    if not path.exists():
        st.error(f"Không tìm thấy file: {filename}")
        st.stop()

    mime_type, _ = mimetypes.guess_type(str(path))

    if not mime_type:
        mime_type = "image/png"

    with open(path, "rb") as file:
        encoded = base64.b64encode(
            file.read()
        ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# Đường dẫn hình ảnh
background = image_to_base64("background_hcmute.png")
logo_hcmute = image_to_base64("logo_hcmute.png")
logo_khoa = image_to_base64("logo_khoa.png")


# ==================================================
# 3. THÔNG TIN SINH VIÊN
# ==================================================

ten_sinh_vien = "Nguyễn Hoàng Khiêm"
mssv = "23458009"

ten_khoa = "KHOA MỸ THUẬT VÀ TRUYỀN THÔNG"

loi_chao = (
    "Chào mừng bạn đến với project "
    "Khoa học Màu sắc của mình!"
)


# ==================================================
# 4. THIẾT KẾ GIAO DIỆN CSS
# ==================================================

st.markdown(f"""
<style>

/* XÓA GIAO DIỆN MẶC ĐỊNH STREAMLIT */

#MainMenu {{
    display: none;
}}

footer {{
    display: none;
}}

header {{
    display: none;
}}

.stApp {{
    background-image: url("{background}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* CĂN CHỈNH TOÀN TRANG */

.block-container {{
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}}

/* KHUNG CHÍNH */

.main-wrapper {{
    width: 100%;
    min-height: 100vh;

    display: flex;
    align-items: center;
    justify-content: center;

    padding: 35px;
    box-sizing: border-box;
}}

/* KHUNG NỘI DUNG TRONG SUỐT */

.content-card {{

    width: 100%;
    max-width: 1450px;

    min-height: 92vh;

    padding: 45px 35px;

    box-sizing: border-box;

    display: flex;
    flex-direction: column;
    align-items: center;

    text-align: center;

    background: rgba(224, 244, 255, 0.77);

    border: 1px solid rgba(255,255,255,0.75);

    border-radius: 55px;

    box-shadow:
        0 8px 30px rgba(0, 80, 150, 0.18),
        inset 0 0 20px rgba(255,255,255,0.25);

    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
}}

/* LOGO TRƯỜNG HCMUTE */

.school-logo {{
    display: block;

    width: min(760px, 85%);
    height: 145px;

    object-fit: contain;

    margin: 0 auto 35px;
}}

/* LOGO KHOA */

.faculty-logo {{
    display: block;

    width: 360px;
    max-width: 80%;

    height: 150px;

    object-fit: contain;

    margin: 0 auto 15px;
}}

/* TÊN KHOA */

.faculty-title {{

    color: #0754D9;

    font-size: clamp(22px, 2.5vw, 38px);

    font-weight: 850;

    line-height: 1.4;

    margin: 0;

    text-transform: uppercase;

    text-shadow:
        1px 2px 2px rgba(255,255,255,0.95);
}}

/* LỜI CHÀO */

.welcome-title {{

    color: #0750D5;

    font-size: clamp(20px, 2.35vw, 37px);

    font-weight: 750;

    line-height: 1.5;

    margin-top: 65px;

    text-shadow:
        1px 2px 3px rgba(255,255,255,0.95);
}}

/* THÔNG TIN SINH VIÊN */

.student-name {{

    color: #0750D5;

    font-size: clamp(19px, 2.35vw, 37px);

    font-weight: 750;

    line-height: 1.5;

    margin-top: 5px;

    text-shadow:
        1px 2px 3px rgba(255,255,255,0.95);
}}


/* ==================================================
   5. RESPONSIVE - MÁY TÍNH BẢNG VÀ ĐIỆN THOẠI
================================================== */

@media (max-width: 768px) {{

    .main-wrapper {{
        padding: 15px;
    }}

    .content-card {{
        min-height: 94vh;
        padding: 35px 15px;
        border-radius: 30px;
    }}

    .school-logo {{
        height: 100px;
        margin-bottom: 25px;
    }}

    .faculty-logo {{
        height: 110px;
        margin-top: 15px;
    }}

    .welcome-title {{
        margin-top: 45px;
    }}

}}

@media (max-width: 480px) {{

    .content-card {{
        padding: 30px 12px;
    }}

    .school-logo {{
        height: 85px;
    }}

    .faculty-logo {{
        height: 95px;
    }}

    .welcome-title {{
        margin-top: 35px;
    }}

}}

</style>
""", unsafe_allow_html=True)


# ==================================================
# 6. HIỂN THỊ WEBSITE
# ==================================================

st.markdown(f"""

<div class="main-wrapper">

    <div class="content-card">

        <!-- LOGO TRƯỜNG HCMUTE -->

        <img
            src="{logo_hcmute}"
            class="school-logo"
            alt="Logo HCMUTE"
        >

        <!-- LOGO FACULTY OF ARTS AND MEDIA -->

        <img
            src="{logo_khoa}"
            class="faculty-logo"
            alt="Faculty of Arts and Media"
        >

        <!-- TÊN KHOA -->

        <div class="faculty-title">
            {ten_khoa}
        </div>

        <!-- LỜI CHÀO MỪNG -->

        <div class="welcome-title">
            {loi_chao}
        </div>

        <!-- THÔNG TIN SINH VIÊN -->

        <div class="student-name">
            Mình tên là {ten_sinh_vien},
            MSSV: {mssv}
        </div>

    </div>

</div>

""", unsafe_allow_html=True)
