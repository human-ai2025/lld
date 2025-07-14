from abc import ABC, abstractmethod

# --- The Abstract Class ---
class DataProcessor(ABC):
    # This is the "Template Method". It's not abstract.
    # It defines the skeleton of the algorithm.
    def process(self):
        self.extract()
        self.transform()
        if self.needs_validation(): # This is a "hook"
            print("Hook: Performing data validation...")
        self.load()
        print("Processing complete.")

    # --- Primitive Operations (to be implemented by subclasses) ---
    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    @abstractmethod
    def load(self):
        pass
    
    # --- A "Hook" ---
    # A concrete method with a default implementation.
    # Subclasses are not required to override it.
    def needs_validation(self):
        return False

# --- Concrete Subclasses ---
class CsvDataProcessor(DataProcessor):
    def extract(self):
        print("CsvProcessor: Extracting data from CSV.")

    def transform(self):
        print("CsvProcessor: Transforming CSV data.")

    def load(self):
        print("CsvProcessor: Loading data to SQL database.")
        
    # This subclass chooses to override the hook
    def needs_validation(self):
        return True

class ApiDataProcessor(DataProcessor):
    def extract(self):
        print("ApiProcessor: Extracting data from API.")

    def transform(self):
        print("ApiProcessor: Transforming JSON data.")

    def load(self):
        print("ApiProcessor: Loading data to NoSQL database.")
    # This subclass uses the default hook implementation (returns False)

# --- Client Code ---
print("--- Processing CSV Data ---")
csv_processor = CsvDataProcessor()
csv_processor.process() # The client calls the single template method

print("\n" + "="*25 + "\n")

print("--- Processing API Data ---")
api_processor = ApiDataProcessor()
api_processor.process()