import tkinter as tk
import time
import requests

def get_data():
    CityName = CityEntry.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={CityName}&appid=<API KEY>"
    #print(api)
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    temp_max = int(json_data['main']['temp_max'] - 273.15)
    temp_min = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind_speed = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 19800))

    FinalData = str(condition) + "\n" + str(temp) + "°C"
    FinalInfo = "\n" + "Max Temp: " + str(temp_max) + "\n" + "Min Temp: " + str(temp_min) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind_speed) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    OP1.config(text = FinalData)
    OP2.config(text = FinalInfo)

master = tk.Tk()
master.geometry("600x500")
master.title("Weather Application")

font_1 = ("poppins", 15, "bold")
font_2 = ("poppins", 35, "bold")

CityEntry = tk.Entry(master, font=font_2)
CityEntry.pack(pady=20)
CityEntry.focus()

submitButton = tk.Button(master, text = "Get Data", command = get_data)
submitButton.pack()

OP1 = tk.Label(master, font=font_2)
OP1.pack()
OP2 = tk.Label(master, font=font_1)
OP2.pack()

master.mainloop()