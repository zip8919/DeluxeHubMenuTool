from PIL import Image
import random
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
output_file = config.get('config','output_file')

def open_image(file):
    image = Image.open(file)
    image.show()

material = "book"
slot = "0"
amount = "1"
glow = "true"
display_name = "display_name"
lore_all = []
actions = "[command] say hi!"

name = str((input("名称(用于DeluxeHub插件区分物品的名称-字符串): ") or "Name") + "_random-" + str(random.randint(10000, 99999)))
material = str((input("显示的图标(物品的Minecraft命名空间ID-字符串): ")) or "book")
open_image("slot_zh-cn.png")
slot = str((input("槽位(物品在箱子界面内所在的位置-非负整数): ")) or "0")
amount = str((input("数量(物品的数量-正整数): ")) or "1")
glow = str((input("发光(物品是否有附魔发光效果-是'true'或否'false'): ")) or "true")
display_name = str((input("显示名称(物品显示的名称-字符串): ")) or "display_name")

lore_rows = int((input("Lore的行数(物品描述的行数-正整数): ")) or 2)
for i in range(lore_rows):    
    lore_all.append("      - '" + (input(("Lore的第" + str(i+1) + "行(字符串): ")) or ("lore" + str(i+1))) + "'")
lore = "\n".join(lore_all)

actions = str((input("操作(DeluxeHub插件的操作-字符串): ")) or "[command] say hi!")

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
      - '{actions}'"""

with open(output_file,'a',encoding='utf-8') as f:
    for i in output:
        f.write(i)

print("已经保存到" + output_file + "文件")



