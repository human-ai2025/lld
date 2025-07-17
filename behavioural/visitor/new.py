from __future__ import annotations
from abc import ABC, abstractmethod

# --- Visitor Interface ---
# Declares a visit method for each type of Concrete Element.
class Visitor(ABC):
    @abstractmethod
    def visit_headline(self, element: Headline): pass
    @abstractmethod
    def visit_paragraph(self, element: Paragraph): pass

# --- Element Interface ---
# Declares an `accept` method to take a visitor.
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor): pass

# --- Concrete Elements ---
# They don't contain any operational logic.
class Headline(Element):
    def __init__(self, text: str):
        self.text = text
    
    # The first dispatch happens here.
    def accept(self, visitor: Visitor):
        # It calls the correct visit method on the visitor, passing itself.
        visitor.visit_headline(self)

class Paragraph(Element):
    def __init__(self, text: str):
        self.text = text
        
    def accept(self, visitor: Visitor):
        visitor.visit_paragraph(self)

# --- Concrete Visitors ---
# Each visitor encapsulates one specific operation.
class HtmlExportVisitor(Visitor):
    def __init__(self):
        self.output = ""
    def visit_headline(self, element: Headline):
        self.output += f"<h1>{element.text}</h1>\n"
    def visit_paragraph(self, element: Paragraph):
        self.output += f"<p>{element.text}</p>\n"

class TextExtractorVisitor(Visitor):
    def __init__(self):
        self.output = ""
    def visit_headline(self, element: Headline):
        self.output += f"{element.text}\n"
    def visit_paragraph(self, element: Paragraph):
        self.output += f"{element.text}\n"

# --- Client Code ---
document = [
    Headline("The Visitor Pattern"),
    Paragraph("This pattern is great for separating algorithms..."),
    Paragraph("...from the objects they operate on.")
]

# Use the HtmlExportVisitor to perform one operation
html_visitor = HtmlExportVisitor()
print("--- Exporting to HTML ---")
for element in document:
    element.accept(html_visitor)
print(html_visitor.output)

# Use the TextExtractorVisitor to perform a different operation
# We did not have to change ANY of the element classes.
text_visitor = TextExtractorVisitor()
print("--- Extracting Raw Text ---")
for element in document:
    element.accept(text_visitor)
print(text_visitor.output)