class ResaleShop: #Class for the ResaleShop object

    #Attributes for the ResaleShop class
    # Import a few useful containers from the typing module
    from typing import Dict, Optional  

    inventory: Dict[int, Dict] = {} #Dictionary to store inventory

    itemID = 0 # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID

    
    """
    Constructor to create a ResaleShop object
    """
    def __init__ (self, inventory: Dict[int, Dict], itemID: int):
        self.inventory = inventory
        self.itemID = itemID

    

    #Methods for the ResaleShop class
    """ 
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, new_computer: Dict):
        global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = new_computer
        return self.itemID

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if self.item_id in self.inventory:
            self.inventory[self.item_id]["price"] = new_price
        else:
            print("Item", self.item_id, "not found. Cannot update price.")

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if self.item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", self.item_id, "sold!")
        else: 
            print("Item", self.item_id, "not found. Please select another item to sell.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
         # For each item
            for self.item_id in self.inventory:
            # Print its details
                print(f'Item ID: {self.item_id} : {self.inventory[self.item_id]}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    pass

main()