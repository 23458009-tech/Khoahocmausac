import math
import streamlit as st
from utils.ui import apply_theme, asset_url

st.set_page_config(
    page_title="Khoa học Màu sắc | HCMUTE",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

with st.sidebar:
    st.markdown("## 🎨 Khoa học Màu sắc")
    st.caption("HCMUTE · Faculty of Arts & Media")
    st.divider()
    st.markdown(
        """
        **Hướng dẫn sử dụng**
        1. Chọn chức năng ở danh sách phía trên.
        2. Chuẩn bị dữ liệu CSV hoặc MAT nếu trang yêu cầu.
        3. Nhập thông số và nhấn nút tính toán / vẽ biểu đồ.
        """
    )
    st.divider()
    st.caption("Project học phần Khoa học Màu sắc")


def polar_point(cx, cy, radius, angle_deg):
    angle = math.radians(angle_deg - 90)
    return cx + radius * math.cos(angle), cy + radius * math.sin(angle)


def color_wheel_svg(harmony_name, angles, wheel_id):
    """Tạo bánh xe 12 sắc độ, đường nối và điểm màu cho từng nguyên tắc phối màu."""
    cx = cy = 60
    radius = 53
    colors = [
        "#ff321f", "#ff681d", "#ff981b", "#ffc21a",
        "#f4e51b", "#a6d914", "#28b83b", "#00a99b",
        "#078ed0", "#354fc4", "#742dbb", "#c51c91",
    ]

    sectors = []
    for i, color in enumerate(colors):
        start = i * 30 - 15
        end = start + 30
        x1, y1 = polar_point(cx, cy, radius, start)
        x2, y2 = polar_point(cx, cy, radius, end)
        sectors.append(
            f'<path d="M {cx:.2f} {cy:.2f} L {x1:.2f} {y1:.2f} '
            f'A {radius} {radius} 0 0 1 {x2:.2f} {y2:.2f} Z" '
            f'fill="{color}" stroke="rgba(255,255,255,.18)" stroke-width=".5"/>'
        )

    points = [polar_point(cx, cy, radius - 3, a) for a in angles]
    if len(points) > 2:
        line_points = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
        connector = (
            f'<polygon points="{line_points}" fill="none" '
            f'stroke="#253746" stroke-width="1.8" stroke-linejoin="round"/>'
        )
    elif len(points) == 2:
        connector = (
            f'<line x1="{points[0][0]:.2f}" y1="{points[0][1]:.2f}" '
            f'x2="{points[1][0]:.2f}" y2="{points[1][1]:.2f}" '
            f'stroke="#253746" stroke-width="1.8"/>'
        )
    else:
        connector = ""

    markers = []
    for idx, (x, y) in enumerate(points):
        marker_color = colors[int(round((angles[idx] % 360) / 30)) % 12]
        markers.append(
            f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6.3" '
            f'fill="{marker_color}" stroke="#263746" stroke-width="1.5"/>'
        )

    return f"""
    <svg class="wheel-rotor" viewBox="0 0 120 120" role="img"
         aria-label="Bánh xe phối màu {harmony_name}">
      <g>
        {''.join(sectors)}
        <circle cx="60" cy="60" r="53" fill="none"
                stroke="rgba(20,50,80,.25)" stroke-width="1"/>
        {connector}
        {''.join(markers)}
      </g>
    </svg>
    """


# Trang chủ
logo_hcmute = asset_url("logo_hcmute.png")
logo_khoa = asset_url("logo_khoa.png")

missing = [
    name for name, url in [
        ("logo_hcmute.png", logo_hcmute),
        ("logo_khoa.png", logo_khoa),
    ] if not url
]
if missing:
    st.error("Không tìm thấy hình ảnh trong thư mục static/: " + ", ".join(missing))
    st.stop()

harmony_wheels = [
    ("PRIMARY", [0, 120, 240]),
    ("ANALOGOUS", [-30, 0, 30]),
    ("SECONDARY", [60, 180, 300]),
    ("COMPLEMENTARY", [45, 225]),
    ("SQUARE", [45, 135, 225, 315]),
    ("SPLIT COMPLEMENTARY", [0, 150, 210]),
]

wheel_cards = []
for index, (label, angles) in enumerate(harmony_wheels):
    wheel_cards.append(
        f"""
        <div class="harmony-item">
          <div class="harmony-label">{label}</div>
          <div class="harmony-wheel wheel-speed-{index + 1}">
            {color_wheel_svg(label, angles, index)}
          </div>
        </div>
        """
    )

st.markdown(
    f"""
    <style>
      .harmony-section {{
        width: min(1050px, 98%);
        margin: 34px auto 0;
        padding: 22px 28px 26px;
        border-radius: 24px;
        background: rgba(232,247,255,.48);
        border: 1px solid rgba(255,255,255,.55);
        box-shadow: inset 0 1px 14px rgba(255,255,255,.22);
      }}
      .harmony-heading {{
        text-align: center;
        color: #0754a5;
        font-size: clamp(15px, 1.4vw, 19px);
        font-weight: 800;
        letter-spacing: 2px;
        margin: 0 0 12px;
        text-shadow: 0 1px 2px rgba(255,255,255,.9);
      }}
      .harmony-grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 20px 28px;
        align-items: center;
        justify-items: center;
      }}
      .harmony-item {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 9px;
        min-width: 0;
      }}
      .harmony-label {{
        color: #637487;
        font-size: clamp(11px, 1vw, 14px);
        font-weight: 800;
        letter-spacing: .5px;
        text-align: center;
      }}
      .harmony-wheel {{
        width: clamp(105px, 10vw, 150px);
        aspect-ratio: 1;
        display: grid;
        place-items: center;
        filter: drop-shadow(0 3px 4px rgba(0,60,120,.16));
      }}
      .wheel-rotor {{
        display: block;
        width: 100%;
        height: 100%;
        transform-origin: 50% 50%;
        animation: colorWheelSpin 24s linear infinite;
      }}
      .wheel-speed-2 .wheel-rotor {{ animation-duration: 30s; animation-direction: reverse; }}
      .wheel-speed-3 .wheel-rotor {{ animation-duration: 27s; }}
      .wheel-speed-4 .wheel-rotor {{ animation-duration: 34s; animation-direction: reverse; }}
      .wheel-speed-5 .wheel-rotor {{ animation-duration: 29s; }}
      .wheel-speed-6 .wheel-rotor {{ animation-duration: 37s; animation-direction: reverse; }}
      @keyframes colorWheelSpin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      @media (max-width: 700px) {{
        .harmony-section {{ width: 100%; padding: 16px 10px; margin-top: 22px; }}
        .harmony-grid {{ gap: 10px 5px; }}
        .harmony-wheel {{ width: clamp(88px, 23vw, 125px); }}
        .harmony-label {{ font-size: 9px; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .wheel-rotor {{ animation: none !important; }}
      }}
    </style>

    <div class="home-wrap">
      <section class="home-card">
        <img src="{logo_hcmute}" class="school-logo" alt="Logo HCMUTE">
        <img src="{logo_khoa}" class="faculty-logo" alt="Faculty of Arts and Media">
        <div class="faculty-title">KHOA MỸ THUẬT VÀ TRUYỀN THÔNG</div>
        <div class="welcome-title">
          Chào mừng bạn đến với project Khoa học Màu sắc của mình!
        </div>
        <div class="student-title">
          Mình tên là Nguyễn Hoàng Khiêm, MSSV: 23458009
        </div>

        <section class="harmony-section" aria-label="Các nguyên tắc phối màu">
          <div class="harmony-heading">COLOR HARMONY · NGUYÊN TẮC PHỐI MÀU</div>
          <div class="harmony-grid">
            {''.join(wheel_cards)}
          </div>
        </section>
      </section>
    </div>
    """,
    unsafe_allow_html=True,
)
