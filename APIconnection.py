import sqlite3
import requests

# Function to get optimal growing conditions from Trefle API
def get_growing_conditions(seed_type):
    api_key = 'YOUR_TREFLE_API_KEY'  # Replace with your actual Trefle API key
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
    conn = sqlite3.connect('seeds.db')
    cursor = conn.cursor()
    cursor.execute('SELECT seed_type FROM seeds')
    seeds = cursor.fetchall()
    conn.close()
    return [seed[0] for seed in seeds]

# Main function to display optimal growing conditions
def main():
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

if __name__ == "__main__":
    main()