import sys
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
from geopy.geocoders import Nominatim


def get_location(address):
    geolocator = Nominatim(user_agent="RestaurantRater")
    geocoded_address = geolocator.geocode(address)
    return f'{geocoded_address.latitude}, {geocoded_address.longitude}'

def get_restaurant_results(location, keyword, API_KEY):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&keyword={keyword}&radius=5000&type=restaurant&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        results = data['results']
        for result in results:
            # Extract relevant information from the result
            name = result['name']
            address = result['vicinity']
            rating = result['rating'] if 'rating' in result else 'N/A'

            print(f'Name: {name}')
            print(f'Address: {address}')
            print(f'Rating: {rating}')
            print('---')
    else:
        print('Error:', data['status'])

def main(argv):
    #encode API key later
    API_KEY = "AIzaSyBGRwQhPbp_p8bZK0U7RvOK-_l4sVZmze8"

    #location and restaurant type will be user-entered data
    address = "Salt Lake City"
    keyword = "Italian"
    location = get_location(address)
    get_restaurant_results(location, keyword, API_KEY)



if __name__ == "__main__":
    main(sys.argv[1:]) 