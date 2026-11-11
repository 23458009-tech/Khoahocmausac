import streamlit as st
import pandas as pd
import numpy as np
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header("Tính giá trị 3 thành phần", "Đọc phổ phản xạ từ CSV và tính các giá trị kích thích màu CIE XYZ.")

uploaded = st.file_uploader("Tải tệp CSV phổ phản xạ", type=["csv"])

if uploaded is not None:
    try:
        df = pd.read_csv(uploaded, header=None)
        if df.shape[1] < 2:
            st.error("CSV cần tối thiểu 2 cột: bước sóng và giá trị phổ.")
            st.stop()
        data = df.iloc[:, :2].copy()
        data.columns = ["Wavelength", "Value"]
        data["Wavelength"] = pd.to_numeric(data["Wavelength"], errors="raise")
        data["Value"] = pd.to_numeric(data["Value"], errors="raise")
        if len(data) < 2:
            st.error("CSV cần ít nhất 2 dòng dữ liệu.")
            st.stop()
        if data["Wavelength"].duplicated().any():
            st.error("Bước sóng trong CSV không được trùng nhau.")
            st.stop()
        if not np.isfinite(data.to_numpy(dtype=float)).all():
            st.error("CSV chứa giá trị không hữu hạn.")
            st.stop()

        st.subheader("Xem trước dữ liệu")
        st.dataframe(data.head(10), use_container_width=True)
        st.caption(f"Tổng số mẫu: {len(data)}")
        if st.button("Tính XYZ", type="primary"):
            spectral_data = dict(zip(data["Wavelength"].astype(int), data["Value"]))
            sd = colour.SpectralDistribution(spectral_data)
            cmfs = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
            illuminant = colour.SDS_ILLUMINANTS["D65"]
            xyz = colour.sd_to_XYZ(sd, cmfs, illuminant)
            c1, c2, c3 = st.columns(3)
            c1.metric("X", f"{xyz[0]:.3f}")
            c2.metric("Y", f"{xyz[1]:.3f}")
            c3.metric("Z", f"{xyz[2]:.3f}")
    except Exception as exc:
        st.error(f"Không thể đọc hoặc tính toán CSV: {exc}")
else:
    st.info("Tải lên CSV có cột thứ nhất là bước sóng (nm), cột thứ hai là giá trị phổ phản xạ.")
