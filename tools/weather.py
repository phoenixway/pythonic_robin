import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    client = python_weather.Client()

    # fetch a weather forecast from a city
    weather = await client.find("Kyiv")

    # returns the current day's forecast temperature (int)
    print("Temperature now is {}C".format(weather.current.temperature))

    # get the weather forecast for a few days
    print("Forecast:")
    for forecast in weather.forecasts:
        print(str(forecast.date.strftime("%d-%m-%Y")), forecast.sky_text, '{}C'.format(str(forecast.temperature)))

    # close the wrapper once done
    await client.close()

def get_weather():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())