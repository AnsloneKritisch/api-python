import requests
import json

url = "https://api.data.gov.in/resource/4200eb5f-1729-4fee-8477-af5feb715b3c?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=xml&offset=0&limit=10"

r = requests.get(url)

data = r.json()

print(data)
