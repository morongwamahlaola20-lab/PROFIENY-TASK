import pandas as pd
import requests

class DataPipeline:
    """A professional data pipeline for fetching and cleaning API data."""
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.raw_data = None
        self.df = None

    def fetch_data(self):
        """Fetch data from the external API with error handling."""
        print(f"Connecting to API: {self.api_url}")
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            self.raw_data = response.json()
            print("Successfully fetched data.")
        except Exception as e:
            print(f"Error fetching data: {e}")

    def clean_data(self):
        """Transform raw JSON into a clean Pandas DataFrame."""
        if self.raw_data:
            # Extract specific fields to show data manipulation skills
            processed_data = []
            for user in self.raw_data:
                processed_data.append({
                    'id': user.get('id'),
                    'name': user.get('name'),
                    'email': user.get('email'),
                    'company_name': user.get('company', {}).get('name')
                })
            
            self.df = pd.DataFrame(processed_data)
            print("\n--- Cleaned Data Sample (Pandas Output) ---")
            print(self.df.head())
        else:
            print("No data available to clean.")

# --- Execution ---
if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/users"
    pipeline = DataPipeline(URL)
    pipeline.fetch_data()
    pipeline.clean_data()
    