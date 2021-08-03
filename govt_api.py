import requests

url = "https://api.data.gov.in/resource/4200eb5f-1729-4fee-8477-af5feb715b3c?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=xml&offset=0&limit=10"

payload={}
headers = {
  'accept': 'application/xml',
  'Cookie': 'BIGipServerapi.data.gov.in=!Aux/NnYqkpINvvaCbbshOuMRiHS6yKeJhBNVqpu98j7cPMz98O1teFM+KhaWleRiAeXykkeWy74jmQ==; TS01a12685=0161d6dfc34384ae391fb8632bf67c64ff33347b082f7c78ea7e3d4d82fc1fc3b738d0efdd1bd5058b81c480b81b62802dfb3aebad; TS01a12685028=01e4def2166889ac93b1ff0940acb0425570efb4b229a3d564371d8c5a50849e8ae5210f13ba74bc4a787a59f014f115c4104bc928'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
