class Inventory:

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.items = []
        self.left_capacity = self.__capacity

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
            self.left_capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
hui = Inventory(3)
hui.add_item("putka")
hui.add_item("kon")
print(hui.add_item("maika ti"))
print(hui.get_capacity())
print(hui)