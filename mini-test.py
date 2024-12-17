import tkinter as tk

class calc:
    def __init__(self,root):
        self.root=root

        cord=[('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2)]
        self.area=tk.Label(
            root,
            bg="red",
            text="calculator",
            font=("Arial",12)

        )
        self.area.place(
            x=400,
            y=100,
            height=100,
            width=100
        )
        for (text,row,col) in cord:
            
            btn=tk.Button(root,
                        command= lambda t= text :self.press(t),
                        text=text,
                        font=("Arial",15),
                        )
            btn.place(
                x=col*100,
                y=row*100
            )
    def press(self,t):
        self.area.config(bg="blue",
                                 text=f"{t}")
        

window=tk.Tk()
window.geometry("1000x1000")
calc(window)
window.mainloop()