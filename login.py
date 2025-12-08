import tkinter as tk
from tkinter import messagebox

# --- Cơ sở dữ liệu "giả" ---
# Dùng một dictionary để lưu trữ {username: password}
# Chúng ta thêm 'admin' vào làm tài khoản gốc
user_database = {
    "admin": "123"
}

# --- Hàm xử lý cho Cửa Sổ Đăng Ký ---

def handle_register_submit(username_entry, pass_entry, confirm_pass_entry, window_to_close):
    """Hàm này được gọi khi bấm 'Xác nhận' trên form đăng ký"""
    username = username_entry.get()
    password = pass_entry.get()
    confirm_password = confirm_pass_entry.get()

    # --- Bắt lỗi (Validate) ---
    if not username or not password or not confirm_password:
        messagebox.showerror("Lỗi Đăng Ký", "Không được để trống bất kỳ ô nào!", parent=window_to_close)
        return

    if password != confirm_password:
        messagebox.showerror("Lỗi Đăng Ký", "Mật khẩu xác nhận không khớp!", parent=window_to_close)
        return

    if username in user_database:
        messagebox.showerror("Lỗi Đăng Ký", f"Tên tài khoản '{username}' đã tồn tại!", parent=window_to_close)
        return
        
    # --- Đăng ký thành công ---
    user_database[username] = password
    messagebox.showinfo("Thành Công", f"Đã đăng ký thành công tài khoản: {username}", parent=window_to_close)
    print(f"Cơ sở dữ liệu người dùng đã cập nhật: {user_database}") # In ra terminal để kiểm tra
    window_to_close.destroy() # Đóng cửa sổ đăng ký

def open_register_window():
    """Mở ra một cửa sổ Toplevel (cửa sổ con) để đăng ký"""
    
    # Tạo cửa sổ mới (Toplevel)
    register_window = tk.Toplevel(window)
    register_window.title("Đăng Ký Tài Khoản Mới")
    register_window.geometry("400x250")
    register_window.configure(bg="#f0f0f0") # Màu nền xám nhạt
    
    # Giữ cửa sổ này ở trên cùng và chặn tương tác với cửa sổ chính
    register_window.transient(window)
    register_window.grab_set()
    
    # Tạo khung
    reg_frame = tk.Frame(register_window, bg="#f0f0f0")
    reg_frame.pack(pady=20, padx=20)

    # 1. Tên tài khoản mới
    lbl_new_user = tk.Label(reg_frame, text="Tên tài khoản:", bg="#f0f0f0", font=("Arial", 11))
    lbl_new_user.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_new_user = tk.Entry(reg_frame, width=30, font=("Arial", 11))
    entry_new_user.grid(row=0, column=1, padx=10, pady=10)

    # 2. Mật khẩu mới
    lbl_new_pass = tk.Label(reg_frame, text="Mật khẩu:", bg="#f0f0f0", font=("Arial", 11))
    lbl_new_pass.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_new_pass = tk.Entry(reg_frame, width=30, font=("Arial", 11), show="*")
    entry_new_pass.grid(row=1, column=1, padx=10, pady=10)

    # 3. Xác nhận mật khẩu
    lbl_confirm_pass = tk.Label(reg_frame, text="Xác nhận MK:", bg="#f0f0f0", font=("Arial", 11))
    lbl_confirm_pass.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_confirm_pass = tk.Entry(reg_frame, width=30, font=("Arial", 11), show="*")
    entry_confirm_pass.grid(row=2, column=1, padx=10, pady=10)
    
    # 4. Nút Xác nhận Đăng ký
    # Chúng ta dùng 'lambda' để truyền tham số vào hàm handle_register_submit
    btn_submit_reg = tk.Button(reg_frame, text="Xác nhận", width=15, font=("Arial", 10), 
                               command=lambda: handle_register_submit(
                                   entry_new_user, 
                                   entry_new_pass, 
                                   entry_confirm_pass, 
                                   register_window
                               ))
    btn_submit_reg.grid(row=3, column=1, pady=20, sticky="e")


# --- Hàm xử lý cho Cửa Sổ Chính ---

