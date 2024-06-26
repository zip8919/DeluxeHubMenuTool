import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import configparser
import time
import importlib
from PIL import Image
from functions import functions
from functools import partial

CONFIG = """[config]
output_file=menu.yml
language=zh_cn"""

functions = functions()
if functions.check_file("config.ini") == False:
    functions.crete("config.ini", CONFIG)
config = configparser.ConfigParser()
config.read('config.ini')
output_file = config.get('config', 'output_file')
language = config.get('config', 'language')
message = importlib.import_module("message")
class_obj = getattr(message, f"message_{language}")
lang = class_obj()

#打开图片
def open_image(file):
    if functions.check_file(file) == False:
        messagebox.showwarning(lang.message("warn"), file + lang.message("nofound"))
    else:
        image = Image.open(file)
        image.show()

def window():
    #保存
    def save_to_file():
        name = name_entry.get() + "_random-" + str(random.randint(10000, 99999)) or "name" + str(random.randint(10000, 99999))
        material = material_entry.get() or "book"
        slot = slot_entry.get() or "0"
        amount = amount_entry.get() or "1"
        glow = glow_var.get() or "true"
        display_name = display_name_entry.get() or "display name"
        lore = lore_text.get("1.0", "end-1c")
        lore = "\n".join(["      - '" + line.strip() + "'" for line in lore.splitlines() if line.strip()])
        actions = actions_text.get("1.0", "end-1c")
        actions = "\n".join(["      - '" + line.strip() + "'" for line in actions.splitlines() if line.strip()])
    
        output = f"""
  {name}:
    material: {material}
    slot: {slot}
    amount: {amount}
    glow: {glow}
    display_name: '{display_name}'
    lore:
{lore}
    actions:
{actions}"""

        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(output)
        messagebox.showinfo((lang.message("savesuccess")), ("[" + time.strftime('%H:%M:%S', time.localtime()) + "]" +lang.message("saveto") + output_file))
        
    # 创建窗口
    root = tk.Tk()
    root.title(lang.message("title"))
    root.geometry("520x500")

    # 添加标签和文本框
    tk.Label(root, text=lang.message("name")).pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text=lang.message("material")).pack()
    material_entry = tk.Entry(root)
    material_entry.pack()

    tk.Label(root, text=lang.message("slot")).pack()
    slot_entry = tk.Entry(root)
    slot_entry.pack()

    tk.Label(root, text=lang.message("amount")).pack()
    amount_entry = tk.Entry(root)
    amount_entry.pack()

    glow_var = tk.BooleanVar()
    glow_check = tk.Checkbutton(root, text=lang.message("glow"), variable=glow_var)
    glow_check.pack()

    tk.Label(root, text=lang.message("display_name")).pack()
    display_name_entry = tk.Entry(root)
    display_name_entry.pack()

    tk.Label(root, text=lang.message("lore")).pack()
    lore_text = tk.Text(root, height=5, width=30)
    lore_text.pack()

    tk.Label(root, text=lang.message("actions")).pack()
    actions_text = tk.Text(root, height=5, width=30)
    actions_text.pack()


    #保存按钮
    save_button = tk.Button(root, text=lang.message("save"), command=save_to_file)
    save_button.pack()

    #打开图片
    open_image(f"_internal/slot_{language}.png")
    #显示窗口
    root.mainloop()

def main():
    window()

main()
