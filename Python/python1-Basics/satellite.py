# Determine the speed (v) of a satellite at a position A(x,y) from the center of the Earth.[Refer to the Satellite Orbital Image Below]
# Read in first the (x,y) position of the satellite from STDIN and based on these values calculate and print the satellite speed (v).

# Given are the following constants:
# Gravity value G = 6.67*10-11Nm2/kg2
# Earth mass    M = 5.9722 x 10^24 kilograms
# Earth radius  R = 6,371 km


# Sample I/O:

#     Satellite distance(KM) = <value of d>
#     Satellite speed v = <speed value>
import math as m

G = 6.67*pow(10,-11)        #coefficient of gravity in Nm2/kg2
M = 5.98*pow(10,24)         #earth mass in Kg
R = 6371                    #earth radius in KM
d = input("Satellite distance(KM) = ")
D = 400 + R   #satellite distance from earth center
v = m.sqrt((G*M)/(D*1000))
print(f'Satellite speed v = {v:.3f} m/s')