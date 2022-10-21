#this function gives dialouge for the purpose of the app
def intro():
  print("Welcome to the grade calculator!")
  print("Please indicate whether you would like to calculate a weighted grade or a final grade")
  return;

def space():
  print("")
  return;

intro()
choose = input("Input one of the following (weighted/final): ")

#these set the values for the counters that will remember the grades and weights inputed to add/multiply at the end
newweight = 0
newgrade = 0
counter = 0
gcounter = 0


if choose == "final":
  print("")
  ask1 = input("Would you like find your final grade? (y/n): ")
  print("")
  if ask1 == "y":
    while ask1 == "y":
      grade1 = input("Please input your current grade: ")
      grade2 = input("Please input your target grade: ")
      grade3 = input("Please input your final exam weight: ")
      grade1 = float(grade1) * 0.01
      grade2 = float(grade2) * 0.01
      grade3 = float(grade3) * 0.01
      grade4 = 1 - grade3
      grade4 = grade4 * grade1
      grade4 = grade2 - grade4
      grade4 = grade4 / grade3
      grade4 = grade4 * 100
      space()
      print("You're required grade on the final exam is: ")
      print(grade4)
      if grade4 > 100:
        print("That percentage is highly unlikley.")
      space()
      ask1 = input("Would you like to find another final grade? (y/n): ")
      space()
      if ask1 == "n":
        print("Thank you for using the weighted grade calculator!")
elif choose == "weighted":
  space()
  ask = input("Would you like to find your average grade? (y/n): ")
  if ask == "y":
    while ask == "y":
      print("")
      grade = input("Please input your grade: ")
      weight = input("Please input the percentage weight: ")
      newweight = int(weight) * 0.01
      newgrade = int(grade) * newweight
      counter = newweight + counter
      gcounter = newgrade + gcounter

      ask = input("Do you have another grade? (y/n): ")

    space()
    print ("Thank you for using the weighted grade calculator! Here is your average grade:")
    print(gcounter)
elif ask == "n":
  print("done")
  
  