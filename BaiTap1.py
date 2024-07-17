import tkinter as tk

def start_recording():
    status_label.config(text="Đang ghi lại...")

def pause_recording():
    status_label.config(text="Ghi lại tạm dừng.")

def end_recording():
    status_label.config(text="Kết thúc ghi lại.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ghi lại khung hình")
root.geometry("600x300")
root.configure(bg="#00FF00")  # Màu nền tùy chỉnh

# Nhãn tiêu đề
title_label = tk.Label(root, text="Ghi lại khung hình", font=("Arial", 24), bg="#00FF00")
title_label.pack(pady=20)

# Nhãn FPS
fps_label = tk.Label(root, text="FPS:", font=("Arial", 14), bg="#00FF00")
fps_label.pack()
fps_entry = tk.Entry(root, font=("Arial", 14))
fps_entry.pack(pady=10)

# Nhãn trạng thái
status_label = tk.Label(root, text="Sẵn sàng...", font=("Arial", 14), bg="#00FF00")
status_label.pack(pady=20)

# Các nút điều khiển
button_frame = tk.Frame(root, bg="#00FF00")
button_frame.pack(pady=10)

pause_button = tk.Button(button_frame, text="Tạm dừng", font=("Arial", 14), command=pause_recording)
pause_button.grid(row=0, column=0, padx=10)

start_button = tk.Button(button_frame, text="Bắt đầu", font=("Arial", 14), command=start_recording)
start_button.grid(row=0, column=1, padx=10)

end_button = tk.Button(button_frame, text="Kết thúc", font=("Arial", 14), command=end_recording)
end_button.grid(row=0, column=2, padx=10)

# Chạy vòng lặp chính của Tkinter
root.mainloop()
