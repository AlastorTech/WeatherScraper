import requests, json

#keeping the key here will mean we don't have to try to remember it later.
api_key = "cd77449f2de9a0c710d2504728d2a174"

#The base url for openweathermap's api. 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#This can also be the zip code, and I may force it to be...
city_name = input("Enter city name: ")

#The completed url so we can make our call and get our data!
complete_url = base_url + "q=" + city_name + "&appid=" + api_key

#We get a response back from the website with lots of information in it.
#Now, we can parse through the data and look at everything!
response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    
    # store the value of "main"
    # key in variable y
    y = x["main"]

    #store the value corresponding to the "temp" key of y
    current_temperature = y["temp"]
    current_temperature = (current_temperature-273.15) * 9/5 + 32

    #store the value corresponding to the "pressure" key of y
    current_pressure = y["pressure"]

    #store the value corresponding to the "humidity" key of y
    current_humidity = y["humidity"]

    #store the value of "weather" key in variable z
    z = x["weather"]

    #store the value corresponding to the "description" key at the 0th index of z
    weather_description = z[0]["description"]

    #store the weather descriptions ID. This'll be handy for passing to
    #robotics later.
    weather_desc_id = z[0]["id"]

    #print the values
    print (" Temperature ) = " +
              str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
          "\n humidity (in percentage) = " +
              str(current_humidity) +
          "\n description = " +
              str(weather_description) +
           "\n description ID = " +
               str(weather_desc_id))
else:
        print("City not found")

    
