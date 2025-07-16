from __future__ import annotations
from abc import ABC, abstractmethod

# --- The Context ---
# The VendingMachine delegates all state-specific behavior to its current state object.
class VendingMachine:
    def __init__(self):
        # Create an instance for each possible state
        self._no_coin_state = NoCoinState(self)
        self._has_coin_state = HasCoinState(self)
        self._sold_out_state = SoldOutState(self)
        
        # The initial state
        self._current_state = self._no_coin_state

    def set_state(self, new_state: State):
        self._current_state = new_state

    # These methods delegate to the current state object
    def insert_coin(self):
        self._current_state.insert_coin()
    def eject_coin(self):
        self._current_state.eject_coin()
    def select_item(self):
        self._current_state.select_item()
    
    # Getters for the state objects so they can transition the context
    def get_has_coin_state(self) -> State: return self._has_coin_state
    def get_no_coin_state(self) -> State: return self._no_coin_state
    def get_sold_out_state(self) -> State: return self._sold_out_state

# --- The State Interface (ABC) ---
class State(ABC):
    def __init__(self, machine: VendingMachine):
        # State objects need a reference to the context to transition it
        self.machine = machine
        
    @abstractmethod
    def insert_coin(self): pass
    @abstractmethod
    def eject_coin(self): pass
    @abstractmethod
    def select_item(self): pass

# --- Concrete States ---
# Each class implements the behavior associated with one state.
class NoCoinState(State):
    def insert_coin(self):
        print("You inserted a coin.")
        # Transition the machine's state
        self.machine.set_state(self.machine.get_has_coin_state())
    def eject_coin(self):
        print("You haven't inserted a coin.")
    def select_item(self):
        print("You selected an item, but there's no coin.")

class HasCoinState(State):
    def insert_coin(self):
        print("You can't insert another coin.")
    def eject_coin(self):
        print("Coin returned.")
        self.machine.set_state(self.machine.get_no_coin_state())
    def select_item(self):
        print("Item selected... dispensing.")
        # In a real system, this would transition to a "SoldState"
        self.machine.set_state(self.machine.get_no_coin_state())

class SoldOutState(State):
    def insert_coin(self): print("You can't insert a coin, the machine is sold out.")
    def eject_coin(self): print("You can't eject, you haven't inserted a coin yet.")
    def select_item(self): print("You selected an item, but there are no items left.")


# --- Client Code ---
machine = VendingMachine()

print(f"Machine is in: {machine._current_state.__class__.__name__}")
machine.select_item()
machine.insert_coin()

print(f"\nMachine is in: {machine._current_state.__class__.__name__}")
machine.insert_coin()
machine.eject_coin()