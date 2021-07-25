
#Debugger helps the developer to keep track of thye code segments while it's executing

import pdb

def sequencePrinter(n):
    for item in range (n):
        pdb.set_trace() #set the tracker
        print(item)
    return

sequencePrinter(3)

#debugger options: 1) c: continue, 2) q: quit debugging, 3) p: print, 4) locals(): print all local variables, 5) list: get the current execution portion, 6) h: get all the functions
