
import streamlit as st
import numpy as np
import colour

# =====================================================
# 1. CẤU HÌNH GIAO DIỆN
# =====================================================

from ui_helpers import apply_theme, page_header

st.set_page_config(
    page_title="Chuyển đổi không gian màu | HCMUTE",
    page_icon="🎨",
    layout="wide"
)

apply_theme()

page_header(
    "CHUYỂN ĐỔI KHÔNG GIAN MÀU",
    "Chuyển đổi giữa sRGB và CIE XYZ theo thư viện Colour Science."
)

# =====================================================
# 2. CSS GIAO DIỆN
# =====================================================

st.markdown("""
<style>
.result-box {
    background: rgba(255,255,255,0.94);
    border-radius: 15px;
    padding: 20px;
    border: 1px solid #dce8f5;
    box-shadow: 0 4px 15px rgba(0,50,100,0.08);
}
.section-title {
    color: #0754a5;
    font-size: 23px;
    font-weight: 700;
}
.color-preview {
    width: 100%;
    height: 110px;
    border-radius: 12px;
    border: 2px solid white;
    box-shadow: 0 3px 12px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# 3. LỰA CHỌN CHIỀU CHUYỂN ĐỔI
# =====================================================

st.markdown("### ⚙️ Thiết lập chuyển đổi")

mode = st.radio(
    "Chọn chiều chuyển đổi:",
    ["sRGB → XYZ", "XYZ → sRGB"],
    horizontal=True
)

st.divider()

# =====================================================
# 4. CHUYỂN ĐỔI sRGB SANG XYZ
# =====================================================

if mode == "sRGB → XYZ":

    st.markdown(
        '<div class="section-title">🔴 Chuyển đổi sRGB → CIE XYZ</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Nhập giá trị ba kênh màu RGB trong khoảng từ 0 đến 255."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        R = st.number_input(
            "Giá trị R (0–255)",
            min_value=0,
            max_value=255,
            value=255,
            step=1
        )

    with col2:
        G = st.number_input(
            "Giá trị G (0–255)",
            min_value=0,
            max_value=255,
            value=0,
            step=1
        )

    with col3:
        B = st.number_input(
            "Giá trị B (0–255)",
            min_value=0,
            max_value=255,
            value=0,
            step=1
        )

    rgb_preview = f"rgb({R},{G},{B})"

    st.markdown(
        f"""
        <div style="
            background:{rgb_preview};
            height:75px;
            border-radius:12px;
            border:2px solid white;
            box-shadow:0 3px 12px rgba(0,0,0,.15);
        "></div>
        """,
        unsafe_allow_html=True
    )

    st.caption(f"Màu RGB đầu vào: {rgb_preview}")

    if st.button("🔄 CHUYỂN SANG XYZ", type="primary", use_container_width=True):

        try:
            rgb = np.array([R, G, B], dtype=float) / 255.0

            xyz = colour.sRGB_to_XYZ(rgb) * 100

            st.success("Chuyển đổi thành công!")

            st.markdown("### 📊 Kết quả CIE XYZ")

            c1, c2, c3 = st.columns(3)

            c1.metric("X", f"{xyz[0]:.4f}")
            c2.metric("Y", f"{xyz[1]:.4f}")
            c3.metric("Z", f"{xyz[2]:.4f}")

            st.markdown(
                f"""
                <div class="result-box">
                    <b>Kết quả:</b><br><br>
                    X = {xyz[0]:.4f}<br>
                    Y = {xyz[1]:.4f}<br>
                    Z = {xyz[2]:.4f}
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Lỗi chuyển đổi: {e}")

# =====================================================
# 5. CHUYỂN ĐỔI XYZ SANG sRGB
# =====================================================

else:

    st.markdown(
        '<div class="section-title">🔵 Chuyển đổi CIE XYZ → sRGB</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Nhập giá trị X, Y, Z. Các giá trị được sử dụng theo thang XYZ 0–100."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        X = st.number_input(
            "Giá trị X",
            min_value=0.0,
            value=95.047,
            step=0.1,
            format="%.3f"
        )

    with col2:
        Y = st.number_input(
            "Giá trị Y",
            min_value=0.0,
            value=100.0,
            step=0.1,
            format="%.3f"
        )

    with col3:
        Z = st.number_input(
            "Giá trị Z",
            min_value=0.0,
            value=108.883,
            step=0.1,
            format="%.3f"
        )

    if st.button("🔄 CHUYỂN SANG sRGB", type="primary", use_container_width=True):

        try:
            xyz = np.array([X, Y, Z], dtype=float) / 100.0

            # Chuyển đổi XYZ sang RGB tuyến tính
            rgb_linear = colour.XYZ_to_sRGB(xyz)

            # Mã hóa RGB theo hàm truyền sRGB
            rgb_encoded = colour.cctf_encoding(rgb_linear)

            # Giá trị RGB 8-bit trước khi giới hạn
            rgb_255 = rgb_encoded * 255.0

            st.success("Chuyển đổi thành công!")

            st.markdown("### 📊 Kết quả sRGB")

            c1, c2, c3 = st.columns(3)

            c1.metric("R", f"{rgb_255[0]:.2f}")
            c2.metric("G", f"{rgb_255[1]:.2f}")
            c3.metric("B", f"{rgb_255[2]:.2f}")

            # Kiểm tra gamut sRGB
            out_of_gamut = np.any(
                (rgb_255 < 0) | (rgb_255 > 255)
            )

            # Giới hạn RGB 8-bit
            clipped = np.clip(
                rgb_255, 0, 255
            ).round().astype(int)

            st.markdown(
                f"""
                <div class="result-box">
                    <b>Mã màu RGB 8-bit:</b><br><br>
                    R = {clipped[0]}<br>
                    G = {clipped[1]}<br>
                    B = {clipped[2]}<br><br>
                    <b>CSS Color:</b>
                    rgb({clipped[0]}, {clipped[1]}, {clipped[2]})
                </div>
                """,
                unsafe_allow_html=True
            )

            color_hex = "#{:02X}{:02X}{:02X}".format(
                clipped[0], clipped[1], clipped[2]
            )

            st.markdown(
                f"""
                <div style="
                    background:{color_hex};
                    height:100px;
                    border-radius:12px;
                    border:2px solid white;
                    margin-top:15px;
                    box-shadow:0 3px 12px rgba(0,0,0,.15);
                "></div>
                """,
                unsafe_allow_html=True
            )

            st.caption(f"Mã HEX: {color_hex}")

            if out_of_gamut:
                st.warning(
                    "Một hoặc nhiều kênh màu nằm ngoài gamut sRGB. "
                    "Giá trị hiển thị đã được giới hạn về khoảng 0–255."
                )

        except Exception as e:
            st.error(f"Lỗi chuyển đổi: {e}")

# =====================================================
# 6. THÔNG TIN PHƯƠNG PHÁP
# =====================================================

st.divider()

with st.expander("📘 Thông tin về không gian màu sRGB và CIE XYZ"):

    st.markdown("""
    **sRGB (Standard Red Green Blue)**

    Là không gian màu RGB tiêu chuẩn được sử dụng rộng rãi
    trong màn hình, hình ảnh kỹ thuật số và thiết bị điện tử.

    **CIE XYZ**

    Là không gian màu được xây dựng bởi Ủy ban Quốc tế về Chiếu sáng (CIE),
    sử dụng ba thành phần X, Y, Z để biểu diễn màu sắc.

    **Lưu ý:**
    - Chuyển đổi sRGB → XYZ sử dụng giá trị RGB đã chuẩn hóa về 0–1.
    - Giá trị XYZ trong giao diện được biểu diễn theo thang 0–100.
    - Chuyển đổi XYZ → sRGB có thể tạo ra giá trị ngoài gamut sRGB.
    - Khi hiển thị màu trên màn hình, giá trị RGB được giới hạn trong khoảng 0–255.
    """)
