from __future__ import annotations
from abc import ABC, abstractmethod

# --- The Mediator Interface ---
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str):
        pass

# --- The Colleague Base Class ---
# Colleagues are aware of the mediator, but not of each other.
class Colleague:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator
    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

# --- Concrete Colleagues (the UI widgets) ---
class OKButton(Colleague):
    def __init__(self, mediator: Mediator = None):
        super().__init__(mediator)
        self.is_enabled = False
    def set_enabled(self, enabled: bool):
        print(f"UI: OK Button is now {'Enabled' if enabled else 'Disabled'}")
        self.is_enabled = enabled

class UsernameInput(Colleague):
    def __init__(self, mediator: Mediator = None):
        super().__init__(mediator)
        self.text = ""
    def on_text_changed(self, new_text: str):
        print(f"UI: Username text changed to '{new_text}'")
        self.text = new_text
        self._mediator.notify(self, "username_typed")

class GuestCheckbox(Colleague):
    def __init__(self, mediator: Mediator = None):
        super().__init__(mediator)
        self.is_checked = False
    def on_checked(self, is_checked: bool):
        print(f"UI: Guest checkbox {'checked' if is_checked else 'unchecked'}")
        self.is_checked = is_checked
        self._mediator.notify(self, "guest_checked")

# --- The Concrete Mediator ---
# This is where all the complex interaction logic lives.
class AuthenticationDialog(Mediator):
    def __init__(self):
        self._username_input = UsernameInput(self)
        self._guest_checkbox = GuestCheckbox(self)
        self._ok_button = OKButton(self)

    def notify(self, sender: object, event: str):
        print(f"MEDIATOR: Received event '{event}' from {sender.__class__.__name__}")
        if event == "guest_checked":
            # Logic: When guest is checked, disable username and ok button
            is_guest = self._guest_checkbox.is_checked
            # In a real UI, you'd disable the input widget itself
            print(f"MEDIATOR: {'Disabling' if is_guest else 'Enabling'} username input.")
            self._ok_button.set_enabled(not is_guest)

        if event == "username_typed":
            # Logic: If username is empty, disable ok button
            if not self._username_input.text:
                self._ok_button.set_enabled(False)
            else:
                self._ok_button.set_enabled(True)
    
    # These methods simulate user interaction
    def get_username_input(self): return self._username_input
    def get_guest_checkbox(self): return self._guest_checkbox

# --- Client Code ---
dialog = AuthenticationDialog()

# Simulate user actions
# The client talks to the widgets, the widgets talk to the mediator.
user_input = dialog.get_username_input()
guest_check = dialog.get_guest_checkbox()

user_input.on_text_changed("Alice")
print("-" * 20)
guest_check.on_checked(True)
print("-" * 20)
user_input.on_text_changed("")
print("-" * 20)
guest_check.on_checked(False)