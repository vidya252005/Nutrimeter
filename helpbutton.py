import customtkinter as ctk
def place_the_helpbutton(frame_name):

    def help():
        window=ctk.CTk()
        window.geometry('400x400')
        window.title('INSTRUCTIONS')
        label=ctk.CTkLabel(window,text='INSTRUCTIONS:')
        label.pack()
        window.mainloop()

#WIDGETS

    help_button=ctk.CTkButton(frame_name, text='help',
                            font=('Bahnschrift SemiBold',30),
                            height=40,
                            width=40,                            
                            fg_color='#9F9',
                            text_color='#111',command=help)
    help_button.place(relx=0,rely=0)