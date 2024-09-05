# Creating graphics
from tkinter import *   # using 'from' keyword to import tkinter module, which is the fastest and easiest way to create GUI applications.
from tkinter import ttk, Button    #imports the ttk module (providing themed widgets) and Button class for creating buttons.
from googletrans import Translator,LANGUAGES     # Imports the Translator class and LANGUAGES dictionary from the googletrans library


# here we define the function which call the Translator function
def change(text="type",src="English",dest="Nepali"):
    text1 = text    #storing the data of text to be translated in text1
    src1 = src      #storing the data of src in src1
    dest1 = dest    #storing the data of dest in dest1
    trans = Translator()    #Creates an instance of the Translator class.
    trans1 = trans. translate(text,src=src1,dest=dest1)    #creating a variable trans1 which Uses the translate method to translate the text from src1 to dest1.
    return trans1.text   # Returns the translated text.



def data():
    s = comb_sor.get() #Get the source languages from the combo boxes.
    d = comb_dest.get() #Get the destination languages from the combo boxes.
    masg = Sor_txt.get(1.0,END)  #Retrieves the text from the source text box.
    textget = change(text = masg, src = s, dest = d)  #Stores the translated text returned by the change function.
    dest_txt.delete(1.0,END) #Clears the destination text box before inserting the new text.
    dest_txt.insert(END,textget) # Clears the destination text box before inserting the new text.



root = Tk() #root is the object which creates the main window (or root window) of the application.
root.title("Translator")
root.geometry("500x700")  # Sets the dimensions of the window to 500x700 pixels.
root.config(bg='light Blue')

# icon
image_icon = PhotoImage(file="google.png")  #Loads an image file to be used as the window icon.
root.iconphoto(False, image_icon)  #Sets the icon of the window to the loaded image.

# Creating label for Translator
lab_txt=Label(root,text="Translator", font=("Times New Roman",40,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

# Creating frame
frame = Frame(root).pack(side=BOTTOM)  #pack is used for placement

#Creating label for Source Text
lab_txt=Label(root,text="Source Text", font=("Times New Roman",20,"bold"),fg="Black",bg="light Blue")
lab_txt.place(x=100,y=100,height=20,width=300)


#Creates a Text widget where users can input the text they want to translate.
Sor_txt =Text(frame,font=("Times New Roman",40,"bold"),wrap=WORD)   #Ensures that words are wrapped to the next line instead of being split.
Sor_txt.place(x=10,y=130,height=150,width=480)  #Positions the text box within the frame.


#creating combo box
list_text = list(LANGUAGES.values())   #Converts the LANGUAGES dictionary values (language names) into a list.

comb_sor = ttk.Combobox(frame,value=list_text) # comb_sor Creates a combo box for selecting the source language.
comb_sor.place(x=10,y=300,height=40,width=150)  #Positions the combo box within the frame.
comb_sor.set("English")   #setting the value

# Creating the button
button_change = Button(frame,text="Translate",relief=RAISED,command=data)  #Creates a "Translate" button. When clicked, it calls the data function to perform the translation.
button_change.place(x=170,y=300,height=40,width=150)  # RAISED gives the button a raised appearance.

#creating the combo box for destination
comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("English")

# test box for destination
lab_txt = Label(root, text="Destination Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="light Blue")
lab_txt.place(x=100, y=380, height=20, width=300)  # Adjusting the y position of the label

dest_txt = Text(frame, font=("Times New Roman", 40, "bold"), wrap=WORD)
dest_txt.place(x=10, y=420, height=150, width=480)  # Adjust the y position of the text box


# Footer Label
footer_label = Label(root, text="Powered by Google Translate", font=("Helvetica", 12), bg="#f2f2f2", fg="gray")
footer_label.pack(side=BOTTOM, pady=20)   #This uses the pack geometry manager to place the label in the window.

root.mainloop()   #Starts the Tkinter event loop, which keeps the window open and responsive until the user closes it.
