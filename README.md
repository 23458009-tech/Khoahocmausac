# Khoa học Màu sắc – HCMUTE

## Cấu trúc dự án
- `app.py`: Trang chủ HCMUTE.
- `pages/`: 8 trang chức năng.
- `utils/ui.py`: Giao diện dùng chung.
- `.streamlit/config.toml`: Cấu hình giao diện và Sidebar.
- `background_hcmute.png`: Ảnh nền.
- `logo_hcmute.png`: Logo trường.
- `logo_khoa.png`: Logo Faculty of Arts & Media.
- `halftone.mat`: Dữ liệu máy in nửa tông.

## Cài đặt và chạy trên Windows
Nên dùng Python 3.11 hoặc 3.12 để có độ tương thích thư viện tốt.

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Nếu máy đang dùng Python 3.13, có thể tạo môi trường bằng:
```bash
py -3.13 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

## Ghi chú
- Sidebar tự động lấy tên các trang từ thư mục `pages/`.
- Giữ nguyên thư mục `pages/`, `utils/` và các ảnh khi di chuyển dự án.
- Chức năng máy in nửa tông sử dụng `halftone.mat` nằm cạnh `app.py`.
- File MAT cần có `W` kích thước `(1, 31)` và `P` kích thước `(120, 31)`.
