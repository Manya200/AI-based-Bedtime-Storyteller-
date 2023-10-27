import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from Story_maker import printinfo
#import Story_Reader
import subprocess
from tkinter import filedialog
root = tk.Tk()
root.title("Bedtime Story teller")
root.iconbitmap('') #place icon here

#background image setup

root.geometry('1366x768')
#root.configure(background='#0096DC')




# Create a canvas
canvas = tk.Canvas(root, bg='#0096DC')
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#bgimage
bg_image = Image.open("BEITproject.png")
bg_image = bg_image.resize((1366, 768))
bg_img = ImageTk.PhotoImage(bg_image)
img_label = Label(canvas, image=bg_img)
img_label.place(relwidth=1, relheight=1)

#heading
#headimg=Image.open("headbg.jpeg")
#heading_img= ImageTk.PhotoImage(headimg)
"""text_label = Label(canvas, text="", fg='white' ,font=('Algerian', 50), compound=tk.CENTER)
text_label.grid(row=0 , column= 0, columnspan=2,sticky="n")"""
#text_label.place(relx=0.5, rely=0.5)


#take input
#input Main character
"""mainChar_label= tk.Label(canvas, text="", fg='white',font=('Algerian', 20))
mainChar_label.grid(row=3,column=0,pady=(20,5),sticky="w")"""
character1_name = tk.Entry(canvas,width=50)
#character1_name.grid(row=3,column=1, ipady=6)
character1_name.place(x=874,y=141,width=400, height=30)

"""mainChar_type= tk.Label(canvas, text="", fg='white' )
mainChar_type.grid(row=4, column=0, pady=(20,5),sticky="w")
mainChar_type.config(font=('Algerian', 20))"""
character1_type = tk.Entry(canvas,width=50)
#character1_type.grid(row=4, column=1, ipady=6)
character1_type.place(x=874,y=206,width=400, height=30)

#input2
"""Char2_label= tk.Label(canvas, text="", fg='white')
Char2_label.grid(row=5 , column=0 , pady=(20,5),sticky="w")
Char2_label.config(font=('Algerian', 20))"""
character2_name = tk.Entry(canvas,width=50)
#character2_name.grid(row=5 , column= 1, ipady=6)
character2_name.place(x=874, y=286,width=400, height=30)

"""Char2_type= tk.Label(canvas, text="", fg='white')
Char2_type.grid(row=6 , column=0, pady=(20,5),sticky="w")
Char2_type.config(font=('Algerian', 20))"""
character2_type = tk.Entry(canvas,width=50)
#character2_type.grid(row=6 , column=1, ipady=6)
character2_type.place(x=874, y=359,width=400, height=30)
#input3
"""venue_label=tk.Label(canvas, text="",fg='white')
venue_label.grid(row=7 , column=0, pady=(20,5),sticky="w")
venue_label.config(font=("Algerian",20))"""
venue= tk.Entry(canvas,width=50)
#venue.grid(row=7 , column=1, ipady=6)
venue.place(x=874, y=427,width=400, height=30)
#input4
"""genre_label= tk.Label(canvas, text="",fg='white')
genre_label.grid(row=8 , column=0, pady=(20,5),sticky="w")
genre_label.config(font=("Algerian",20))"""
genre= tk.Entry(canvas, width=50)
#genre.grid(row=8 , column=1, ipady=6)
genre.place(x=874, y=496,width=400, height=30)

def runall():
    printinfo(character1_name.get(),character1_type.get(),character2_name.get(),character2_type.get(),venue.get(),genre.get())
    subprocess.run( ["python", "Story_maker.py"] )

"""def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print("Selected folder:", folder_path)
    else:
        print("No folder selected.")"""


store_run_button = tk.Button(canvas, text="Submit", command=runall)
#store_run_button.grid(row=10 , column=0, pady=(20,10),columnspan=2)
store_run_button.place(x=669,y=554)
store_run_button.config(font=("Algerian",20))


"""select_button = tk.Button(canvas, text=" Browse",command= select_folder)
select_button.pack(pady=(20,10))
select_button.config(font = ("Algerian",20))
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)"""

root.mainloop()
