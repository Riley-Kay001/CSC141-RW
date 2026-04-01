# Working on Item nd Abstract Base Class CH 10

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_cost(self):
        pass

# 1: Item Subclasses 
class Item:
    def __init__(self, name):
        self.name = name


class ByWeightItem(Item):
    def __init__ (self, name, weight, cost_per_pound):
        super().__init__(name)
        self.weight = weight
        self.cost_per_pound = cost_per_pound 

    def get_cost(self):
        return self.weight * self.cost_per_pound 
    
class ByQuantityItem(Item):
    def __init__ (self, name, quantity, cost_each):
            super().__init__(name)
            self.quantity = quantity
            self.cost_each = cost_each

    def get_cost(self):
        return self.quantity * self.cost_each
    
# 2: Subclasses of ByWeight 
class Grapes(ByWeightItem):
     def __init__(self, weight):
          super().__init__("Grapes", weight, 2.24)

class Bananas(ByWeightItem):
     def __init__(self, weight):
          super().__init__("Bananas", weight, 0.70)

# 3: Subclasses of ByQuantity
class Oranges(ByQuantityItem):
     def __init__(self, quantity):
          super().__init__("Oranges", quantity, 3.50)

class Cantaloupes(ByQuantityItem):
     def __init__ (self, quantity):
          super().__init__("Cantaloupes", quantity, 4.00)

# 4: Heirarchy
# Class called Order
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.get_cost() for item in self.items)

    def get_items(self):
        return self.items

    def __len__(self):
        return len(self.items)

# Driver Code
order = Order()

# Add items
order.add_item(Grapes(2.24))
order.add_item(Bananas(1.5))
order.add_item(Oranges(4))
order.add_item(Cantaloupes(2))

# Print receipt
print("----- RECEIPT -----")
for item in order.get_items():
    if hasattr(item, "weight"):
        print(f"{item.name} ({item.weight} lbs): ${item.get_cost():.2f}")
    elif hasattr(item, "quantity"):
        print(f"{item.name} ({item.quantity}): ${item.get_cost():.2f}")

print("-------------------")
print(f"Total items: {len(order)}")
print(f"Total cost: ${order.calculate_total():.2f}")