def handle_login():
    """Hàm này được gọi khi bấm nút 'Đăng nhập'"""
    username = entry_username.get()
    password = entry_password.get()
    
    # --- LOGIC ĐĂNG NHẬP MỚI ---
    # 1. Kiểm tra xem username có trong database không
    if username in user_database:
        # 2. Nếu có, kiểm tra xem password có khớp không
        if user_database[username] == password:
            # ĐĂNG NHẬP THÀNH CÔNG
            messagebox.showinfo("Thông báo", f"Đăng nhập thành công! Chào mừng {username}")
            
            # Kích hoạt các nút menu
            menu_bar.entryconfig("Quản Lý Độc Giả", state="normal")
            menu_bar.entryconfig("Quản Lý Sách", state="normal")
            menu_bar.entryconfig("Quản Lý Tác Giả", state="normal")
            menu_bar.entryconfig("Quản Lý Mượn Trả", state="normal")
            system_menu.entryconfig("Đăng xuất", state="normal")
            system_menu.entryconfig("Đăng nhập", state="disabled")
            
            # Ẩn khung đăng nhập
            login_frame.place_forget()
        else:
            # Sai mật khẩu
            messagebox.showerror("Lỗi", "Mật khẩu không đúng!")
    else:
        # Sai tên tài khoản
        messagebox.showerror("Lỗi", "Tên tài khoản không tồn tại!")


def handle_exit():
    """Hàm này được gọi khi bấm nút 'Thoát'"""
    if messagebox.askokcancel("Xác nhận", "Bạn có chắc chắn muốn thoát?"):
        window.quit() # Đóng cửa sổ

# --- Cài đặt cửa sổ chính ---
window = tk.Tk()
window.title("Quản Lý Thư Viện - [Đăng Nhập]")
window.geometry("600x400") # Kích thước cửa sổ
window.configure(bg="#90EE90") # Màu nền xanh

# --- Tạo Menu Bar ---
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Menu "Hệ Thống"
system_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Hệ Thống", menu=system_menu)
system_menu.add_command(label="Đăng nhập", state="disabled") # Vô hiệu hóa vì đang ở màn hình đăng nhập
system_menu.add_command(label="Đăng ký", command=open_register_window) # Thêm nút đăng ký ở đây
system_menu.add_command(label="Đăng xuất", state="disabled") # Vô hiệu hóa khi chưa đăng nhập
system_menu.add_separator()
system_menu.add_command(label="Thoát", command=handle_exit) # Sửa lại để gọi hàm handle_exit

# Các menu khác (vô hiệu hóa cho đến khi đăng nhập)
menu_bar.add_command(label="Quản Lý Độc Giả", state="disabled")
menu_bar.add_command(label="Quản Lý Sách", state="disabled")
menu_bar.add_command(label="Quản Lý Tác Giả", state="disabled")
menu_bar.add_command(label="Quản Lý Mượn Trả", state="disabled")


# --- Tạo Khung (Frame) cho Form Đăng Nhập ---
login_frame = tk.Frame(window, bg="#90EE90") 
login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 1. Tên tài khoản
lbl_username = tk.Label(login_frame, text="Tên tài khoản:", bg="#90EE90", font=("Arial", 12))
lbl_username.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_username = tk.Entry(login_frame, width=30, font=("Arial", 12))
entry_username.grid(row=0, column=1, padx=10, pady=10)

# 2. Mật khẩu
lbl_password = tk.Label(login_frame, text="Mật khẩu:", bg="#90EE90", font=("Arial", 12))
lbl_password.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_password = tk.Entry(login_frame, width=30, font=("Arial", 12), show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# 3. Các nút bấm (Đăng nhập, Đăng ký, Thoát)
button_frame = tk.Frame(login_frame, bg="#90EE90")
button_frame.grid(row=2, column=1, pady=20, sticky="w") # Đặt dưới ô mật khẩu

btn_login = tk.Button(button_frame, text="Đăng nhập", width=10, font=("Arial", 10), command=handle_login)
btn_login.pack(side=tk.LEFT, padx=5)

# NÚT ĐĂNG KÝ MỚI
btn_register = tk.Button(button_frame, text="Đăng ký", width=10, font=("Arial", 10), command=open_register_window)
btn_register.pack(side=tk.LEFT, padx=5)

btn_exit = tk.Button(button_frame, text="Thoát", width=10, font=("Arial", 10), command=handle_exit)
btn_exit.pack(side=tk.LEFT, padx=5)

# --- Chạy ứng dụng ---
window.mainloop()