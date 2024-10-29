import sqlite3
import requests

# Function to get optimal growing conditions from Trefle API
def get_growing_conditions(seed_type):
    """
    Fetch optimal growing conditions for a given seed type from the Trefle API.

    Args:
        seed_type (str): The type of seed to search for in the Trefle API.

    Returns:
        dict: A dictionary containing the common name of the plant and its optimal growing conditions.
              Returns 'N/A' for missing values. If no data is found, returns None.
    """
    api_key = 'TREFLE_API_KEY'  # Replace with your own actual Trefle API key
    url = f'https://trefle.io/api/v1/plants/search?token={api_key}&q={seed_type}'
    
    response = requests.get(url)
    data = response.json()

    if data['data']:
        plant = data['data'][0]
        return {
            'common_name': plant.get('common_name', 'N/A'),
            'optimal_conditions': plant.get('growing_conditions', 'N/A')
        }
    else:
        return None

# Function to read seed types from the database
def read_seeds():
    """
    Read seed types from the database.

    Returns:
        list: A list of seed types
    """
    conn = sqlite3.connect('seeds.db')
    cursor = conn.cursor()
    cursor.execute('SELECT seed_type FROM seeds')
    seeds = cursor.fetchall()
    conn.close()
    return [seed[0] for seed in seeds]

# Main function to display optimal growing conditions
/*************  ✨ Codeium Command 🌟  *************/
def main():
    """Main function to display optimal growing conditions"""
    seeds = read_seeds()
    
    if not seeds:
        print("No seeds found in the database.")
        return

    print("Optimal Growing Conditions:")
    for seed in seeds:
        conditions = get_growing_conditions(seed)
        if conditions:
            print(f"\nCommon Name: {conditions['common_name']}")
            print(f"Optimal Conditions: {conditions['optimal_conditions']}")
        else:
            print(f"\nNo data found for seed type: {seed}")
/******  3c76d1e7-4c7b-49b7-9f0a-9426f58db106  *******/

if __name__ == "__main__":
    main()