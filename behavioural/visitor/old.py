class Headline:
    def __init__(self, text):
        self.text = text
    
    # Operation 1
    def to_html(self):
        return f"<h1>{self.text}</h1>"
        
    # Operation 2
    def extract_text(self):
        return self.text

class Paragraph:
    def __init__(self, text):
        self.text = text
        
    # Operation 1
    def to_html(self):
        return f"<p>{self.text}</p>"
        
    # Operation 2
    def extract_text(self):
        return self.text

# PROBLEM: Adding a new operation, like count_words(), requires modifying
# BOTH the Headline and Paragraph classes.