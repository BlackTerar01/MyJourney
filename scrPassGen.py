from tkinter import *
from random import randint
from tkinter.filedialog import asksaveasfile
from tkinter import ttk
from tkinter import filedialog

main = Tk()
main.title("Secure password generator")
main.geometry("600x400")
main.config(bg="aqua")
message = "Welcome to secure password generator!"

title = Label(main, text="Welcome to secure password generator!")
title.config(font=("Courier", 20, "bold"), bg="aqua", )
title.pack(pady=30)
# titleText = Text(main, height = 5, width=52)
# titleText.pack()

pwdChar = chr(randint(33, 126))

#Function to create new password
def newPass():
    entryOfPwd.delete(0, END)

    lenOfPwd = int(entryBox.get())

    global generatedPwd
    generatedPwd = " "

    for x in range(lenOfPwd):
        generatedPwd += chr(randint(33, 126))

    entryOfPwd.insert(0, generatedPwd)

#Function to copy the generated password
def copyToClipboard():
    main.clipboard_clear()
    main.clipboard_append(entryOfPwd.get())
    pass


# def save():
#     files = [('All Files', '*.*'), 
#              ('Python Files', '*.py'),
#              ('Text Document', '*.txt')]
#     file = asksaveasfile(filetypes = files, defaultextension = files)

#Function to open a file and append the new password to the file  
def openTxt():
    textFile = filedialog.askopenfilename()
    textFile = open(textFile, 'a')
    textFile.write(generatedPwd + "\n")
    textFile.close()

# Label frame
labelFrame = LabelFrame(main, text="How many characters would you like?", bg="yellow")
labelFrame.pack(pady=20)

# Create entry box to designate number of characters
entryBox = Entry(labelFrame, font=("Helvetica", 24))
entryBox.pack(pady=20, padx=20)

#Label fram for output
returnFrame = LabelFrame(main, text="Generated password:", bg="yellow")
returnFrame.pack(pady=20)

# Create entry box for our returned password
entryOfPwd = Entry(returnFrame, text="", font=("Helvetica", 24), bd=0, bg="aqua")
entryOfPwd.pack(pady=20)

# Create a frame for the button
buttonFrame = Frame(main, bg="aqua")
buttonFrame.pack(pady=10)

# Create buttons
generatorButton = Button(buttonFrame, text="Generate Strong Password", command=newPass)
generatorButton.grid(row=0, column=0, padx=10)

clipperButton = Button(buttonFrame, text="Copy to clipboard", command=copyToClipboard)
clipperButton.grid(row=0, column=1, padx=10)

saveButton = Button(buttonFrame, text = 'Save', command=openTxt)
saveButton.grid(row=0, column=2, padx = 10)

main.mainloop()


