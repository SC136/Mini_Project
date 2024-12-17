import tkinter as tk

class convert:
    def __init__(self,root):
        self.root=root

        self.select=tk.StringVar()
        self.select.set("Select Conversion")
        self.drop=tk.OptionMenu(root,
                                self.select,
                                "F to C ","C to F",
                                command=self.click)
        self.drop.place(x=100,
                        y=200,
                        height=100,
                        width=300
                        )
        
        self.put=tk.Entry(root,
                            bg="red")
        self.put.place(x=100,
                    y= 100,
                    height=50,
                    width=200)
        self.answer=tk.Label(root,
                            bg="Blue",
                            fg="white")
        self.answer.place(x=500,
                        y=200,
                        height=100,
                        width=300)
    def click(self,sel_opt):
        x=float(self.put.get())
        
        if sel_opt=="F to C ":
            self.answer.config(text=f"{(x-32)/1.8} C")
            
        elif sel_opt=="C to F":
            self.answer.config(text=f"{(x*1.8)+32} F")
        

a=tk.Tk()
a.geometry("1000x1000")
convert(a)
a.mainloop()