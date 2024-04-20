class message_zh_cn:
    def __init__(self):
        self.title = "DeluxeHub菜单生成工具"
        self.name = "名称(用于DeluxeHub插件区分物品的名称-字符串):"
        self.material = "显示的图标(物品的Minecraft命名空间ID-字符串):"
        self.slot = "槽位(物品在箱子界面内所在的位置-非负整数):"
        self.amount = "数量(物品的数量-正整数):"
        self.glow = "发光(物品是否有附魔发光效果)"
        self.display_name = "显示名称(物品显示的名称-字符串):"
        self.lore = "Lore的内容(物品描述-字符串）:"
        self.actions = "操作(DeluxeHub插件的操作-字符串):"
        self.save = "保存"
        self.saveto = "已经保存到"
        self.savesuccess = "保存成功"
        
    def message(self, name):
        return getattr(self, name, None)

class message_en_us:
    def __init__(self):
        self.title = "DeluxeHub Menu Generation Tool"
        self.name = "Name(The name used to distinguish items in the DeluxeHub plugin - character string): "
        self.material = "Material(The Minecraft Namespaced identifier of the item - character string): "
        self.slot = "Slot(The location of the item within the box interface - nonnegative integer number): "
        self.amount = "Amount(Quantity of items - positive integer number): "
        self.glow = "Glow(Does the item have an enchanted glowing effect - true or false): "
        self.display_name = "Display Name(The name displayed on the item - character string): "
        self.lore = "Lore content (Item description - string)"
        self.actions = "Actions(Operation of DeluxeHub plugin - character string): "
        self.save = "save"
        self.saveto = "Save the file to "
        self.savesuccess = "Save successfully"
        
    def message(self, name):
        return getattr(self, name, None)