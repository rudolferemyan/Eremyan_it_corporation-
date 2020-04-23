import pyowm
a = input("Какой город вас интересует?")
owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc")

observation = owm.weather_at_place(a)
w = observation.get_weather()
temperature = w.get_temperature('celsius')["temp"]
print(temperature)
print(w.get_detailed_status())