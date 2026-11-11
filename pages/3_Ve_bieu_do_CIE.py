import streamlit as st
import matplotlib.pyplot as plt
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header("Vẽ biểu đồ CIE 1931", "Biểu đồ sắc độ CIE 1931 – người quan sát chuẩn 2°.")

fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(show=False)
ax.set_xlim([-0.1, 0.85])
ax.set_ylim([-0.1, 0.90])
ax.set_title("CIE 1931 Chromaticity Diagram\n2 Degree Standard Observer")
st.pyplot(fig, use_container_width=True)
plt.close(fig)
