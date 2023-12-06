import requests

API_Key = 'b82ce2b77824e85de7aa68e07b9ed005'

while True:
    city = input("Enter a city: (Enter q to quit) ")
    if city == "q" or city == "Q":
        break

    geourl = f"http://api.openweathermap.org/geo/1.0/direct?appid={API_Key}&q={city}&limit=5"
    geodata = requests.get(geourl).json()

    if len(geodata) == 0:
        print("No info found for this city")
    else:
        country_list = []
        print("Select which country and state is your city in: ")
        for i in range(0, len(geodata)):
            name = geodata[i]["name"]
            country = geodata[i]["country"]
            lat = geodata[i]["lat"]
            lon = geodata[i]["lon"]
            country_list.append({"latitude": lat, "longitude": lon})
            try:
                state = geodata[i]["state"]
                print(f"{i+1}:{name} {country}/{state}")
            except:
                print(f"{i+1}:{name} {country}")
        try:
            option = int(input("Type number as option: ")) - 1
        except:
            print("Not a valid number")
            option = 99
        while option not in range(0, 5):
            print("Unrecognized option")
            try:
                option = int(input("Type number as option: ")) - 1
            except:
                print("Not a valid number")


        lat = country_list[option]["latitude"]
        lon = country_list[option]["longitude"]
        weatherurl = f"https://api.openweathermap.org/data/2.5/weather?appid={API_Key}&lat={lat}&lon={lon}&units=metric"

        weatherdata = requests.get(weatherurl).json()

        print(f"The weather for this city is {weatherdata['weather'][0]['main']} - {weatherdata['weather'][0]['description']}")
        print(f"The temperature is {weatherdata['main']['temp']} degree Celsius")