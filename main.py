print("Welcome to the List Generator.")
print()

print("I will display a list of numbers based on the your answers.")
print()

print("Everytime you key in your response press enter.")


def startAt():
  while True:
    print()
    try:
      startNum = int(input("Start at: "))
      print()
    except ValueError:
      print()
      print("I am expecting positive integers .")
      print()
      continue
    return startNum


def endBefore():
  while True:
    print()
    try:
      endBeforeNum = int(input("End before: "))
      print()
    except ValueError:
      print()
      print("I am expecting positive integers .")
      print()
      continue
    return endBeforeNum  


def IncrementValue():
  while True:
    print()
    try:
      incrementNum = int(input("Increment between values: "))
      print()
    except ValueError:
      print()
      print("I am expecting positive integers .")
      print()
      continue
    return incrementNum


def displayList(start, end, increment):
  for i in range(start, end, increment):
    print(i)
  

def endGame():
  while True:
    print()
    input("""Thank you for participating.
To play again please click Stop on top right page and click Run """)
    print()
    continue


if __name__=="__main__":
  start = startAt()
  end = endBefore()
  increment = IncrementValue()
  displayList(start, end, increment)
  endGame()
  