import requests

def fetch_images(query):
    # Example: Unsplash API
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id=jdDwVPdF3fRykN7HtKkSn3n5XmO1XnlycUoI1qcDuTc"
    resp = requests.get(url)
    data = resp.json()
    print(data)
    return [img['urls']['regular'] for img in data['results'][:3]]
