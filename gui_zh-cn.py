import tkinter as tk
import random
import configparser
import time
from PIL import Image

config = configparser.ConfigParser()
config.read('config.ini')
output_file = config.get('config', 'output_file')

def open_image(file):
    image = Image.open(file)
    image.show()

# 定义一个函数，用于增加窗口宽度
def increase_width():
    current_height = root.winfo_height()  # 获取当前窗口宽度
    new_height = current_height + 22  # 增加宽度
    root.geometry(f"350x{new_height}")  # 设置新的窗口尺寸


def save_to_file():
    name = name_entry.get() + "_random-" + str(random.randint(10000, 99999))
    material = material_entry.get()
    slot = slot_entry.get()
    amount = amount_entry.get()
    glow = glow_var.get()
    display_name = display_name_entry.get()
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

    label = tk.Label(root, text="[" + time.strftime('%H:%M:%S', time.localtime()) + "]" +"已经保存到" + output_file + "文件")
    label.pack()
    increase_width()
    
# 创建窗口
root = tk.Tk()
root.title("DeluxeHub菜单生成工具")
root.geometry("350x500")

# 添加标签和文本框
tk.Label(root, text="名称(用于DeluxeHub插件区分物品的名称-字符串):").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="显示的图标(物品的Minecraft命名空间ID-字符串):").pack()
material_entry = tk.Entry(root)
material_entry.pack()

tk.Label(root, text="槽位(物品在箱子界面内所在的位置-非负整数):").pack()
slot_entry = tk.Entry(root)
slot_entry.pack()

tk.Label(root, text="数量(物品的数量-正整数):").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

glow_var = tk.BooleanVar()
glow_check = tk.Checkbutton(root, text="发光(物品是否有附魔发光效果)", variable=glow_var)
glow_check.pack()

tk.Label(root, text="显示名称(物品显示的名称-字符串):").pack()
display_name_entry = tk.Entry(root)
display_name_entry.pack()

tk.Label(root, text="Lore的内容(物品描述-字符串）:").pack()
lore_text = tk.Text(root, height=5, width=30)
lore_text.pack()

tk.Label(root, text="操作(DeluxeHub插件的操作-字符串):").pack()
actions_text = tk.Text(root, height=5, width=30)
actions_text.pack()


save_button = tk.Button(root, text="保存", command=save_to_file)
save_button.pack()

open_image("slot_zh-cn.png")

root.mainloop()
