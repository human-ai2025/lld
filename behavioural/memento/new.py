# --- The Memento ---
# This object is a simple data container.
# It holds the state but has no behavior.
class EditorState:
    def __init__(self, content: str):
        # In this pattern, we make the attribute "read-only" to emphasize
        # that the Caretaker should not modify it.
        self._content = content
    
    def get_content(self) -> str:
        return self._content

# --- The Originator ---
# It creates mementos and can restore itself from them.
class Editor:
    def __init__(self):
        self._content = ""

    def type(self, words: str):
        self._content += " " + words
    
    def get_content(self) -> str:
        return self._content

    # The Originator creates the Memento, packaging its own state.
    def save(self) -> EditorState:
        print("Originator: Saving my state to a Memento.")
        return EditorState(self._content)

    # The Originator knows how to restore its state from a Memento.
    def restore(self, memento: EditorState):
        print("Originator: Restoring my state from a Memento.")
        self._content = memento.get_content()

# --- The Caretaker ---
# It holds the history of mementos but never looks inside them.
class History:
    def __init__(self, editor: Editor):
        self._editor = editor
        self._history: list[EditorState] = []

    def save(self):
        print("Caretaker: Asking originator for a memento and saving it.")
        # The Caretaker gets an opaque memento object from the editor.
        self._history.append(self._editor.save())

    def undo(self):
        if not self._history:
            return
            
        print("Caretaker: Popping last memento and asking originator to restore.")
        memento = self._history.pop()
        # The Caretaker passes the memento back to the editor.
        # It never inspects the memento's content itself.
        self._editor.restore(memento)

# --- Client Code ---
editor = Editor()
history = History(editor)

history.save() # Save initial empty state

editor.type("Hello")
history.save()

editor.type("World")
print(f"\nCurrent content: '{editor.get_content()}'")

print("\n--- UNDO ---")
history.undo()
print(f"Content after undo: '{editor.get_content()}'")

print("\n--- UNDO ---")
history.undo()
print(f"Content after undo: '{editor.get_content()}'")