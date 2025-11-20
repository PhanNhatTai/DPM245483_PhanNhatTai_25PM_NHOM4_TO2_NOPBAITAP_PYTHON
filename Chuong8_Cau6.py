from tkinter import *

# 1. Khởi tạo cửa sổ
root = Tk()
root.title("frame 2") # Tên cửa sổ

# 2. Định nghĩa các kiểu relief và borderwidth
relief_styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]
border_widths = range(5) # borderwidth từ 0 đến 4

# Vòng lặp chính để tạo các hàng (rows)
for row_index, bw in enumerate(border_widths):
    # Tạo nhãn (Label) hiển thị giá trị borderwidth ở cột đầu tiên
    Label(root, text=f"borderwidth = {bw}", padx=10).grid(row=row_index, column=0, sticky=W)
    
    # Vòng lặp lồng nhau để tạo các nút (buttons) theo kiểu relief
    for col_index, relief_style in enumerate(relief_styles):
        
        # Chỉ định màu nền và viền đặc biệt cho kiểu "solid"
        if relief_style == "solid":
            # Ví dụ: Làm nổi bật nút "solid" với màu đen
            bg_color = "white"
            fg_color = "black"
        else:
            # Màu mặc định cho các nút khác
            bg_color = "SystemButtonFace" 
            fg_color = "black"

        # Tạo và đặt nút Button
        Button(
            root, 
            text=relief_style, 
            relief=relief_style, # Thiết lập kiểu viền
            borderwidth=bw,       # Thiết lập độ dày viền
            padx=10, 
            pady=5,
            bg=bg_color,
            fg=fg_color
        ).grid(row=row_index, column=col_index + 1, padx=5, pady=5) # column+1 vì cột 0 là Label

root.mainloop()