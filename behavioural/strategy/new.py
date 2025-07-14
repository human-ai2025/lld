from abc import ABC, abstractmethod

# --- Abstract Strategy Interface ---
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, items):
        pass

# --- Concrete Strategies ---
class FedExStrategy(ShippingStrategy):
    def calculate(self, items):
        cost = len(items) * 5.00
        print(f"Calculating shipping cost via FedEx: ${cost}")
        return cost

class UPSStrategy(ShippingStrategy):
    def calculate(self, items):
        cost = len(items) * 4.50
        print(f"Calculating shipping cost via UPS: ${cost}")
        return cost

class PostalStrategy(ShippingStrategy):
    def calculate(self, items):
        cost = len(items) * 3.00
        print(f"Calculating shipping cost via Postal Service: ${cost}")
        return cost

# --- The Context ---
class Order:
    def __init__(self, items, shipping_strategy: ShippingStrategy):
        self.items = items
        # The Order class HAS-A ShippingStrategy
        self._shipping_strategy = shipping_strategy

    def set_shipping_strategy(self, shipping_strategy: ShippingStrategy):
        """Allows changing the strategy at runtime."""
        self._shipping_strategy = shipping_strategy

    def calculate_shipping_cost(self):
        # Delegate the work to the strategy object
        return self._shipping_strategy.calculate(self.items)

# Client Code
items = ["book", "laptop"]

# The client chooses the strategy and injects it into the context
order1 = Order(items, FedExStrategy())
order1.calculate_shipping_cost()

order2 = Order(items, UPSStrategy())
order2.calculate_shipping_cost()

# Now, let's add a new provider without touching the Order class
class DHLStrategy(ShippingStrategy):
    def calculate(self, items):
        cost = len(items) * 6.50
        print(f"Calculating shipping cost via DHL: ${cost}")
        return cost

order3 = Order(items, DHLStrategy())
order3.calculate_shipping_cost()