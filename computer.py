class Computer: #Class for the computer object

    #Attributes for the Computer class

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    """
    Constructor that creates a computer object.
    """
    def __init__ (self, description: str, 
                  processor_type: str, 
                  hard_drive_capacity: int, 
                  memory: int, 
                  operating_system: str,
                  year_made: int, 
                  price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # Methods for the Computer class
    """
    Updates a computer object's price.
    """
    def update_price(self, new_price: int):
        self.price = new_price

    """
    Updates a computer object's operating system.
    """
    def update_OS(self, new_OS: str):
        self.operating_system = new_OS


def main():
        my_computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
        print(my_computer.price)

        my_computer.update_price(1)
        print(my_computer.price)


main()
        

