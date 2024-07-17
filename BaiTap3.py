import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Form Nhập Dữ Liệu")
root.geometry("500x400")

# Khung thông tin người dùng
user_info_frame = ttk.LabelFrame(root, text="Thông Tin Người Dùng")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# Các nhãn và ô nhập cho thông tin người dùng
ttk.Label(user_info_frame, text="Tên").grid(row=0, column=0, padx=5, pady=5)
ttk.Entry(user_info_frame).grid(row=1, column=0, padx=5, pady=5)

ttk.Label(user_info_frame, text="Họ").grid(row=0, column=1, padx=5, pady=5)
ttk.Entry(user_info_frame).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(user_info_frame, text="Chức danh").grid(row=0, column=2, padx=5, pady=5)
ttk.Combobox(user_info_frame, values=["Ông", "Bà", "Tiến sĩ", "Giáo sư"]).grid(row=1, column=2, padx=5, pady=5)

ttk.Label(user_info_frame, text="Tuổi").grid(row=2, column=0, padx=5, pady=5)
ttk.Spinbox(user_info_frame, from_=18, to=100).grid(row=3, column=0, padx=5, pady=5)

ttk.Label(user_info_frame, text="Quốc tịch").grid(row=2, column=1, padx=5, pady=5)
ttk.Entry(user_info_frame).grid(row=3, column=1, padx=5, pady=5)

# Khung trạng thái đăng ký
registration_frame = ttk.LabelFrame(root, text="Trạng Thái Đăng Ký")
registration_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

# Hộp kiểm và các hộp quay số cho trạng thái đăng ký
ttk.Checkbutton(registration_frame, text="Đã đăng ký").grid(row=0, column=0, padx=5, pady=5)

ttk.Label(registration_frame, text="Số khóa học đã hoàn thành").grid(row=1, column=0, padx=5, pady=5)
ttk.Spinbox(registration_frame, from_=0, to=50).grid(row=1, column=1, padx=5, pady=5)

ttk.Label(registration_frame, text="Số học kỳ").grid(row=1, column=2, padx=5, pady=5)
ttk.Spinbox(registration_frame, from_=0, to=20).grid(row=1, column=3, padx=5, pady=5)

# Khung điều khoản và điều kiện
terms_frame = ttk.LabelFrame(root, text="Điều Khoản & Điều Kiện")
terms_frame.grid(row=2, column=0, sticky="ew", padx=20, pady=10)

# Hộp kiểm điều khoản và điều kiện
ttk.Checkbutton(terms_frame, text="Tôi chấp nhận các điều khoản và điều kiện.").grid(row=0, column=0, padx=5, pady=5)

# Nút gửi
ttk.Button(root, text="Nhập dữ liệu").grid(row=3, column=0, pady=20)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
