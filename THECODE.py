import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import carbsdata
import proteindata
import caloriesdata
import fooditems
import helpbutton
from stylings import *

root = ctk.CTk()
root.geometry('1100x650')
root.title('NUTRITION TRACKER')
root.minsize(1100,650)



##########makes the frame remain half of the window
def resize_frame(event):
    width = root.winfo_width() // 2
    height= root.winfo_height()
    frame_left.place_configure(width=width,height=height)
    frame_right.place_configure(width=width,height=height)
    
root.bind('<Configure>', resize_frame)
#######################################################

frame_left=ctk.CTkFrame(root,
                        width=root.winfo_screenwidth()//2,
                        height=root.winfo_screenheight(),
                        fg_color=frame_left_color,
                        corner_radius=0)
frame_left.place(relx=0)


frame_right=ctk.CTkFrame(root,
                         width=root.winfo_screenwidth()//2,
                         height=root.winfo_screenheight(),
                         fg_color='#888',
                         corner_radius=0)
frame_right.place(relx=0.5)

#DATA
items = fooditems.items
calories = caloriesdata.calories
protein = proteindata.protein
carbs = carbsdata.carbs

#operations
k=0
p=0
c=0

target=tk.StringVar(value='1000')
opt_var = tk.StringVar(value='apple')
mass = tk.IntVar()

def update_label(*args):
    what_u_eating = opt_var.get()
    kcal = calories[what_u_eating] * mass.get()
    pro = protein[what_u_eating] * mass.get()
    carbohydrates = carbs[what_u_eating] * mass.get()
    display_label.configure(text=f'{kcal:.1f}Kcal calories\n{pro:.1f}g of Protein\n{carbohydrates:.1f}g of carbs')

def change_mass(value):
    current_mass = mass.get()
    new_mass = current_mass + value
    if new_mass>=0:
        mass.set(new_mass)
    else:
        mass.set(0)
    update_label()

def add():
    temp=target.get()
    if temp.isnumeric()==False:
        messagebox.showwarning('ERROR','only ineger to be entered')
    elif int(temp)<1:
        messagebox.showwarning('ERROR','positive non 0 target only')
    else:
        what_u_eating = opt_var.get()
        kcal = calories[what_u_eating] * mass.get()
        pro = protein[what_u_eating] * mass.get()
        carbohydrates = carbs[what_u_eating] * mass.get()
        global k,p,c
        k=k+kcal
        p=p+pro
        c=c+carbohydrates
        progress=round((k*100/int(temp)),2)
        total_consumed.configure(text=f"THAT's a total of :\n{k:.1f}kcal calories\n{p:.1f}gm protein\n{c:.1f}gm carbs")
        canvas.delete("all")  
        if progress<=100:
            canvas.create_oval((115, 0, 415, 300), fill='yellow')
            canvas.create_arc((115, 0, 415, 300), start=90, extent=progress * 3.6, fill='red')
            canvas.create_oval((145, 30, 385, 270), fill='white')
            canvas.create_text(( 268,157), text=f"Progress = {progress}%", font=('Bahnschrift Semibold', 20))
        else:
            canvas.create_text((280,140), text=f"        GOAL\nACCOMPLISHED", font=('Bahnschrift Semibold', 30))


#widgets
helpbutton.place_the_helpbutton(frame_left)

#the frame on the top where you enter your target calories
target_frame=ctk.CTkFrame(frame_left,fg_color=frame_left_color)
target_frame.pack(pady=50)

label=ctk.CTkLabel(target_frame,text='whats your target ???',
                   font=('Bahnschrift SemiBold',30),
                   text_color='#111')
target_entry=ctk.CTkEntry(target_frame,
                          textvariable=target,
                          height=30,
                          width=100,
                          font=('Bahnschrift SemiBold',30),fg_color='#6C6',
                          text_color='#111')
label.pack(side='left')
target_entry.pack(side='right')


#the option menu conatining list of eatables
optm = ctk.CTkOptionMenu(frame_left, 
                         values=items, 
                         variable=opt_var,
                         width=220,
                         height=45,
                         text_color='#222',
                         font=('Bahnschrift SemiBold',30),
                         fg_color=widget_color,
                         button_color='#6C6',
                         dynamic_resizing=True,
                         dropdown_fg_color=widget_color,
                         dropdown_text_color='#222',
                         dropdown_font=('Bahnschrift SemiBold',15),
                         corner_radius=10)
optm.pack(pady=30)
####change the item and label changed###########
opt_var.trace("w", update_label)
#####################################

#the frame where you alter the mass --_g++
weight_frame = ctk.CTkFrame(frame_left,fg_color='#6C6')
weight_frame.pack()
minusbig = ctk.CTkButton(weight_frame, text='-10', font=('Calibri', 40),
                         height=20, width=20 + 20, command=lambda: change_mass(-10),
                         fg_color=widget_color,text_color='#111')
minusbig.grid(column=0, row=0, padx=20, pady=20)
minussmall = ctk.CTkButton(weight_frame, text='-1', font=('Calibri', 20),
                           height=10, width=20 + 10, command=lambda: change_mass(-1),
                           fg_color=widget_color,text_color='#111')
minussmall.grid(column=1, row=0, padx=20, pady=20)
weight_display = ctk.CTkLabel(weight_frame, 
                              textvariable=mass, 
                              font=('Calibri', 50),
                              text_color='#111')
weight_display.grid(column=2, row=0, sticky='nse', padx=20)
g_display = ctk.CTkLabel(weight_frame, text='g', font=('Calibri', 50),text_color='#111')
g_display.grid(column=3, row=0, sticky='nsw')
plussmall = ctk.CTkButton(weight_frame, text='+1', font=('Calibri', 20),
                          height=10, width=20 + 10, command=lambda: change_mass(1),
                          fg_color=widget_color,text_color='#111')
plussmall.grid(column=4, row=0, padx=20, pady=20)
plusbig = ctk.CTkButton(weight_frame, text='+10', font=('Calibri', 40),
                        height=20, width=20 + 20, command=lambda: change_mass(10),
                        fg_color=widget_color,text_color='#111')
plusbig.grid(column=5, row=0, padx=20, pady=20)

display_label = ctk.CTkLabel(frame_left, font=('Bahnschrift SemiBold',40),text_color='#222')
display_label.pack(pady=30)
update_label()

#the button used to update what you consumed
UPDATE_BUTTON=ctk.CTkButton(frame_left, text='UPDATE',
                            font=('Bahnschrift SemiBold',30),
                            height=40,
                            width=40,
                            command=add,
                            fg_color=widget_color,
                            text_color='#111')
UPDATE_BUTTON.pack(pady=30)


#right frame label show casing total nutrition 
total_consumed=ctk.CTkLabel(frame_right, font=('Bahnschrift SemiBold',45),text_color='#222')
total_consumed.pack(pady=50)
total_consumed.configure(text=f'')

canvas = tk.Canvas(frame_right, width=550, height=325,bg='#888',highlightthickness=0)
canvas.place(rely=0.5)


root.mainloop()