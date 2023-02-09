# import the periodic table
import json

PT = open("PERIODIC-TABLE.json")
PT = json.load(PT)

# convert the formula into something that can be used by the program
def getForm(formula):
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
  depth = 0
  sub = []
  last = ""

  for i in formula:

    if i == "(":
      totalMass += mass
      mass = 0
      depth += 1

    elif i == ")":
      depth -= 1

    elif type(i) == int and depth == 0:
      if type(last) == int:
        mass = mass/last
        mass *= int(str(last)+str(i))
      else:
        mass *= i

    elif depth == 0:
      totalMass += mass
      mass = 0
      mass = PT[i]["ATOMIC MASS"]
    
    if depth != 0:
      sub.append(i)
    elif sub != []:
      sub.pop(0)
      mass = calc(sub)
      sub = []
    
    last = i
      
  totalMass += mass
  return totalMass
  
  
def main():
  formula = getForm(input("formula: "))
  mass = calc(formula)
  print(mass)

if __name__ == "__main__":

  main()
