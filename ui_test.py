import threading
import tkinter
import tkinter as tk
from tkinter import ttk

import sv_ttk

def ui_thread():
    # Create the main window
    root = tkinter.Tk()
    root.title("UI Example")

    # 设置窗口自适应大小
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # 创建Checkbuttons框架
    checkbuttons_frame = ttk.LabelFrame(root, text="Checkbuttons")
    checkbuttons_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # 添加Checkbuttons
    checkbutton_options = ["Europe", "France", "Germany", "Froland"]
    checkbutton_states = [tk.BooleanVar() for _ in checkbutton_options]
    checkbutton_states[2].set(True)  # 将Germany设为选中状态
    for i, option in enumerate(checkbutton_options):
        ttk.Checkbutton(checkbuttons_frame, text=option, variable=checkbutton_states[i]).grid(row=i, column=0, sticky="w")

    # 创建Radiobuttons框架
    radiobuttons_frame = ttk.LabelFrame(root, text="Radiobuttons")
    radiobuttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # 添加Radiobuttons
    radiobutton_options = ["Dog", "Cat", "Neither"]
    radiobutton_state = tk.StringVar(value="Dog")  # 将Dog设为选中状态
    for i, option in enumerate(radiobutton_options):
        ttk.Radiobutton(radiobuttons_frame, text=option, value=option, variable=radiobutton_state).grid(row=i, column=0, sticky="w")

    # 创建中间部分
    middle_frame = ttk.Frame(root)
    middle_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

    # 添加Entry控件
    entry1 = ttk.Entry(middle_frame)
    entry1.insert(0, "3.14")
    entry1.grid(row=0, column=0, pady=5, sticky="ew")

    entry2 = ttk.Entry(middle_frame)
    entry2.insert(0, "Lorem")
    entry2.grid(row=1, column=0, pady=5, sticky="ew")

    entry3 = ttk.Entry(middle_frame)
    entry3.insert(0, "Ipsum")
    entry3.grid(row=2, column=0, pady=5, sticky="ew")

    # 添加Combobox
    combobox = ttk.Combobox(middle_frame, values=["Python", "Java", "C++"])
    combobox.set("Python")
    combobox.grid(row=3, column=0, pady=5, sticky="ew")

    # 添加按钮
    button1 = ttk.Button(middle_frame, text="Click me!")
    button1.grid(row=4, column=0, pady=5, sticky="ew")

    button2 = ttk.Button(middle_frame, text="I love it!", style="Accent.TButton")
    button2.grid(row=5, column=0, pady=5, sticky="ew")

    # 添加Toggle开关
    toggle_switch = ttk.Checkbutton(middle_frame, text="Toggle me!", style="Switch.TCheckbutton")
    toggle_switch.grid(row=6, column=0, pady=5, sticky="ew")

    # 创建右侧部分
    right_frame = ttk.Frame(root)
    right_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

    # 添加Listbox
    listbox = tk.Listbox(right_frame)
    listbox_items = ["Kali 2013 Rolling", "Ubuntu 2004 Fixed", "Mint 2010 Semi-rolling"]
    for item in listbox_items:
        listbox.insert(tk.END, item)
    listbox.grid(row=0, column=0, pady=5, sticky="nsew")

    # 添加Notebook（标签页）
    notebook = ttk.Notebook(right_frame)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    tab3 = ttk.Frame(notebook)
    notebook.add(tab1, text="Tab1")
    notebook.add(tab2, text="Tab2")
    notebook.add(tab3, text="Tab3")
    notebook.grid(row=1, column=0, pady=5, sticky="nsew")

    # 添加Scale（滑块）
    scale = ttk.Scale(right_frame, from_=0, to=1, orient="horizontal")
    scale.set(1)  # 设为Dark theme
    scale.grid(row=2, column=0, pady=5, sticky="ew")

    # 设置右侧部分自适应大小
    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)

    # This is where the magic happens
    sv_ttk.set_theme("light")  # or "dark"

    root.mainloop()

if __name__ == "__main__":
    ui_thread = threading.Thread(target=ui_thread)
    ui_thread.start()
