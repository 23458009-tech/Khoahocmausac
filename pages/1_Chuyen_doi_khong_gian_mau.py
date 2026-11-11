import streamlit as st
import numpy as np
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header("Chuyển đổi không gian màu", "Chuyển đổi giữa sRGB và XYZ theo thư viện Colour Science.")

mode = st.radio("Chọn chiều chuyển đổi", ["sRGB to XYZ", "XYZ to sRGB"], horizontal=True)

if mode == "sRGB to XYZ":
    st.subheader("sRGB → CIE XYZ")
    c1, c2, c3 = st.columns(3)
    with c1:
        R = st.number_input("Giá trị R (0–255)", min_value=0, max_value=255, value=255)
    with c2:
        G = st.number_input("Giá trị G (0–255)", min_value=0, max_value=255, value=0)
    with c3:
        B = st.number_input("Giá trị B (0–255)", min_value=0, max_value=255, value=0)

    if st.button("Chuyển sang XYZ", type="primary"):
        rgb = np.array([R, G, B], dtype=float) / 255.0
        xyz = colour.sRGB_to_XYZ(rgb) * 100
        a, b, c = st.columns(3)
        a.metric("X", f"{xyz[0]:.3f}")
        b.metric("Y", f"{xyz[1]:.3f}")
        c.metric("Z", f"{xyz[2]:.3f}")
else:
    st.subheader("CIE XYZ → sRGB")
    c1, c2, c3 = st.columns(3)
    with c1:
        X = st.number_input("Giá trị X", min_value=0.0, value=95.047, step=0.1)
    with c2:
        Y = st.number_input("Giá trị Y", min_value=0.0, value=100.0, step=0.1)
    with c3:
        Z = st.number_input("Giá trị Z", min_value=0.0, value=108.883, step=0.1)

    if st.button("Chuyển sang sRGB", type="primary"):
        rgb_linear = colour.XYZ_to_sRGB(np.array([X, Y, Z], dtype=float) / 100.0)
        rgb_255 = rgb_linear * 255.0
        st.write("**Giá trị sRGB tính được (chưa giới hạn gamut):**")
        a, b, c = st.columns(3)
        a.metric("R", f"{rgb_255[0]:.2f}")
        b.metric("G", f"{rgb_255[1]:.2f}")
        c.metric("B", f"{rgb_255[2]:.2f}")
        clipped = np.clip(rgb_255, 0, 255).round().astype(int)
        st.caption(f"Mã RGB 8-bit sau khi giới hạn: rgb({clipped[0]}, {clipped[1]}, {clipped[2]}).")
        if np.any((rgb_255 < 0) | (rgb_255 > 255)):
            st.warning("Một hoặc nhiều kênh nằm ngoài gamut sRGB trước khi giới hạn.")
