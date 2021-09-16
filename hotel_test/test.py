import requests

url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"query":"mumbai","locale":"hi"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': "5f92fdd308msh0bd290c2c66a477p10139cjsnb25e6fed8618"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
