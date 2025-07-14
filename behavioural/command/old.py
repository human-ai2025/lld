# These are the device classes with specific methods
class Light:
    def on(self): print("Light is ON")
    def off(self): print("Light is OFF")

class Stereo:
    def on(self): print("Stereo is ON")
    def set_cd(self): print("Stereo is set for CD input")
    def off(self): print("Stereo is OFF")

class SimpleRemoteControl:
    def __init__(self):
        # The remote has direct knowledge of the devices
        self._light = Light()
        self._stereo = Stereo()

    def button_one_pressed(self):
        # The logic is hard-coded
        self._light.on()

    def button_two_pressed(self):
        # More hard-coded logic
        self._stereo.on()
        self._stereo.set_cd()

# Client Code
remote = SimpleRemoteControl()
print("Pressing button one...")
remote.button_one_pressed()

print("\nPressing button two...")
remote.button_two_pressed()

# This remote is not "smart." It's rigid. Adding a GarageDoor device requires changing the SimpleRemoteControl class. There's no way to implement an "undo" button.