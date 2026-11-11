import streamlit as st
import matplotlib.pyplot as plt
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header(
    "Vẽ biểu đồ CIE dạng band",
    "Biểu diễn biểu đồ sắc độ CIE 1931 với phạm vi bước sóng từ 400 nm đến 700 nm."
)

cmfs = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
cmfs_band = cmfs.copy().align(colour.SpectralShape(400, 700, 1))

fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(
    cmfs=cmfs_band,
    show_diagram_colours=True,
    show_spectral_locus=True,
    show=False,
    bounding_box=(0, 0.8, 0, 0.9),
)
ax.set_title("CIE 1931 Chromaticity Diagram (400–700 nm)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(alpha=0.3)
st.pyplot(fig, use_container_width=True)
plt.close(fig)
