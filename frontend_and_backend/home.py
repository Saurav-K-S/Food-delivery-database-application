from tkinter import*

class foodorder:
    def __init__(self,root):
        self.root=root
        self.root.title("Automated Food Ordering System")
        self.root.geometry("1550x800+0+0")

        lbl_title=Label(self.root,text="AUTO-FOOD", font=("Montserrat", 35, "bold italic"),bg="white",fg="black",bd=0)
        lbl_title.place(x=0,y=20, width=1305,height=70)
        #Label(self.root, text='ERROR\nCan\'t register please try again').pack()
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=92,width=1550,height=620)
        Label(self.root, text='WELCOME TO').pack()

if __name__=="__main__":
    root=Tk()
    obj=foodorder(root)
    root.mainloop()