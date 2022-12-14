from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("Working On Canvas")
root.geometry("900x900")

color=Label(root, text="Enter A Color :")
color.place(relx=0.6,rely=0.9, anchor=CENTER)

color_drop = ["red","blue","pink","black",""]
coordinate=["10","50","80","100","150","200","300","400","500"]
selectval= StringVar()
dropdown =ttk.Combobox(root, state="readonly", values = color_drop,width=10,textvariable = selectval)
dropdown.place(relx=0.8,rely=0.9, anchor=CENTER)

startx=Label(root, text="StartX")
startx.place(relx=0.1,rely=0.85, anchor=CENTER)
selectval1= StringVar()
dropdown2=ttk.Combobox(root, state="readonly", values = coordinate,width=10,textvariable = selectval1)
dropdown2.place(relx=0.2,rely=0.85, anchor=CENTER)

starty=Label(root, text="StartY")
starty.place(relx=0.3,rely=0.85, anchor=CENTER)
selectval2= StringVar()
dropdown3=ttk.Combobox(root, state="readonly", values = coordinate,width=10,textvariable = selectval2)
dropdown3.place(relx=0.4,rely=0.85, anchor=CENTER)

endx=Label(root, text="EndX")
endx.place(relx=0.5,rely=0.85, anchor=CENTER)
selectval3= StringVar()
dropdown4=ttk.Combobox(root, state="readonly", values = coordinate,width=10,textvariable = selectval3)
dropdown4.place(relx=0.6,rely=0.85, anchor=CENTER)

endy=Label(root, text="EndY")
endy.place(relx=0.7,rely=0.85, anchor=CENTER)
selectval4= StringVar()
dropdown5=ttk.Combobox(root, state="readonly", values = coordinate,width=10,textvariable = selectval4)
dropdown5.place(relx=0.8,rely=0.85, anchor=CENTER)


canvas=Canvas(root, width=990, height=490, bg = "white", highlightbackground="Lightgray")
canvas.pack()


def circle(event):
    oldx=dropdown2.get()
    oldy=dropdown3.get()
    newx=dropdown4.get()
    newy=dropdown5.get()
    keypress= "c"
    draw(keypress,oldx,oldy,newx,newy)
    
def rectangle(event):
    oldx=dropdown2.get()
    oldy=dropdown3.get()
    newx=dropdown4.get()
    newy=dropdown5.get()
    keypress= "r"
    draw(keypress,oldx,oldy,newx,newy)
    
def line(event):
    oldx=dropdown2.get()
    oldy=dropdown3.get()
    newx=dropdown4.get()
    newy=dropdown5.get()
    keypress= "l"
    draw(keypress,oldx,oldy,newx,newy)
    
def draw(keypress,oldx,oldy,newx,newy):
    fill_color=dropdown.get()
    if (keypress=="c"):
        draw_circle=canvas.create_oval(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if (keypress=="r"):
       draw_rectangle=canvas.create_rectangle(oldx,oldy,newx,newy,width=3,fill=fill_color)
    if (keypress=="l"):
        draw_line=canvas.create_line(oldx,oldy,newx,newy,width=3,fill=fill_color)
    
   
root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)


root.mainloop()
