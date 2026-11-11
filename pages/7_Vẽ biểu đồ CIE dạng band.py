
import streamlit as st
import matplotlib.pyplot as plt
import colour

st.set_page_config(
    page_title="CIE Band 400-700 nm",
    layout="wide"
)

st.title("BIỂU ĐỒ CIE 1931 – BAND 400–700 nm")

st.write(
    "Biểu diễn biểu đồ sắc độ CIE 1931 với "
    "phạm vi bước sóng từ 400 nm đến 700 nm."
)

# Lấy dữ liệu CIE 1931 2 Degree Standard Observer
cmfs = colour.MSDS_CMFS[
    "CIE 1931 2 Degree Standard Observer"
]

# Giới hạn bước sóng 400–700 nm
cmfs_band = cmfs.copy().align(
    colour.SpectralShape(400, 700, 1)
)

# Vẽ biểu đồ CIE
fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(
    cmfs=cmfs_band,
    show_diagram_colours=True,
    show_spectral_locus=True,
    show=False,
    bounding_box=(0, 0.8, 0, 0.9)
)

ax.set_title(
    "CIE 1931 Chromaticity Diagram (400–700 nm)",
    fontsize=14
)

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.grid(alpha=0.3)

st.pyplot(fig)

plt.close(fig)
