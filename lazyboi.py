import pyperclip
import pyautogui
import os,sys
import asyncio

# Handy tool for defacers
# IDK why I did use asyncio, it does nothing it this code it stays SYNC :P Just for fun you know
try:
    while True:
        gui = pyautogui.prompt(text="Enter folder name",title="Locate Folders",default=None)
        if gui == None:
            print("Please give us an folder name you want to load, if you wanna exit type exit")
        elif gui.lower() == "exit":
            sys.exit(0)
        else:
            if os.path.isdir(gui):
                break
            else:
                print("This folder does not exist, if you wanna exit type exit")
except:
    sys.exit(0)

async def Main(g = gui):
    SHELLfiles = os.listdir(g)
    AmountShells = len(SHELLfiles)
    c = 1
    for files in SHELLfiles:
        print("{} -> {}".format(c,files+"\n"))
        c+=1
    
    menu = True
    fix = 1
    while menu:
        option =  input("$[Choose]-> ")
        if option == "exit":
            sys.exit(0)
        else:
            pass
        try:
            validity = True
        except:
            validity = False
            print("Invalid , this file does not exist")
        if validity:
            chosen = SHELLfiles[int(option)-fix]
            smartUtil = chosen.split('.')
            try:
                with open(f"{gui}/{smartUtil[0]}.{smartUtil[1]}","r")as f:
                    pyperclip.copy(f.read())
                    await asyncio.sleep(0)
                    print("Successfull copied")
            except:
                print("This file does not exist or i do not have access to open and read it. Check file formatting.")
        
        else:
            pass   

async def Startup():
    await asyncio.gather(
        Main()
    )

startLP = asyncio.new_event_loop()
startLP.run_until_complete(Startup())
