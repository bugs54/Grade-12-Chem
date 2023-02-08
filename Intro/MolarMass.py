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
  depth = 0
  sub = []
  
  for i in formula:

    if i == "(":
      totalMass += mass
      mass = 0
      depth += 1
    elif i == ")":
      depth -= 1
    elif type(i) == int and depth == 0:
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
      
  totalMass += mass
  return totalMass
  
  
def main():
  formula = getForm()
  mass = calc(formula)
  print(mass)

if __name__ == "__main__":
  # import the periodic table
  import json

  PT = open("PERIODIC-TABLE.json")
  PT = json.load(PT)
  
  main()
