import MolarMass

AVO = 6.02 * 10**23

def molesToAtoms(moles):
  return moles * AVO

def molesToWeight(moles, formula):
  formula = MolarMass.getForm(formula)
  M = MolarMass.calc(formula)

  return moles * M

def atomsToMoles(atoms):
  return atoms / AVO

def atomsToWeight(atoms, formula):
  n = atomsToMoles(atoms)
  return molesToWeight(n, formula)

def weightToAtoms(weight, formula):
  n = weightToMoles(weight, formula)
  return molesToAtoms(n)

def weightToMoles(weight, formula):

  formula = MolarMass.getForm(formula)
  M = MolarMass.calc(formula)

  return weight/M

def main():
  atoms = 5.67*10**23
  form = input("formula: ")
  print(atomsToWeight(atoms, form))

if __name__ == "__main__":
  # import the periodic table
  import json

  PT = open("PERIODIC-TABLE.json")
  PT = json.load(PT)
  
  main()