
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Khoa học Màu sắc HCMUTE",
    layout="wide"
)

# 1. Đọc logo
logo_hcmute = Image.open("B_Tagline - HCM-UTE -.png").convert("RGBA")
logo_khoa = Image.open("logo khoa.png").convert("RGBA")

# 2. Cắt khoảng trắng trong suốt
def crop_logo(image):
    bbox = image.getbbox()
    if bbox:
        return image.crop(bbox)
    return image

logo_hcmute = crop_logo(logo_hcmute)
logo_khoa = crop_logo(logo_khoa)

# 3. Chuẩn hóa chiều cao logo
chieu_cao = 150

def resize_logo(image, height):
    width = int(image.width * height / image.height)
    return image.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )

logo_hcmute = resize_logo(logo_hcmute, chieu_cao)
logo_khoa = resize_logo(logo_khoa, chieu_cao)

# 4. Tạo khung ảnh
khung_rong = 900
khung_cao = 160

def tao_khung(image):
    canvas = Image.new(
        "RGBA",
        (khung_rong, khung_cao),
        (255, 255, 255, 255)
    )

    x = (khung_rong - image.width) // 2
    y = 0

    canvas.paste(image, (x, y), image)
    return canvas

logo1 = tao_khung(logo_hcmute)
logo2 = tao_khung(logo_khoa)

# 5. Hiển thị logo
col1, col2 = st.columns(2)

with col1:
    st.image(logo1, use_container_width=True)

with col2:
    st.image(logo2, use_container_width=True)

# 6. Tạo khoảng cách
for i in range(4):
    st.write("")

# 7. Tiêu đề chào mừng
st.markdown(
    """
    <h2 style="
        text-align: center;
        color: #1565C0;
        font-weight: 700;
    ">
        Chào mừng bạn đến với project Khoa học Màu sắc!
    </h2>
    """,
    unsafe_allow_html=True
)

# 8. Tên sinh viên
st.markdown(
    """
    <h1 style="
        text-align: center;
        color: #303F9F;
        font-size: 46px;
        font-weight: 800;
        margin-top:15px;
    ">
        NGÔ THANH LỘC
    </h1>
    """,
    unsafe_allow_html=True
)

# 9. Mã số sinh viên
st.markdown(
    """
    <h2 style="
        text-align: center;
        color: #F57C00;
        font-size: 36px;
        font-weight: 700;
        margin-top: 10px;
    ">
        MSSV: 23458010
    </h2>
    """,
    unsafe_allow_html=True
)


# 10. Chèn ảnh khuôn viên trường
st.image(
    "background_hcmute.jpg",
    caption="Trường Đại học công nghệ Kỹ thuật TP. Hồ Chí Minh",
    use_container_width=True
)