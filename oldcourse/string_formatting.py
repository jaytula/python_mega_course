if __name__ == '__main__':
  name = 'Ardit'
  surname = 'Sulce'
  when = "today"

  print(f'Hello {name}!')
  print("Hello %s!" % name) # Since Python 3.6

  message =  "Hello %s %s" % (name, surname)
  print(message)
  
  message = f"Hello {name} {surname}. What's up {when}"
  print(message)
