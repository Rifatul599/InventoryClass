class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self,item,quantity):
        if item in self.items:
            self.items[item]+=quantity
        else:
            self.items[item]=quantity
            print(f"Added {quantity} of {item} to the inventory.")

    def remove_item(self,item,quantity):
        if item not in self.items:
            print(f"Error: {item} is not in the inventory.")
        elif self.items[item]<quantity:
            print(f"Error: Not enough {item} in stock to remove.")

        else:
            self.items[item]-=quantity
            if self.items[item]==0:
                del self.items[item]
                print(f"Removed {quantity} of {item} from inventory.")

    def check_stock(self,item):
        return self.items.get(item,0)

    def list_all_items(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item,quantity in self.items.items():
                print(f"{item}: {quantity} in stock.")

    def restock_item(self,item,quantity):
        if item in self.items:
            self.items[item]+=quantity
            print(f"Restock {quantity} of {item}.")
        else:
            print(f"Error: {item} not in the inventory.Add the item first.")

    def generate_inventory_report(self):
        if not self.items:
            return "Inventory is empty."
        report="Inventory report:\n"
        for item, quantity in self.items.items():
            report+=f"{item}:{quantity}\n"
            return report


store_inventory=Inventory()

store_inventory.add_item("Apple",100)
store_inventory.add_item("Banana",50)
store_inventory.add_item("Orange",75)

print(store_inventory.check_stock("Apple"))
store_inventory.list_all_items()
store_inventory.restock_item("Apple",50)
print(store_inventory.generate_inventory_report())






