
import streamlit as st
import base64
import mimetypes
from pathlib import Path

# =====================================================
# 1. CẤU HÌNH WEBSITE
# =====================================================

st.set_page_config(
    page_title="Khoa học Màu sắc | HCMUTE",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. HÀM ĐỌC HÌNH ẢNH
# =====================================================

def image_to_base64(filename):

    path = Path(filename)

    if not path.exists():
        st.error(f"Không tìm thấy file hình ảnh: {filename}")
        st.stop()

    mime_type, _ = mimetypes.guess_type(str(path))

    if not mime_type:
        mime_type = "image/png"

    with open(path, "rb") as file:
        encoded = base64.b64encode(
            file.read()
        ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


# =====================================================
# 3. TẢI HÌNH ẢNH
# =====================================================

background = image_to_base64("background_hcmute.png")
logo_hcmute = image_to_base64("logo_hcmute.png")
logo_khoa = image_to_base64("logo_khoa.png")


# =====================================================
# 4. THÔNG TIN SINH VIÊN
# =====================================================

ten_sinh_vien = "Nguyễn Hoàng Khiêm"
mssv = "23458009"

ten_khoa = "KHOA MỸ THUẬT VÀ TRUYỀN THÔNG"

loi_chao = (
    "Chào mừng bạn đến với project "
    "Khoa học Màu sắc của mình!"
)


# =====================================================
# 5. CSS TOÀN WEBSITE
# =====================================================

css = """
<style>

/* =========================================
   THIẾT LẬP CHUNG
========================================= */

html, body {
    margin: 0;
    padding: 0;
}

#MainMenu,
footer {
    visibility: hidden;
}

/* =========================================
   HÌNH NỀN TOÀN WEBSITE
========================================= */

.stApp {
    background-image: url("__BACKGROUND__");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    min-height: 100vh;
}

/* Khu vực nội dung trong suốt */

[data-testid="stMain"],
[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

/* =========================================
   SIDEBAR - THANH BÊN TRÁI
========================================= */

[data-testid="stSidebar"] {
    display: block !important;
    visibility: visible !important;
    min-width: 270px;
    width: 270px;
    background-color: #F7F8FA !important;
    border-right: 1px solid #E1E1E1;
}

[data-testid="stSidebarContent"] {
    padding-top: 25px;
    background-color: #F7F8FA !important;
}

/* Giữ lại danh sách điều hướng */

[data-testid="stSidebarNav"] {
    display: block !important;
    visibility: visible !important;
}

/* Chữ trong thanh điều hướng */

[data-testid="stSidebarNav"] span {
    font-size: 14px;
}

/* Hiệu ứng mục đang chọn */

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #E6EDF8;
    border-radius: 8px;
    font-weight: 700;
}

/* Nút thu gọn sidebar */

[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
}

/* =========================================
   KHU VỰC NỘI DUNG BÊN PHẢI
========================================= */

[data-testid="stMainBlockContainer"],
.main .block-container {
    max-width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* =========================================
   KHUNG BAO NGOÀI
========================================= */

.main-wrapper {

    width: 100%;
    min-height: 100vh;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 35px;
    box-sizing: border-box;
}

/* =========================================
   KHUNG KÍNH TRONG SUỐT
========================================= */

.content-card {

    width: 100%;
    max-width: 1450px;

    min-height: calc(100vh - 100px);

    padding: 45px 35px;

    box-sizing: border-box;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;

    text-align: center;

    background: rgba(225, 245, 255, 0.77);

    border: 1px solid rgba(255, 255, 255, 0.8);

    border-radius: 55px;

    box-shadow:
        0 8px 30px rgba(0, 70, 140, 0.18),
        inset 0 0 20px rgba(255, 255, 255, 0.25);

    backdrop-filter: blur(4px);
    -webkit-backdrop-filter: blur(4px);
}

/* =========================================
   LOGO HCMUTE
========================================= */

.school-logo {

    display: block;

    width: min(760px, 85%);
    height: 145px;

    object-fit: contain;

    margin: 0 auto 35px;
}

/* =========================================
   LOGO KHOA
========================================= */

.faculty-logo {

    display: block;

    width: 360px;
    max-width: 80%;

    height: 150px;

    object-fit: contain;

    margin: 0 auto 15px;
}

/* =========================================
   TÊN KHOA
========================================= */

.faculty-title {

    color: #0754D9;

    font-size: clamp(22px, 2.5vw, 38px);

    font-weight: 850;

    line-height: 1.4;

    margin: 0;

    text-transform: uppercase;

    text-shadow: 1px 2px 2px rgba(255,255,255,0.95);
}

/* =========================================
   LỜI CHÀO
========================================= */

.welcome-title {

    color: #0750D5;

    font-size: clamp(20px, 2.35vw, 37px);

    font-weight: 750;

    line-height: 1.5;

    margin-top: 65px;

    text-shadow: 1px 2px 3px rgba(255,255,255,0.95);
}

/* =========================================
   THÔNG TIN SINH VIÊN
========================================= */

.student-name {

    color: #0750D5;

    font-size: clamp(19px, 2.35vw, 37px);

    font-weight: 750;

    line-height: 1.5;

    margin-top: 5px;

    text-shadow: 1px 2px 3px rgba(255,255,255,0.95);
}

/* =========================================
   RESPONSIVE - TABLET
========================================= */

@media (max-width: 768px) {

    [data-testid="stSidebar"] {
        min-width: 250px;
        width: 250px;
    }

    .main-wrapper {
        padding: 18px;
    }

    .content-card {
        min-height: 90vh;
        padding: 35px 15px;
        border-radius: 30px;
    }

    .school-logo {
        height: 105px;
        margin-bottom: 25px;
    }

    .faculty-logo {
        height: 110px;
    }

    .welcome-title {
        margin-top: 40px;
    }
}

/* =========================================
   RESPONSIVE - ĐIỆN THOẠI
========================================= */

@media (max-width: 480px) {

    .main-wrapper {
        padding: 12px;
    }

    .content-card {
        min-height: 90vh;
        padding: 25px 12px;
        border-radius: 25px;
    }

    .school-logo {
        height: 85px;
    }

    .faculty-logo {
        height: 95px;
    }

    .welcome-title {
        margin-top: 30px;
    }
}

</style>
"""

# Thay đường dẫn ảnh nền vào CSS
css = css.replace("__BACKGROUND__", background)

# Hiển thị CSS
st.markdown(css, unsafe_allow_html=True)


# =====================================================
# 6. TẠO HTML TRANG CHỦ
# =====================================================

html_code = f"""

<div class="main-wrapper">

    <div class="content-card">

        <!-- LOGO TRƯỜNG HCMUTE -->

        <img
            src="{logo_hcmute}"
            class="school-logo"
            alt="Logo HCMUTE"
        >

        <!-- LOGO FACULTY OF ARTS & MEDIA -->

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

"""

# Hiển thị HTML trang chủ
st.markdown(html_code, unsafe_allow_html=True)
