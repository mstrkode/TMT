# Adding an Item to Inventory through the API

This doc is a guide for adding an item to inventory through the API.

## Understanding the Requirements

You need to add a new inventory item with specific metadata fields:
- year
- actors (as a list)
- imdb_rating
- rotten_tomatoes_rating
- film_locations (as a list)

## The Approach

Our inventory system uses a REST API with JSON payloads. To add a new item, we'll need to:

1. Understand the data structure
2. Prepare the request payload
3. Send a POST request to the right endpoint
4. Handle the response

## Step 1: Understanding the Data Structure

Looking at our `Inventory` model, we need to provide:
- `name`: The title of the inventory item
- `type`: The type ID (movie, series, episode, etc.)
- `language`: The language ID
- `metadata`: A JSON object with our specific fields

## Step 2: Preparing the Request Payload

Here's how your request payload should look:

```json
{
  "name": "The Movie Title",
  "type": 1,  // ID of the inventory type (e.g., 1 for "Movie")
  "language": 37,  // ID of the language (e.g., 37 for "English")
  "metadata": {
    "year": 2023,
    "actors": ["Actor 1", "Actor 2", "Actor 3"],
    "imdb_rating": 8.5,
    "rotten_tomatoes_rating": 95,
    "film_locations": ["New York", "Los Angeles", "Toronto"]
  }
}
```

## Step 3: Sending the Request

You can use various tools to send the request:

### Using Python Requests

```python
import requests
import json

url = "http://your-api-domain/inventory/"

payload = {
  "name": "The Movie Title",
  "type": 1,
  "language": 37,
  "metadata": {
    "year": 2023,
    "actors": ["Actor 1", "Actor 2", "Actor 3"],
    "imdb_rating": 8.5,
    "rotten_tomatoes_rating": 95,
    "film_locations": ["New York", "Los Angeles", "Toronto"]
  }
}

headers = {
  "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

# Check if the request was successful
if response.status_code == 201:
    print("Success! Inventory item created.")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

### Using cURL

```bash
curl -X POST http://your-api-domain/inventory/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "The Movie Title",
    "type": 1,
    "language": 37,
    "metadata": {
      "year": 2023,
      "actors": ["Actor 1", "Actor 2", "Actor 3"],
      "imdb_rating": 8.5,
      "rotten_tomatoes_rating": 95,
      "film_locations": ["New York", "Los Angeles", "Toronto"]
    }
  }'
```

## Step 4: Handling Common Issues

### Finding Type and Language IDs

If you don't know the IDs for types and languages, you can get them with:

```python
# Get all inventory types
response = requests.get("http://your-api-domain/inventory/types/")
types = response.json()
print(types)

# Get all languages
response = requests.get("http://your-api-domain/inventory/languages/")
languages = response.json()
print(languages)
```

### Validation Errors

Our API validates the metadata structure. If you get a 400 error, check:
- All required fields are present
- Data types are correct (numbers for ratings, arrays for actors and locations)
- Ratings are within expected ranges (0-10 for IMDb, 0-100 for Rotten Tomatoes)

## Complete Working Example

Here's a complete script that:
1. Gets the first available type and language
2. Creates a new inventory item
3. Handles errors properly

```python
import requests
import json

base_url = "http://your-api-domain/inventory"

# Step 1: Get the first available type
response = requests.get(f"{base_url}/types/")
if response.status_code != 200:
    print("Error fetching types")
    exit(1)
    
types = response.json()
if not types:
    print("No inventory types available")
    exit(1)
    
type_id = types[0]["id"]

# Step 2: Get the first available language
response = requests.get(f"{base_url}/languages/")
if response.status_code != 200:
    print("Error fetching languages")
    exit(1)
    
languages = response.json()
if not languages:
    print("No languages available")
    exit(1)
    
language_id = languages[0]["id"]

# Step 3: Create the inventory item
payload = {
    "name": "The Shawshank Redemption",
    "type": type_id,
    "language": language_id,
    "metadata": {
        "year": 1994,
        "actors": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"],
        "imdb_rating": 9.3,
        "rotten_tomatoes_rating": 91,
        "film_locations": ["Mansfield, Ohio", "Ashland, Ohio"]
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(base_url, data=json.dumps(payload), headers=headers)

if response.status_code == 201:
    print("Success! Inventory item created:")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

Hope this helps! Please reach out to a team member if you have any questions or run into any issues.