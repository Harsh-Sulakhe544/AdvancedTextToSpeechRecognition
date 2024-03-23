import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox
import pyttsx3
import os

root =Tk() 

root.title("Text to speech") # title of the application
root.geometry("900x450+200+200") # 900 is breadth and 450 is length (that 200 is the distance to place that speaker logo.png (from x and y axis)) 
root.resizable(False,False)
root.configure(bg="#305065") # to change the color of entire box(that green big -huge box )


engine=pyttsx3.init()

def exit_app():
    root.destroy()

# to use speak button :
def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices') # this line helps engine (computer to speak )
    
    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        
        else : # for the Female voice 
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
            
    if(text): # if we wrote text only 
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
            
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
            
        else :
            engine.setProperty('rate',60)
            setvoice()        

# to use download button                 
def download():
    text=text_area.get(1.0,END).strip()
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')
    
    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory() # to ask which directory you want to save your file 
            os.chdir(path)  # save the file to specified location in to your os 
            engine.save_to_file(text,'text.mp3') # to save to particular file in the format of mp3 
            engine.runAndWait()
        
        else :
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            
    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
            
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
            
        else :
            engine.setProperty('rate',60)
            setvoice()  

        # Ask for directory only if there is text to save
        path = filedialog.askdirectory()
        if path:
            try:
                os.chdir(path)
                engine.save_to_file(text, 'text.mp3')
                engine.runAndWait()
            except OSError as e:
                # Handle specific OSError if needed, e.g., display a messagebox
                messagebox.showinfo("Error", f"Error saving file: {e}")
        else:
            print("Saving cancelled.")
    else:
        # Display a message on the application screen
        messagebox.showinfo("Error", "No text to save.")    
        
              
# icon 
image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)

#top frame : frame just below top is (white) 
Top_frame=Frame(root,bg="white",width=900,height=100) 
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="speaker logo.png") # that logo in white text (just below the top frame)
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)

# tHE HEADING (SPEECH TO TEXT) 
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

# to make a (square white box) inside that (green big box )
text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD) # wrap => when line is filled (automatically we can go to the next line )
text_area.place(x=10,y=150,width=500,height=250) # place a object on ui  

# to label above the geeder_combobox as VOICE and to label above the speed_combobox as  SPEED  
Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)


#to create box with two options(we use combobox) => male and female
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male') # by default we want to set it to Male

# we also want to change the speed of the speaker => again we use different combobox
speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal') # by default we want to set it to Normal

# to create a speak button with the image 
imageicon=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,font="arail 14 bold",command=speaknow)
btn.place(x=550,y=289)

# we also want to create a save button (to save and listen in whenever we want ): 
imageicon2=PhotoImage(file="download.png")
save=Button(root,text="Save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arail 14 bold",command=download)
save.place(x=730,y=289)

# Create an "Exit" button, x = 1.0 -> right-side , rel-y -bottom , se-soth-east
exit_button = Button(root, text="Exit", width=20, command=exit_app)
exit_button.place(relx=1.0, rely=1.0, anchor='se')


root.mainloop()