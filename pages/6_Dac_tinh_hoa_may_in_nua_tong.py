from pathlib import Path
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import scipy.io
import colour
from utils.ui import apply_theme, page_header

apply_theme()
page_header(
    "Đặc tính hóa của máy in nửa tông",
    "Phân tích trộn màu vàng và tím, phổ phản xạ và đường cong tái tạo tông."
)

data_path = Path(__file__).resolve().parents[1] / "halftone.mat"
if not data_path.is_file():
    st.error(
        "Không tìm thấy halftone.mat trong thư mục gốc của dự án. "
        "Hãy đặt file halftone.mat cạnh app.py để sử dụng chức năng này."
    )
    st.stop()

try:
    data = scipy.io.loadmat(str(data_path))
except Exception as exc:
    st.error(f"Không đọc được halftone.mat: {exc}")
    st.stop()

if "W" not in data or "P" not in data:
    st.error("File halftone.mat không có đủ hai biến W và P.")
    st.stop()

W = np.asarray(data["W"], dtype=float)
P = np.asarray(data["P"], dtype=float)

if W.shape != (1, 31) or P.shape != (120, 31):
    st.error(
        f"Dữ liệu không đúng kích thước: W={W.shape}, P={P.shape}. "
        "Yêu cầu W=(1, 31) và P=(120, 31)."
    )
    st.stop()

P = np.vstack((W, P))
yellow = P[:11, :]
magenta = np.zeros((11, 31), dtype=np.float64)
for i in range(11):
    magenta[i, :] = P[i * 11, :]

def convert_to_rgb(reflection, cmfs, illuminant):
    spectral = {400 + i * 10: float(value) for i, value in enumerate(reflection)}
    sd = colour.SpectralDistribution(spectral)
    xyz = colour.sd_to_XYZ(sd, cmfs, illuminant)
    rgb = colour.XYZ_to_sRGB(xyz / 100)
    return (np.clip(rgb, 0, 1) * 255).astype(np.uint8)

def get_trc(dig, reflectance, white, solid, exponent):
    reflectance = np.asarray(reflectance, dtype=float) ** (1 / exponent)
    white = np.asarray(white, dtype=float) ** (1 / exponent)
    solid = np.asarray(solid, dtype=float) ** (1 / exponent)
    denominator = np.sum((solid - white) ** 2)
    if denominator == 0:
        raise ValueError("Không thể tính đường cong: mẫu solid và white trùng nhau.")
    c = np.array([
        np.sum((solid - row) * (solid - white)) / denominator
        for row in reflectance
    ])
    c = 1 - c
    polynomial = np.polyfit(dig, c, 3)
    return c, polynomial

choice = st.radio(
    "Chọn nội dung phân tích",
    [
        "Ảnh trộn màu vàng và tím",
        "Phổ màu vàng và tím trên nền trắng",
        "Đường cong tái tạo tông màu vàng và tím",
        "Trộn hai màu vàng và tím",
    ],
)

if choice == "Ảnh trộn màu vàng và tím":
    cmfs = colour.MSDS_CMFS["CIE 1931 2 Degree Standard Observer"]
    illuminant = colour.SDS_ILLUMINANTS["D65"]
    size = 40
    image = np.zeros((size * 11, size * 11, 3), dtype=np.uint8)
    k = 0
    for row in range(11):
        for col in range(11):
            rgb = convert_to_rgb(P[k], cmfs, illuminant)
            image[row*size:(row+1)*size, col*size:(col+1)*size, :] = rgb
            k += 1
    image = image[::-1, :, :]
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(image)
    ticks = list(range(20, 440, 40))
    labels = [f"{v:.1f}" for v in np.linspace(0, 1, 11)]
    ax.set_xticks(ticks, labels)
    ax.set_yticks(ticks, labels[::-1])
    ax.set_xlabel("Yellow")
    ax.set_ylabel("Magenta")
    ax.set_title("Mix Yellow and Magenta Colors")
    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

