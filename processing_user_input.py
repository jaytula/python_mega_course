def weather_condition(temperature: float) -> str:
  if temperature > 7:
    return "Warm"
  else:
    return "Cold"

if __name__ == '__main__':
  the_temperature = float(input('Enter temperature: '))
  print(weather_condition(the_temperature))

