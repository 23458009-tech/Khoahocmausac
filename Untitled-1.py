
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Khoa học Màu sắc",
    layout="wide"
)

# ===== PHẦN ĐẦU TRANG: LOGO + TÊN TRƯỜNG =====
col_logo, col_school = st.columns([1, 8], vertical_alignment="center")

with col_logo:
    logo_path = Path("logo_truong.png")

    if logo_path.exists():
        st.image(str(logo_path), width=120)
    else:
        st.warning("Vui lòng thêm file logo_truong.png")

with col_school:
    st.markdown(
        """
        <h2 style="margin-bottom: 5px;">
            TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP.HCM
        </h2>
        <p style="font-size: 16px; margin-top: 0;">
            HO CHI MINH CITY UNIVERSITY OF TECHNOLOGY
        </p>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ===== THÔNG TIN PROJECT =====
st.write("### Chào mừng bạn đến với project Khoa học Màu sắc của mình!")

st.write("# Mình tên là Nguyễn Hoàng Khiêm")

st.write("# Mã số sinh viên: 23458009")
