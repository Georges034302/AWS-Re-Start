#Req: Read rain until -1
#   - determine and show the longest dry spell
#   [ a dry spell is the number of days with zero rain]
import sys

rain = int(input('rain = '))

count = 0
maxx = -sys.maxsize # smallest number in PC

while rain != -1:
    if rain == 0:
        count += 1
    else:
        maxx = max(maxx,count)
        count = 0
    rain = int(input('rain = '))
    
maxx = max(maxx,count)   
print(f'Longest dry spell = {maxx}')