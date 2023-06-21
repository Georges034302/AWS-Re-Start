# From Python 3.10 onward match is available
# match <criteria>:
#   case <option 1>: <code 1>
# ..............
#   case <option n>: <code n>

code = int(input("HTTP Code: "))

match code:
    case 200: print("Success")
    case 404: print("Page not found")
    case 500: print("Server error")
    case _ : print("Unknown code")
