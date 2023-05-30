# FYI : theese vars are there 2 store floor distance info, so it makes it easier to check!
_basements = xyz
_floorlvl = zyx
_2nd_floor = yzx

def getdistance():
  # Check the current distance, use floor levels
  return distance

def pickfloor():
  # takes user input, then raises or lowers depending on input and elevator state
  print("Choices : ") # Choiced would be : {1:_basements, 2:_floorlvl, 3:_2nd_floor , 0: exit}
  pfloor = int(input("Please pick a floor number!"))
  return pfloor

 
def _raise():
  # Raises elevator
  if pfloor > distance:
    print("Raise the roof") 
def _lower():
  # Lower elevator
  if pfloor < distance
  print("Raise the floor")
  
def move():
  # Move Elevator to distance of pickfloor
  if pfloor > distance:
    # Move Elevator up (Motor Reverse?)
  elif: distance > pfloor
  	# Move Elevator Down (Motor Foward?)
  else: print(" Stairway to Heaven ")

def main():
	getdistance()
    while = true:
      getdistance()
      pickfloor()
      _raise() # Combine raise and lower?
      _floor() # problably!
      move()

main()
