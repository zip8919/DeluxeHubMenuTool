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

name = str((input("Name(The name used to distinguish items in the DeluxeHub plugin-character string): ") or "Name") + "_random-" + str(random.randint(10000, 99999)))
material = str((input("Material(The Minecraft Namespaced identifier of the item-character string): ")) or "book")
Image.open("slot.png").show
open_image("slot.png")
slot = str((input("Slot(The location of the item within the box interface-nonnegative integer number): ")) or "0")
amount = str((input("Amount(Quantity of items-positive integer number): ")) or "1")
glow = str((input("Glow(Does the item have an enchanted glowing effect-true or false): ")) or "true")
display_name = str((input("Display Name(The name displayed on the item-character string): ")) or "display_name")

lore_rows = int((input("Lore Rows(The number of lines in the item description-positive integer number): ")) or 2)
for i in range(lore_rows):    
    lore_all.append("      - '" + (input(("Line " + str(i+1) + " of lore(character string): ")) or ("lore" + str(i+1))) + "'")
lore = "\n".join(lore_all)

actions = str((input("Actions(Operation of DeluxeHub plugin-character string): ")) or "[command] say hi!")

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

print("Has been saved to the " + output_file + " file")



