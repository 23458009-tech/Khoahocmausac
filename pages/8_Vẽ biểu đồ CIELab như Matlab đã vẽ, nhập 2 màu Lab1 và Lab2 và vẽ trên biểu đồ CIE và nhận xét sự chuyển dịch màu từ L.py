
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import colour

st.set_page_config(
    page_title="CIELAB Color Shift",
    layout="wide"
)

st.title("PHÂN TÍCH CHUYỂN DỊCH MÀU CIELAB")

st.write(
    "Nhập hai bộ giá trị Lab1 và Lab2 để xác định "
    "sự chuyển dịch màu trên biểu đồ CIE 1931."
)

# Điểm trắng D50
white_XYZ = np.array([96.31, 100.00, 82.41])

white_xy = colour.XYZ_to_xy(white_XYZ)

# Hàm chuyển Lab sang XYZ và xy
def lab_to_xy(Lab):

    XYZ = colour.Lab_to_XYZ(
        np.array(Lab),
        illuminant=white_xy
    )

    xy = colour.XYZ_to_xy(XYZ)

    return XYZ, xy


# Nhập dữ liệu Lab1 và Lab2
col1, col2 = st.columns(2)

with col1:

    st.subheader("MÀU LAB1")

    L1 = st.number_input("L1", value=57.99)
    a1 = st.number_input("a1", value=56.78)
    b1 = st.number_input("b1", value=58.57)

with col2:

    st.subheader("MÀU LAB2")

    L2 = st.number_input("L2", value=60.00)
    a2 = st.number_input("a2", value=45.00)
    b2 = st.number_input("b2", value=40.00)


if st.button("VẼ BIỂU ĐỒ CIE"):

    Lab1 = [L1, a1, b1]
    Lab2 = [L2, a2, b2]

    # Chuyển đổi tọa độ
    XYZ1, xy1 = lab_to_xy(Lab1)
    XYZ2, xy2 = lab_to_xy(Lab2)

    # Vẽ biểu đồ CIE
    fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(
        show_diagram_colours=True,
        show_spectral_locus=True,
        show=False,
        bounding_box=(0, 0.8, 0, 0.9)
    )

    # Điểm Lab1
    ax.scatter(
        xy1[0], xy1[1],
        color="red",
        s=120,
        edgecolors="black",
        label="Lab1"
    )

    # Điểm Lab2
    ax.scatter(
        xy2[0], xy2[1],
        color="blue",
        s=120,
        edgecolors="black",
        label="Lab2"
    )

    # Mũi tên chuyển dịch
    ax.annotate(
        "",
        xy=xy2,
        xytext=xy1,
        arrowprops=dict(
            arrowstyle="->",
            color="black",
            linewidth=2
        )
    )

    ax.set_title("CIE 1931 - Color Shift Lab1 to Lab2")

    ax.set_xlabel("CIE x")
    ax.set_ylabel("CIE y")

    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)

    plt.close(fig)

    # Tính Delta E CIE76
    delta_E = np.linalg.norm(
        np.array(Lab2) - np.array(Lab1)
    )

    # Độ thay đổi tọa độ
    dL = L2 - L1
    da = a2 - a1
    db = b2 - b1

    st.subheader("KẾT QUẢ PHÂN TÍCH")

    st.write("**Lab1:**", Lab1)
    st.write("**Lab2:**", Lab2)

    st.write("**XYZ1:**", XYZ1)
    st.write("**XYZ2:**", XYZ2)

    st.write("**Tọa độ xy Lab1:**", xy1)
    st.write("**Tọa độ xy Lab2:**", xy2)

    st.metric("Delta E CIE76", f"{delta_E:.3f}")

    st.write("### Nhận xét")

    if dL > 0:
        st.write("- Lab2 sáng hơn Lab1.")
    elif dL < 0:
        st.write("- Lab2 tối hơn Lab1.")
    else:
        st.write("- Độ sáng không thay đổi.")

    if da > 0:
        st.write("- Màu dịch chuyển về phía đỏ.")
    elif da < 0:
        st.write("- Màu dịch chuyển về phía xanh lá.")

    if db > 0:
        st.write("- Màu dịch chuyển về phía vàng.")
    elif db < 0:
        st.write("- Màu dịch chuyển về phía xanh lam.")

    st.write(f"- Độ sai khác màu Delta E = {delta_E:.3f}")
