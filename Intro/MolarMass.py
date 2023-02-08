# import the periodic table
import json

PT = open("PERIODIC-TABLE.json")
PT = json.load(PT)

# convert the formula into something that can be used by the program
def getForm():
  formula = input("What's the formula: ")
  formula = formula.replace(" ", "")
  
  new = ""
  for i in formula:
    if not i.islower():
      new += " "
    new += i
  
  formula = new.strip()
  formula = formula.split()

  new = []
  for i in formula:
    try:
      new.append(int(i))
    except:
      new.append(i)

  return new

# calculate the molar mass
def calc(formula):
  totalMass = 0
  mass = 0
  inSub = False
  sub = ""
  
  for i in formula:

    if type(i) == int:
      mass *= i
    elif i == "(":
      totalMass += mass
      mass = 0
      inSub = True
      sub = ""
    else:
      totalMass += mass
      mass = 0
      mass = PT[i]["ATOMIC MASS"]
    
      
  totalMass += mass
  return totalMass
  
  
def main():
  formula = getForm()
  mass = calc(formula)
  print(mass)

main()
