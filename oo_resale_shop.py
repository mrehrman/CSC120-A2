#Import the Computer class
from computer import Computer

class ResaleShop: #Class for the ResaleShop object

    #Attributes for the ResaleShop class
    #Import a few useful containers from the typing module
    from typing import Optional  

    inventory: list = [] #List to store inventory
 
    """
    Constructor to create a ResaleShop object
    """
    def __init__ (self, inventory: list):
        self.inventory = inventory

    

    #Methods for the ResaleShop class
    """ 
    Takes in a computer object and adds it to the inventory. Prints message confirming that the
    computer was added.
    """
    def buy(self, new_computer: Computer):
        self.inventory.append(new_computer)
        print(new_computer.description, "added to inventory!")

    """
    Takes in a computer and a new price, updates the price of the 
    computer if it is in the inventory, prints error message otherwise.
    """
    def update_price(self, computer: Computer, new_price: int):
        if computer in self.inventory:
            computer.price = new_price
            print(computer.description, "price updated to", computer.price)
        else:
            print("Item", computer.description, "not found. Cannot update price.")

    """
    Takes in a computer and a new operating system, updates the operating system of the 
    computer if it is in the inventory, prints error message otherwise.
    """
    def update_OS(self, computer: Computer, new_os: str):
        if computer in self.inventory:
            computer.operating_system = new_os
            print(computer.description, "operating system updated to", computer.operating_system)
        else:
            print("Item", computer.description, "not found. Cannot update operating system.")


    """
    Takes in a computer object, removes the  computer if it is the inventory, 
    prints error message otherwise.
    """
    def sell(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item", computer.description, "sold!")
        else: 
            print("Item", computer.description, "not found. Please select another item to sell.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
         # For each item
            for computer in self.inventory:
            # Print its details
                print(computer.description) 
        else:
            print("No inventory to display.")

    """
    Takes in a computer and optional new operating system. Checks if the computer is in the inventory and 
    updates its price based on its year made. If it is in the inventory and a new OS was given, 
    updates the computer's OS. Prints error if computer is not in the inventory.
    """
    def refurbish(self, computer: Computer, new_os: Optional[str] = None):
        if computer in self.inventory:
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff
            print("New price:", computer.price)
            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
                print("New operating system:", computer.operating_system)
        else:
            print("Item", computer.description, "not found. Please select another item to refurbish.")

def main():
    #create 3 computer objects of class Computer
    computer1 = Computer("Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500)

    computer2 = Computer("2020 MacBook Air", 
    "Intel", 1024, 32, 
    "MacOS", 2020, 700)

    computer3 = Computer("2019 MacBook Pro", 
    "Intel", 256, 16, 
    "High Sierra", 2019, 1000)

    #create a shop with no computers in its inventory
    shop = ResaleShop([])
    #display starting inventory
    shop.print_inventory()
    #buy 3 computers (add to inventory)
    shop.buy(computer1)
    shop.print_inventory()
    shop.buy(computer2)
    shop.buy(computer3)
    shop.print_inventory()
    #update the price of a computer in the inventory
    shop.update_price(computer2, 1000)
    #update the operating system of a computer in the inventory
    shop.update_OS(computer1, "MacOS Sonoma")
    #sell a computer in the shop's inventory
    shop.sell(computer2)
    #try to update price of a computer not in the inventory
    shop.update_price(computer2, 400)
    #try to sell a computer not in the inventory
    shop.sell(computer2)
    #reburish a computer in the inventory
    shop.refurbish(computer3, "MacOS Sonoma")
    #try to refurbish a computer not in the inventory
    shop.refurbish(computer2)
    shop.print_inventory()


main()