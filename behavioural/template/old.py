class CsvDataProcessor:
    def process(self):
        self.extract_csv_data()
        self.transform_data()
        self.load_data_to_warehouse()

    def extract_csv_data(self):
        print("Extracting data from a CSV file...")

    def transform_data(self):
        print("Transforming data (generic transformation)...")

    def load_data_to_warehouse(self):
        print("Loading data into the data warehouse...")

class ApiDataProcessor:
    def process(self):
        # This process logic is IDENTICAL to the one in CsvDataProcessor
        self.extract_api_data()
        self.transform_data()
        self.load_data_to_warehouse()

    def extract_api_data(self):
        print("Extracting data from an API endpoint...")

    def transform_data(self):
        # Another duplicated method
        print("Transforming data (generic transformation)...")

    def load_data_to_warehouse(self):
        # And another one
        print("Loading data into the data warehouse...")

# Client Code
csv_processor = CsvDataProcessor()
csv_processor.process()

print("\n" + "="*20 + "\n")

api_processor = ApiDataProcessor()
api_processor.process()

# The problem is clear: the process method is the same in both classes. If we needed to add a new step, like validate_data(), we'd have to modify every single processor class. This is brittle and violates the DRY (Don't Repeat Yourself) principle.