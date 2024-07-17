import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

def scan_now():
    status_label.config(text="Đang quét...", fg="#1E90FF")

def quick_scan():
    status_label.config(text="Quét nhanh đang chạy...", fg="#32CD32")

def web_protect():
    status_label.config(text="Bảo vệ web đã được kích hoạt.", fg="#FF4500")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Bảo mật")
root.geometry("900x600")
root.configure(bg="#F0F8FF")

# Tạo font tùy chỉnh
title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
subtitle_font = tkfont.Font(family="Helvetica", size=14)
button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Khung chính được chia làm hai phần: sidebar và main_content
sidebar = tk.Frame(root, width=250, bg="#4682B4", padx=15, pady=15)
sidebar.pack(expand=False, fill="y", side="left")
main_content = tk.Frame(root, bg="#F0F8FF", padx=30, pady=30)
main_content.pack(expand=True, fill="both", side="right")

# Thanh bên (sidebar)
logo_label = tk.Label(sidebar, text="🛡️", font=("Arial", 48), bg="#4682B4", fg="white")
logo_label.pack(pady=(20, 10))

status_label = tk.Label(sidebar, text="Trạng thái", font=button_font, bg="#4682B4", fg="white")
status_label.pack(pady=(10, 5))

update_label = tk.Label(sidebar, text="Đã cập nhật", font=subtitle_font, bg="#4682B4", fg="#E0FFFF")
update_label.pack(pady=(0, 20))

scan_button = ttk.Button(sidebar, text="Quét ngay", command=scan_now, style="Accent.TButton")
scan_button.pack(pady=10, fill="x")

# Khu vực chính (main_content)
title_label = tk.Label(main_content, text="Ứng dụng Bảo mật", font=title_font, bg="#F0F8FF", fg="#4682B4")
title_label.pack(pady=(0, 20))

subtitle_label = tk.Label(main_content, text="Bảo vệ máy tính của bạn với các tính năng bảo mật tiên tiến.", 
                          font=subtitle_font, bg="#F0F8FF", fg="#708090", wraplength=500)
subtitle_label.pack(pady=(0, 30))

button_frame = tk.Frame(main_content, bg="#F0F8FF")
button_frame.pack(fill="x", pady=20)

quick_scan_button = ttk.Button(button_frame, text="Quét nhanh", command=quick_scan, style="TButton")
quick_scan_button.pack(side="left", padx=(0, 10))

web_protect_button = ttk.Button(button_frame, text="Bảo vệ web", command=web_protect, style="TButton")
web_protect_button.pack(side="left")

# Nhãn trạng thái
status_label = tk.Label(main_content, text="Sẵn sàng...", font=subtitle_font, bg="#F0F8FF", fg="#708090")
status_label.pack(pady=30)

# Tùy chỉnh style cho các nút
style = ttk.Style()
style.configure("TButton", font=button_font, padding=10)
style.configure("Accent.TButton", background="#4682B4", foreground="white")

# Chạy vòng lặp chính của Tkinter
root.mainloop()