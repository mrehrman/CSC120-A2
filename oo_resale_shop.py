from computer import Computer

class ResaleShop:

    # What attributes will it need?
    # Import a few useful containers from the typing module
    from typing import Dict, Optional  

    inventory: Dict[int, Dict] = {}

    itemID = 0 # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__ (self, inventory: Dict, itemID: int):
        self.inventory = inventory
        self.itemID = itemID

    # What methods will you need?
    """ 
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: Dict):
        global itemID
        itemID += 1 # increment itemID
        inventory[itemID] = computer
        return itemID

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if item_id in inventory:
            inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id in inventory:
            del inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if inventory:
         # For each item
            for item_id in inventory:
            # Print its details
                print(f'Item ID: {item_id} : {inventory[item_id]}')
        else:
            print("No inventory to display.")


def main():
    my_computer = Computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)
    print(my_computer.operating_system)

    new_computer = buy(my_computer)


    


main()