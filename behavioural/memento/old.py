class Editor:
    def __init__(self):
        # This is the internal state we want to protect.
        self._content = ""

    def type(self, words: str):
        self._content += words

    # PROBLEM: We have to expose the internal state.
    def get_content(self) -> str:
        return self._content
    
    # PROBLEM: We allow an external object to set our internal state.
    def set_content(self, content: str):
        self._content = content

class History:
    def __init__(self, editor: Editor):
        self._editor = editor
        self._history = [editor.get_content()]

    def save(self):
        self._history.append(self._editor.get_content())

    def undo(self):
        if len(self._history) > 1:
            self._history.pop() # Remove the current state
            last_state = self._history[-1]
            self._editor.set_content(last_state) # Violates encapsulation

# --- Client Code ---
editor = Editor()
history = History(editor)

editor.type("This is the first sentence. ")
history.save()

editor.type("This is the second. ")
history.save()

editor.type("And this is the third.")
print(f"Current content: '{editor.get_content()}'")

history.undo()
print(f"After first undo: '{editor.get_content()}'")

history.undo()
print(f"After second undo: '{editor.get_content()}'")

# Breaks encapsulation 
