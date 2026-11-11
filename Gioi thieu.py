import streamlit as st
from utils.ui import apply_theme, asset_uri

st.set_page_config(
    page_title="Khoa học Màu sắc | HCMUTE",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

# Streamlit tự tạo danh sách 8 trang từ thư mục pages/.
with st.sidebar:
    st.markdown("## 🎨 Khoa học Màu sắc")
    st.caption("HCMUTE · Faculty of Arts & Media")
    st.divider()
    st.markdown("**Hướng dẫn sử dụng**")
    st.markdown(
        """
        1. Chọn chức năng ở danh sách phía trên.
        2. Chuẩn bị dữ liệu CSV hoặc MAT nếu trang yêu cầu.
        3. Nhập thông số và nhấn nút tính toán / vẽ biểu đồ.
        """
    )
    st.divider()
    st.caption("Project học phần Khoa học Màu sắc")

logo_hcmute = asset_uri("logo_hcmute.png")
logo_khoa = asset_uri("logo_khoa.png")

missing_assets = []
if not logo_hcmute:
    missing_assets.append("logo_hcmute.png")
if not logo_khoa:
    missing_assets.append("logo_khoa.png")

if missing_assets:
    st.error("Thiếu hình ảnh: " + ", ".join(missing_assets))
    st.info("Đặt các file logo cùng cấp với app.py rồi tải lại trang.")
    st.stop()

st.markdown(
    f"""
    <div class="home-wrap">
      <section class="home-card">
        <img src="{logo_hcmute}" class="school-logo" alt="Logo HCMUTE">
        <img src="{logo_khoa}" class="faculty-logo" alt="Faculty of Arts and Media">
        <div class="faculty-title">KHOA MỸ THUẬT VÀ TRUYỀN THÔNG</div>
        <div class="welcome-title">
          Chào mừng bạn đến với project Khoa học Màu sắc của mình!
        </div>
        <div class="student-title">
          Mình tên là Nguyễn Hoàng Khiêm, MSSV: 23458009
        </div>
      </section>
    </div>
    """,
    unsafe_allow_html=True,
)
