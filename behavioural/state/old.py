class VendingMachine:
    # Using strings to represent states
    NO_COIN = "NO_COIN"
    HAS_COIN = "HAS_COIN"
    
    def __init__(self):
        self.state = self.NO_COIN

    def insert_coin(self):
        if self.state == self.HAS_COIN:
            print("You can't insert another coin.")
        elif self.state == self.NO_COIN:
            self.state = self.HAS_COIN
            print("You inserted a coin.")

    def eject_coin(self):
        if self.state == self.HAS_COIN:
            self.state = self.NO_COIN
            print("Coin returned.")
        elif self.state == self.NO_COIN:
            print("You haven't inserted a coin.")
            
    def select_item(self):
        if self.state == self.HAS_COIN:
            print("Item selected...")
            # transition to a "SOLD" state would happen here
            self.state = self.NO_COIN
        elif self.state == self.NO_COIN:
            print("You need to insert a coin first.")

# --- Client Code ---
machine = VendingMachine()

machine.select_item()  # Fails
machine.insert_coin()  # Succeeds
machine.eject_coin()   # Succeeds

# This class is already becoming messy. Adding a new state like SOLD_OUT would require modifying every single method. This violates the Open/Closed and Single Responsibility principles.