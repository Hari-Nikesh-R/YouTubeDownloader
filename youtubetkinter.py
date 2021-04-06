''' Youtube downloader using python'''

#tkinter is the python GUI to execute the code in a user friendly mode
#It is the syntax means that we are impoting everything from tkinter module
from tkinter import *

import webbrowser
#We are importing Webbrowser to have access through the website.

def yt():
    n=e.get()
    #getting input from Entry

    l=n.split(".")
    #spliting the string with respect to "."

    l[1]=l[1]+"cp"    
    url=""
    #creating Empty string.

    for i in l:
        k="."
        url+=i
        url+=k
    leng=len(url)     
    link=url[:leng-1]
    #for removing extra "." at the last of the string.

    #opening the url in webbrowser
    webbrowser.open(link)    

    l2=Label(m, text="Your Video is downloaded")
    l2.grid(row=2, column=1)

#Here m is the root variable that holds the tkinter window.
m=Tk()

#Giving Title of the application window of tkinter 
m.title("YouTubeDownloader")

v=StringVar()    #Declaring String variable to pass and get value between functions

l=Label(m, text="Copy the link") #Labels are added to make the users to have easy access on the code

e=Entry(m)
#To get Entry from the user

#Button named Download is initialized with the command yt function in it.
b=Button(m, text="Download", width=25, command=yt)
                                        #Directs to the function yt

#grid are used to arrange the button, Label, Entry in a tkinter window
l.grid(row=1, column=0)
e.grid(row=1, column=1)
b.grid(row=1, column=2)


m.mainloop()
#mainloop() completes the code only then tkinter window opens.
