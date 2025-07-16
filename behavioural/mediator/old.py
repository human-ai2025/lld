# Conceptual representation of the problem.
# In a real UI framework, this would be much more complex.

class OKButton:
    def __init__(self):
        self.is_enabled = False
    def set_enabled(self, enabled: bool):
        print(f"OK Button is now {'Enabled' if enabled else 'Disabled'}")
        self.is_enabled = enabled

class UsernameInput:
    def __init__(self, ok_button: OKButton):
        self._ok_button = ok_button
        self.text = ""
    def set_text(self, text: str):
        self.text = text
        if self.text:
            self._ok_button.set_enabled(True)

class GuestCheckbox:
    def __init__(self, username_input: UsernameInput, password_input): # and so on...
        self._username_input = username_input
        # ... it would also need references to password, etc.
    def set_checked(self, checked: bool):
        # ... logic to enable/disable other components
        pass

# The setup is already complex and tightly coupled.
# The GuestCheckbox would need to know about every other widget.