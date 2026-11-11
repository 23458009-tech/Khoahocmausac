
import streamlit as st
import base64
from pathlib import Path

# ==========================================
# 1. CẤU HÌNH WEBSITE
# ==========================================

st.set_page_config(
    page_title="Khoa học Màu sắc - HCMUTE",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. ĐỌC HÌNH ẢNH
# ==========================================

def image_to_base64(path):
    file_path = Path(path)

    if not file_path.exists():
        return ""

    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

background = image_to_base64("background_hcmute.jpg")
logo_hcmute = image_to_base64("logo_hcmute.png")
logo_khoa = image_to_base64("logo_khoa.png")

# ==========================================
# 3. CSS GIAO DIỆN
# ==========================================

st.markdown(f"""
<style>

/* Ẩn thành phần mặc định Streamlit */
#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

.stApp {{
    background-image: url("data:image/jpeg;base64,{background}");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Bỏ khoảng trắng mặc định */
.block-container {{
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    max-width: 100% !important;
}}

/* Căn giữa nội dung */
.main-content {{
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 4vw;
    box-sizing: border-box;
}}

/* Khung nội dung chính */
.content-card {{
    width: 100%;
    max-width: 1450px;
    min-height: 760px;
    padding: 35px 45px;
    border-radius: 55px;

    background: rgba(235, 248, 255, 0.78);

    border: 1px solid rgba(255,255,255,0.75);

    box-shadow:
        0 10px 35px rgba(0, 70, 140, 0.18),
        inset 0 0 25px rgba(255,255,255,0.25);

    backdrop-filter: blur(3px);
    -webkit-backdrop-filter: blur(3px);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    text-align: center;
}}

/* Logo trường */
.logo-school {{
    width: min(550px, 90%);
    height: 125px;
    object-fit: contain;
    margin-bottom: 25px;
}}

/* Logo khoa */
.logo-faculty {{
    width: 350px;
    max-width: 85%;
    height: 145px;
    object-fit: contain;
    margin-top: 25px;
}}

/* Tên khoa */
.faculty-name {{
    color: #064FE0;
    font-size: clamp(23px, 2.3vw, 39px);
    font-weight: 850;
    margin-top: 15px;
    text-transform: uppercase;
    line-height: 1.4;
    text-shadow: 1px 2px 2px rgba(255,255,255,0.9);
}}

/* Lời chào */
.welcome-text {{
    color: #064DD8;
    font-size: clamp(20px, 2.2vw, 39px);
    font-weight: 750;
    margin-top: 65px;
    line-height: 1.5;
    text-shadow: 1px 2px 3px white;
}}

/* Thông tin sinh viên */
.student-info {{
    color: #064DD8;
    font-size: clamp(19px, 2.2vw, 38px);
    font-weight: 750;
    margin-top: 5px;
    line-height: 1.5;
    text-shadow: 1px 2px 3px white;
}}

/* Responsive điện thoại */
@media (max-width: 768px) {{

    .main-content {{
        padding: 18px;
    }}

    .content-card {{
        min-height: 85vh;
        padding: 30px 15px;
        border-radius: 28px;
    }}

    .logo-school {{
        height: 100px;
    }}

    .logo-faculty {{
        height: 110px;
        margin-top: 35px;
    }}

    .welcome-text {{
        margin-top: 40px;
    }}

}}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. HIỂN THỊ NỘI DUNG WEBSITE
# ==========================================

st.markdown(f"""
<div class="main-content">

    <div class="content-card">

        <!-- LOGO HCMUTE -->

        <img
            src="data:image/png;base64,{logo_hcmute}"
            class="logo-school"
        >

        <!-- LOGO KHOA -->

        <img
            src="data:image/png;base64,{logo_khoa}"
            class="logo-faculty"
        >

        <!-- TÊN KHOA -->

        <div class="faculty-name">
            KHOA MỸ THUẬT VÀ TRUYỀN THÔNG
        </div>

        <!-- LỜI CHÀO -->

        <div class="welcome-text">
            Chào mừng bạn đến với project
            Khoa học Màu sắc của mình!
        </div>

        <!-- THÔNG TIN SINH VIÊN -->

        <div class="student-info">
            Mình tên là Nguyễn Hoàng Khiêm,
            MSSV: 23458009
        </div>

    </div>

</div>
""", unsafe_allow_html=True)
