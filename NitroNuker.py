import webbrowser, random, os, sys, tkinter, time

valid = 0
invalid = 0
rate = 0

chars = "qwertyuiopasdfghjklxzcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

def opencode(text):
  webbrowser.open(text, new=2)

def makecode():
    text = random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
    return ["https://discord.gift/"+text, "https://discord.com/api/v8/entitlements/gift-codes/"+text]

def importgui():
    def download():
        os.system("pip install requests")
        errorbox.destroy()
        done()
    
    def done():
        def end():
            donewin.destroy()
            sys.exit()
        
        donewin = tkinter.Tk()

        txt = tkinter.Label(donewin, text="Thank you for letting me install my packages!\nPlease restart the program for the changes to run.\n(If this box pops up again then please contact the owner of the program (jaxo@jaxo.dev) through email.)")
        btn = tkinter.Button(donewin, text="Exit", command=end)

        txt.pack()
        btn.pack()

        donewin.title("NitroNuker")
        donewin.mainloop()
    def exitwin():
        errorbox.destroy()
        sys.exit()
    
    errorbox = tkinter.Tk()

    errorbox.title("NitroNuker")

    label = "Info:\nThis program requires a module known as Requests.\nBy pressing \"Accept\" you let the program download the module.\nBy pressing \"Decline\" you accept that the program will not work, and the module will not be downloaded."
    msg = tkinter.Label(errorbox, text=label)
    btn1 = tkinter.Button(errorbox, text="Accept", command=download)
    btn2 = tkinter.Button(errorbox, text="Decline", command=exitwin)

    msg.grid(column=0, row=0)
    btn1.grid(column=1, row=1)
    btn2.grid(column=2, row=1)

    errorbox.mainloop()

def main():
    import requests

    def exit():
        sys.exit()

    window = tkinter.Tk()

    window.title("NitroNuker")

    global times

    logo = tkinter.Label(text="NitroNuker")
    newline1 = tkinter.Label(text="")
    amount = tkinter.Label(text="Amount of codes tested:")
    times = tkinter.Text(width=10, height=1)

    def madebyjaxodev():
        valid = 0
        invalid = 0
        rate = 0
        for i in range(int(times.get("1.0", "end-1chars"))):
            code = makecode()
            text = requests.get(code[1])
            print(text.text)
            if "Unknown Gift Code" in text.text:
                invalid += 1
            elif "The resource is being rate limited." in text.text:
                stuff = text.text.replace(": ", "\n")
                stuff2 = stuff.split("\n")
                delay = int(round(float(stuff2[6]))) + 1
                time.sleep(delay)
                rate += 1
            else:
                opencode(code[0])
                valid += 1
                
        validwin = tkinter.Tk()
                        
        txt = tkinter.Label(validwin, text="Done loading!\nStats:\n%s valid\n%s invalid\n%s rate limited\nProgrammed by JaxoDev. Thank you for using!" % (str(valid), str(invalid), str(rate)))

        txt.pack()

        validwin.title("NitroNuker")
        validwin.mainloop()
    
    start = tkinter.Button(text="Start Testing", command=madebyjaxodev)
    newline2 = tkinter.Label(text="")
    exitbtn = tkinter.Button(text="Exit App", command=exit)

    logo.pack()
    newline1.pack()
    amount.pack()
    times.pack()
    start.pack()
    newline2.pack()
    exitbtn.pack()
        
    window.mainloop()

def autopip():
    def cmd(txt):
        os.system(txt)
    
    user = os.environ['USERPROFILE']
    cmd("copy /data/get-pip.py C:/Users/%s" % user)
    cmd("python3 C:/Users/%s/get-pip.py" % user)

    errormake()

def errormake():
    window = tkinter.Tk()
    txt = tkinter.Label(window, text="An error occurred!")
    txt.pack()
    window.title("Error")
    window.mainloop()

try:
    import requests
except:
    try:
        importgui()
    except:
        stuff()

main()