import random
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
output_file = config.get('config','output_file')

material = "book"
slot = "0"
amount = "1"
glow = "true"
display_name = "display_name"
lore1 = "lore1"
lore2 = "lore2"
actions = "[command] command"

name = str(input("name:") + "_random-" + str(random.randint(10000, 99999)))
material = str(input("material:"))
slot = str(input("slot(number):"))
amount = str(input("amount(number):"))
glow = str(input("glow(true/false):"))
display_name = str(input("display_name:"))
lore1 = str(input("lore1:"))
lore2 = str(input("lore2:"))
actions = str(input("actions:"))

output = f"""
  {name}:
    material: {material}
    slot: {slot}
    amount: {amount}
    glow: {glow}
    display_name: '{display_name}'
    lore:
      - '{lore1}'
      - '{lore1}'
    actions:
      - '{actions}'
"""

with open(output_file,'a',encoding='utf-8') as f:
    for i in output:
        f.write(i)

print("file save into " + output_file)