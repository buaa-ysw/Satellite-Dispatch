import threading
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

import sv_ttk
import ctypes
import ctypes
import tkinter as tk

def ui_thread():
    #告诉操作系统使用程序自身的dpi适配
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    #获取屏幕的缩放因子
    ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
    # Create the main window
    root = tk.Tk()
    #设置程序缩放
    root.tk.call('tk', 'scaling', ScaleFactor/75)
    root.title("UI Example")
    root.geometry("1500x900")
    # 设置窗口自适应大小
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create the top frame
    top_frame = tk.Frame(root, bg="blue")
    top_frame.grid(row=0, column=0, sticky="nsew")

    # Create the bottom frame
    bottom_frame = tk.Frame(root)
    bottom_frame.grid(row=1, column=0, sticky="nsew")

    # Configure grid weights for resizing
    root.grid_rowconfigure(0, weight=10)
    root.grid_rowconfigure(1, weight=90)
    root.grid_columnconfigure(0, weight=1)

    # This is where the magic happens
    sv_ttk.set_theme("light")  # or "dark"

    root.mainloop()

if __name__ == "__main__":
    ui_thread = threading.Thread(target=ui_thread)
    ui_thread.start()
