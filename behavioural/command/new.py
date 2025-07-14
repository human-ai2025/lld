from abc import ABC, abstractmethod

# --- The Command Interface ---
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# --- The Receivers (they do the actual work) ---
class Light:
    def on(self): print("Light is ON")
    def off(self): print("Light is OFF")

class Stereo:
    def on(self): print("Stereo is ON")
    def set_cd(self): print("Stereo is set for CD input")
    def off(self): print("Stereo is OFF")

# --- Concrete Commands ---
# Each command encapsulates a request by binding a receiver to an action.
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()

    def undo(self):
        self._stereo.off()

# --- The Invoker ---
# The invoker is completely decoupled from the receivers (Light, Stereo).
# It only knows about the Command interface.
class RemoteControl:
    def __init__(self):
        self._command: Command = None
        self._undo_command: Command = None

    def set_command(self, command: Command):
        self._command = command

    def button_was_pressed(self):
        if self._command:
            self._command.execute()
            # Keep track of the last command for the undo feature
            self._undo_command = self._command

    def undo_button_was_pressed(self):
        print("--- UNDO ---")
        if self._undo_command:
            self._undo_command.undo()
            self._undo_command = None

# --- The Client ---
# The client is responsible for creating the receivers, commands, 
# and setting up the invoker.

# Create the invoker
remote = RemoteControl()

# Create the receivers
living_room_light = Light()
living_room_stereo = Stereo()

# Create the command objects, binding receivers to them
light_on = LightOnCommand(living_room_light)
stereo_on = StereoOnWithCDCommand(living_room_stereo)

# Configure the invoker with a command
remote.set_command(light_on)
remote.button_was_pressed()
remote.undo_button_was_pressed()

print("\n" + "="*20 + "\n")

remote.set_command(stereo_on)
remote.button_was_pressed()
remote.undo_button_was_pressed()