elif choice == "Phổ màu vàng và tím trên nền trắng":
    wavelength = np.linspace(400, 700, 31)
    c1, c2 = st.columns(2)
    for column, spectra, color, title in [
        (c1, yellow, "#FF8000", "Phổ màu vàng trên nền trắng"),
        (c2, magenta, "#D000D0", "Phổ màu tím trên nền trắng"),
    ]:
        with column:
            fig, ax = plt.subplots(figsize=(5, 4))
            for row in spectra:
                ax.plot(wavelength, row, color=color, alpha=0.8)
            ax.set_xlim(400, 700)
            ax.set_ylim(0, 1)
            ax.set_xlabel("Bước sóng (nm)")
            ax.set_ylabel("Phổ phản xạ")
            ax.set_title(title + " (a = 0:0.1:1)")
            ax.grid(alpha=0.25)
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

elif choice == "Đường cong tái tạo tông màu vàng và tím":
    n = 20
    target = np.linspace(0, 1, 11)
    c1, c2 = st.columns(2)
    for column, spectra, color, title in [
        (c1, yellow, "#FF8000", "Đường cong tái tạo tông màu vàng"),
        (c2, magenta, "#D000D0", "Đường cong tái tạo tông màu tím"),
    ]:
        with column:
            actual, polynomial = get_trc(target, spectra, spectra[0, :], spectra[10, :], n)
            x_plot = np.linspace(0, 1, 101)
            y_plot = np.polyval(polynomial, x_plot)
            fig, ax = plt.subplots(figsize=(5, 4))
            ax.plot(target, actual, "o", color=color, label="Giá trị đo")
            ax.plot(x_plot, y_plot, color="black", label="Hồi quy bậc 3")
            ax.set_xlabel("Giá trị mục tiêu của a")
            ax.set_ylabel("Giá trị thực tế của a")
            ax.set_title(title)
            ax.grid(alpha=0.25)
            ax.legend()
            st.pyplot(fig, use_container_width=True)
            plt.close(fig)

else:
    c1, c2 = st.columns(2)
    with c1:
        a_mag_target = st.number_input("Mục tiêu a của màu tím", 0.0, 1.0, 0.5, 0.1)
    with c2:
        a_yel_target = st.number_input("Mục tiêu a của màu vàng", 0.0, 1.0, 0.5, 0.1)

    if st.button("Dự báo phổ phản xạ", type="primary"):
        mag_index = int(round(a_mag_target * 10))
        yel_index = int(round(a_yel_target * 10))
        measured_index = mag_index * 11 + yel_index
        measured = P[measured_index, :]

        n = 20
        target = np.linspace(0, 1, 11)
        _, p_mag = get_trc(target, magenta, magenta[0, :], magenta[10, :], n)
        _, p_yel = get_trc(target, yellow, yellow[0, :], yellow[10, :], n)
        a_mag_actual = float(np.polyval(p_mag, a_mag_target))
        a_yel_actual = float(np.polyval(p_yel, a_yel_target))

        Am = a_mag_actual * (1 - a_yel_actual)
        Ay = a_yel_actual * (1 - a_mag_actual)
        Aw = (1 - a_mag_actual) * (1 - a_yel_actual)
        Ao = a_mag_actual * a_yel_actual

        overlap = P[120, :]
        white = P[0, :]
        predicted = np.zeros(31, dtype=np.float64)
        for i in range(31):
            terms = (
                Am * (magenta[10, i] ** (1/n))
                + Ay * (yellow[10, i] ** (1/n))
                + Ao * (overlap[i] ** (1/n))
                + Aw * (white[i] ** (1/n))
            )
            predicted[i] = max(terms, 0) ** n

        wavelength = np.linspace(400, 700, 31)
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(wavelength, measured, "ro", label="Giá trị mục tiêu")
        ax.plot(wavelength, predicted, "b-", label="Giá trị dự báo")
        ax.set_ylim(0, 1)
        ax.set_xlabel("Bước sóng (nm)")
        ax.set_ylabel("Phổ phản xạ")
        ax.set_title(
            "Phổ phản xạ khi trộn màu tím và vàng\n"
            f"a_mag={a_mag_target:.1f}, a_yel={a_yel_target:.1f}"
        )
        ax.legend()
        ax.grid(alpha=0.25)
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
