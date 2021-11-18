 #!/usr/bin/env python

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

class In2Out_Rule():
    def __init__(self, input, output, state={}) -> None:
        self.input = input
        self.output = output
        self.state = state
    def updateState(self, state):
        self.state = state
    def activate(self):
        return self.output, self.state
    def isTrue(self, message):
        if message == self.input:
            return True

class In2OutAndState_Rule(In2Out_Rule):
    def __init__(self, input, output, state={}, state_change=None) -> None:
        self.state_change = state_change
        super().__init__(input, output)
    def updateState(self, state):
        self.state = state
    def activate(self):
        self.state = self.state_change(self.state)
        return self.output, self.state

class In2Code_Rule():
    def __init__(self, input, code, state={}) -> None:
        self.input = input
        self.code = code
    def updateState(self, state):
        self.state = state
    def activate(self):
        result = None
        if isinstance(self.code, list):
            for c in self.code:
                result = eval(c)
        else:
            result = eval(self.code)
        return result, self.state
    def isTrue(self, message):
        if message == self.input:
            return True