import random


material = "book"
slot = "0"
amount = "1"
glow = "true"
display_name = "display_name"
lore1 = "lore1"
lore2 = "lore2"
actions = "[command] command"

name = str(input("name") + "_random_" + str(random.randint(10000, 99999)))
material = str(input("material"))
slot = str(input("slot"))
amount = str(input("amount"))
glow = str(input("glow"))
display_name = str(input("display_name"))
lore1 = str(input("lore1"))
lore2 = str(input("lore2"))
actions = str(input("actions"))

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

print(output)