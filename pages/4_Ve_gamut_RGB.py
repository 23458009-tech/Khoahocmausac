import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import colour
from ui_helpers import apply_theme, page_header

apply_theme()
page_header("Vẽ gamut màu của thiết bị RGB", "Minh họa gamut sRGB trên biểu đồ sắc độ CIE 1931.")

fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(show=False)
ax.set_xlim([-0.1, 0.85])
ax.set_ylim([-0.1, 0.90])
ax.set_title("CIE 1931 Chromaticity Diagram – sRGB Gamut")

rgb_primaries = {
    "R": np.array([1.0, 0.0, 0.0]),
    "G": np.array([0.0, 1.0, 0.0]),
    "B": np.array([0.0, 0.0, 1.0]),
}
xy_points = {}
for name, rgb in rgb_primaries.items():
    xyz = colour.sRGB_to_XYZ(rgb)
    xy_points[name] = colour.XYZ_to_xy(xyz)

triangle = np.array([
    xy_points["R"],
    xy_points["G"],
    xy_points["B"],
    xy_points["R"],
])
ax.plot(triangle[:, 0], triangle[:, 1], color="black", linewidth=2.2, label="sRGB gamut")
for name, xy in xy_points.items():
    ax.scatter(xy[0], xy[1], s=65, label=f"Primary {name}")
ax.legend()
st.pyplot(fig, use_container_width=True)
plt.close(fig)
