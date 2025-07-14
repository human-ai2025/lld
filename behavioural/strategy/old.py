class Order:
    def __init__(self, items, shipping_provider):
        self.items = items
        # The provider is often a string or an enum, which leads to conditional logic
        self.shipping_provider = shipping_provider

    def calculate_shipping_cost(self):
        cost = 0
        if self.shipping_provider == "fedex":
            # Complex FedEx-specific calculation
            cost = len(self.items) * 5.00
            print(f"Calculating shipping cost via FedEx: ${cost}")
        elif self.shipping_provider == "ups":
            # Complex UPS-specific calculation
            cost = len(self.items) * 4.50
            print(f"Calculating shipping cost via UPS: ${cost}")
        elif self.shipping_provider == "postal":
            # Complex Postal Service-specific calculation
            cost = len(self.items) * 3.00
            print(f"Calculating shipping cost via Postal Service: ${cost}")
        else:
            raise ValueError("Invalid shipping provider")
        return cost

# Client Code
order1 = Order(items=["book", "laptop"], shipping_provider="fedex")
order1.calculate_shipping_cost()

order2 = Order(items=["mouse"], shipping_provider="postal")
order2.calculate_shipping_cost()