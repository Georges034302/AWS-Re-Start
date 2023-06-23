# Calculate and show the distance between 2 points
# Calculate and show the perimeter, area, volume with radius r
# Define the system switcher method to provide users with choices:
# (d) - distance
# (g) - circle geometry
# (x) - exit

import math as m 

def distance(x1,y1,x2,y2):
    return m.sqrt(pow(x1-x2,2) + m.pow(y1-y2,2))

def show_distance():
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    print(f"Distance between ({x1},{y1}) and ({x2},{y2}) = {distance(x1,y1,x2,y2)}")
    
# function returning 3-values
def circle_geo(r):
    p = 2*m.pi*r 
    a = m.pi*pow(r,2)
    v = (4/3)*m.pi*m.pow(r,3)
    return p, a, v 

def show_circle_geo():
    r = int(input("r = "))
    p, a, v = circle_geo(r)
    print(f"Perimeter = {p:.2f}")
    print(f"Area = {a:.2f}")
    print(f"Volume = {v:.3f}")

def switch(choice):
    if choice == "d":
        show_distance()
    elif choice == "g":
        show_circle_geo()
    else:
        print("Unknown Command!")
        
def run():
    choice = input("Command (d/g/x): ")
    while choice != "x":
        switch(choice)
        choice = input("Command (d/g/x): ")
    print("Thank you")

run()