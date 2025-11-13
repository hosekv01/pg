import sys
import requests
import json

if __name__ == "__main__":

    if len(sys.argv) > 2:
        print("Usage: python cviceni6_1.py [optional_prefix]")
        sys.exit(1)
    prefix = sys.argv[1] 

    print(f'Downloading webpage with prefix: {prefix}')

    response = requests.get("https://data.carnewschina.com/suggest?q=" + prefix)

    if not response.ok:
        print("Error fetching data from the server.")
        sys.exit(1)
    else:
        data = json.loads(response.text)
        for model in data['models']:
            print(model['name'])
            