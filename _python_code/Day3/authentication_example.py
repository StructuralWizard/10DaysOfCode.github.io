import requests

base_url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "London",
    "appid": "***",
    "units": "metric"  # You can change to "imperial" for Fahrenheit
}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    print(f"Weather in {params['q']}: {data['weather'][0]['description']}")
else:
    print("Error:", response.status_code, response.text)
