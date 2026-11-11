import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header(
    "Phân tích chuyển dịch màu CIELAB",
    "Nhập hai bộ Lab để chuyển đổi sang tọa độ xy và phân tích chênh lệch màu."
)

white_xyz = np.array([96.31, 100.00, 82.41])
white_xy = colour.XYZ_to_xy(white_xyz)

def lab_to_xy(lab):
    xyz = colour.Lab_to_XYZ(np.asarray(lab, dtype=float), illuminant=white_xy)
    xy = colour.XYZ_to_xy(xyz)
    return xyz, xy

c1, c2 = st.columns(2)
with c1:
    st.subheader("MÀU LAB1")
    L1 = st.number_input("L1", 0.0, 100.0, 57.99, 0.1)
    a1 = st.number_input("a1", -128.0, 127.0, 56.78, 0.1)
    b1 = st.number_input("b1", -128.0, 127.0, 58.57, 0.1)
with c2:
    st.subheader("MÀU LAB2")
    L2 = st.number_input("L2", 0.0, 100.0, 60.00, 0.1)
    a2 = st.number_input("a2", -128.0, 127.0, 45.00, 0.1)
    b2 = st.number_input("b2", -128.0, 127.0, 40.00, 0.1)

if st.button("Vẽ biểu đồ CIE và phân tích", type="primary"):
    lab1 = [L1, a1, b1]
    lab2 = [L2, a2, b2]
    xyz1, xy1 = lab_to_xy(lab1)
    xyz2, xy2 = lab_to_xy(lab2)

    fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(
        show_diagram_colours=True,
        show_spectral_locus=True,
        show=False,
        bounding_box=(0, 0.8, 0, 0.9),
    )
    ax.scatter(*xy1, color="red", s=120, edgecolors="black", label="Lab1", zorder=5)
    ax.scatter(*xy2, color="blue", s=120, edgecolors="black", label="Lab2", zorder=5)
    ax.annotate(
        "", xy=xy2, xytext=xy1,
        arrowprops={"arrowstyle": "->", "color": "black", "linewidth": 2},
    )
    ax.set_title("CIE 1931 – Color Shift from Lab1 to Lab2")
    ax.set_xlabel("CIE x")
    ax.set_ylabel("CIE y")
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    delta = np.asarray(lab2) - np.asarray(lab1)
    delta_e = float(np.linalg.norm(delta))
    dL, da, db = delta

    st.subheader("KẾT QUẢ PHÂN TÍCH")
    st.write("**Lab1:**", lab1)
    st.write("**Lab2:**", lab2)
    st.write("**XYZ1:**", xyz1)
    st.write("**XYZ2:**", xyz2)
    st.write("**Tọa độ xy Lab1:**", xy1)
    st.write("**Tọa độ xy Lab2:**", xy2)
    st.metric("Delta E CIE76", f"{delta_e:.3f}")

    st.markdown("### Nhận xét")
    if dL > 0:
        st.write("- Lab2 sáng hơn Lab1.")
    elif dL < 0:
        st.write("- Lab2 tối hơn Lab1.")
    else:
        st.write("- Độ sáng không thay đổi.")

    if da > 0:
        st.write("- Thành phần a* tăng: màu dịch chuyển về phía đỏ.")
    elif da < 0:
        st.write("- Thành phần a* giảm: màu dịch chuyển về phía xanh lá.")
    else:
        st.write("- Thành phần a* không thay đổi.")

    if db > 0:
        st.write("- Thành phần b* tăng: màu dịch chuyển về phía vàng.")
    elif db < 0:
        st.write("- Thành phần b* giảm: màu dịch chuyển về phía xanh lam.")
    else:
        st.write("- Thành phần b* không thay đổi.")

    st.write(f"- Độ sai khác màu theo công thức CIE76: ΔE*ab = {delta_e:.3f}.")
