import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header(
    "Vẽ gamut màu của thiết bị in",
    "Tải CSV chứa tọa độ Lab của các màu R, Y, G, C, B, M để dựng đa giác gamut."
)

required = ["R", "Y", "G", "C", "B", "M"]
uploaded = st.file_uploader("Tải CSV gamut màu thiết bị in", type=["csv"])

if uploaded is None:
    st.info("CSV cần có cột ColorSpace và sáu cột R, Y, G, C, B, M. Mỗi cột màu chứa 3 thành phần L*, a*, b*.")
else:
    try:
        df = pd.read_csv(uploaded)
        if "ColorSpace" not in df.columns:
            st.error("Không tìm thấy cột ColorSpace.")
            st.stop()
        missing = [c for c in required if c not in df.columns]
        if missing:
            st.error("CSV thiếu các cột: " + ", ".join(missing))
            st.stop()

        df = df.set_index("ColorSpace")
        st.subheader("Dữ liệu CSV")
        st.dataframe(df, use_container_width=True)

        if len(df) != 3:
            st.warning(
                f"CSV hiện có {len(df)} dòng. Mỗi màu cần đúng 3 dòng L*, a*, b* "
                "theo cấu trúc dữ liệu của chương trình."
            )
        if st.button("Vẽ gamut", type="primary"):
            fig, ax = colour.plotting.plot_chromaticity_diagram_CIE1931(show=False)
            ax.set_xlim([-0.1, 0.85])
            ax.set_ylim([-0.1, 0.90])
            ax.set_title("CIE 1931 Chromaticity Diagram – Printer Gamut")

            order = ["R", "Y", "G", "C", "B", "M", "R"]
            coords = {}
            for name in required:
                lab = pd.to_numeric(df[name], errors="raise").to_numpy(dtype=float)
                if lab.shape != (3,):
                    raise ValueError(f"Cột {name} phải có đúng 3 giá trị L*, a*, b*.")
                xyz = colour.Lab_to_XYZ(lab)
                xy = colour.XYZ_to_xy(xyz)
                coords[name] = xy

            polygon = np.array([coords[name] for name in order])
            ax.plot(polygon[:, 0], polygon[:, 1], "-o", color="#111111",
                    linewidth=2, markersize=6, label="Printer gamut")
            for name in required:
                ax.annotate(name, coords[name], xytext=(5, 5),
                            textcoords="offset points", fontsize=10)
            ax.legend()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)
    except Exception as exc:
        st.error(f"Không thể xử lý CSV gamut: {exc}")
