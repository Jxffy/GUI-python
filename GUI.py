#!/usr/bin/env python
# coding: utf-8

# In[8]:


from tkinter import *
from tkinter import colorchooser as c

# window=Tk()

#label=Label(window,text='Hello THis is Jeffy',font=('arial',40,'bold'),fg='green',bg='black',relief=GROOVE,bd=10,padx=50,pady=45)
#label.pack()


# count=0
# def counter():
#     global count
#     count+=1
#     print(count)


# button=Button(window,text="Click ME!!",font=('comic sans',20,'bold'),fg='red',bg='blue'
#               ,activeforeground='red',activebackground='blue',
#               relief=RAISED,bd=20,
#               padx=10,pady=10,
#               command=counter)

# button.pack()



# entry=Entry(window,font=('arial',40),bg='black',fg='green',show='*',width=40)

# entry.pack(side=LEFT)


# def sumit():
#     username=entry.get()
#     print(username)

    
# def Del():
#     entry.delete(0,END)
    
# def back():
#     entry.delete(len(entry.get())-1,END)
# b1=Button(text='Sumit',font=('arial',15),command=sumit,bg='green')
# b1.pack(side=RIGHT)

# b1=Button(text='Delete',font=('arial',15),command=Del,bg='red')
# b1.pack(side=RIGHT)

# b1=Button(text='Back',font=('arial',15),command=back,bg='blue')
# b1.pack(side=RIGHT)







# x=IntVar()

# def dis():
#     if x.get()==1:
#         print("you Aggred")
#     elif x.get()==0:
#         print('you disagree')
# check=Checkbutton(window,text="WILL YOU AGREE",font=('arial',20,'bold')
#                   ,variable=x,onvalue=1,offvalue=0,
#                   command=dis,fg='blue',bg='red',
#                  padx=50,pady=40)
# check.pack()













# foods=['pizza','burger','fries']
# x=IntVar()

# def order():
#     if x.get()==0:
#         print("you ordered pizza")
#     elif x.get()==1:
#         print("you ordered burger")
#     elif x.get()==2:
#         print("you ordered fries")
# for i in range(len(foods)):
#     radio=Radiobutton(window,text=foods[i],variable=x,
#                       value=i,padx=50,pady=40,command=order,relief=RAISED,
#                       width=50,indicatoron=0,
#                      font=('impact',50))
#     radio.pack()









# def display():
#     print("the temperature is",scale.get(),'*C')
# scale=Scale(window,from_=100,to=0,length=600,tickinterval=10,showvalue=False,resolution=5,font=('impact',30),
#             fg='red',bg='black',troughcolor='skyblue')
# scale.pack()

# button=Button(window,command=display,padx=20,pady=15,text="Submit",font=('impact',10),activebackground='green')
# button.pack()










# listbox=Listbox(window,font=('arial',20),selectmode=MULTIPLE,
#                 fg='red',bg='black',selectbackground='yellow',selectforeground='black')
# listbox.config(height=listbox.size())
# listbox.pack()
# listbox.insert(0,'Pizza')
# listbox.insert(1,'Burger')
# listbox.insert(2,'Popcorn')
# listbox.insert(3,'Ice Cream')
# listbox.insert(4,'Coke')


# def display():
#     food=[]
    
#     for i in listbox.curselection():
#         food.append(listbox.get(i))
        
#     print("You ordered:")
#     for item in food:
#         print(item)
    
    
    
    
# button=Button(window,text='submit',command=display)
# button.pack()


# def add():
#     listbox.insert(listbox.size(),entry.get())
#     listbox.config(height=listbox.size())
    
    
# def delete():
#     for i in reversed(listbox.curselection()):
#         listbox.delete(i)
        
        
    
# entry=Entry(window)
# entry.pack()
# button1=Button(window,text='add',command=add)
# button1.pack()

# button2=Button(window,text='delete',command=delete)
# button2.pack()

# def color():
#     window.config(bg=c.askcolor()[1])

# button=Button(window,text='Change BG',command=color)
# button.pack()

















# window.title("My GUI Window")
# window.mainloop()  


# In[2]:


from tkinter import *

from tkinter import messagebox as m

# m.showinfo(title='this is a info box',message='you are a robot')
# m.showerror(title='this is a info box',message='you are a robot')
# m.showwarning(title='this is a info box',message='you are a robot')

# if m.askyesno(title='this is a info box',message='you are a robot'):
#     print("you are a robot")
# else:
#     print("you are human")

# m.askquestion(title='Alert',message="DO YOU CODE")


# In[15]:


# window=Tk()
# text=Text(window,bg='lightyellow',fg='violet',font=('arial',20),width=60,height=10)
# text.pack()

# def submit():
#     print(text.get('1.0',END))
# button=Button(window,command=submit,relief=RAISED,padx=20,pady=15,text='submit')
# button.pack()
# window.title('MY GUI WINDOW')
# window.mainloop()


# In[31]:


from tkinter import filedialog

# window=Tk()

# def file():
#     x=filedialog.askopenfilename(initialdir='C:\\Users\\ZiT\\Downloads',filetypes=('text files','*.txt'))
#     file=open(x,'r')
#     print(file.read())
#     file.close()



# button=Button(window,text='OPEN',command=file,padx=10)
# button.pack()



# window.title('MY GUI WINDOW')
# window.mainloop()


# In[3]:


# window=Tk()


# def save():
#     x=filedialog.asksaveasfile(initialdir='C:\\Users\\ZiT\\Downloads',defaultextension='.txt')
#     txt=str(text.get('1.0',END))
#     x.write(txt)
#     x.close()



# button=Button(window,text="SAVE",padx=10,command=save)
# button.pack()

# text=Text(window,font=('arial',20))
# text.pack()





# window.title('MY GUI WINDOW')
# window.mainloop()


# In[21]:


# window=Tk()


# menubar=Menu(window)
# window.config(menu=menubar)

# def open_():
#     print('the file is open')
    
# def save():
#     print("the file is saved")



# filemenu=Menu(menubar,tearoff=0,font=('arial',20))
# menubar.add_cascade(label='file',menu=filemenu)
# filemenu.add_command(label="open",command=open_)
# filemenu.add_separator()
# filemenu.add_command(label='Save',command=save)



# editmenu=Menu(menubar,tearoff=0,font=('arial',20))
# menubar.add_cascade(label='Edit',menu=editmenu)
# editmenu.add_command(label="cut",command=open_)
# editmenu.add_command(label="copy",command=open_)
# editmenu.add_command(label='paste',command=save)


# window.title('MY GUI WINDOW')
# window.mainloop()


# In[32]:


window=Tk()




def start(event):
    widget=event.widget
    widget.startX=event.x
    widget.startY=event.y
    

def motion(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startX+event.x
    y=widget.winfo_y()-widget.startY+event.y
    widget.place(x=x,y=y)



frame=Frame(window,bg='pink')
frame.pack()

frame.bind('<Button-1>',start)
frame.bind('<B1-Motion>',motion)

Button(frame,text='W',padx=10,pady=10,width=3,relief=RAISED).pack(side='top')
Button(frame,text='A',padx=10,pady=10,width=3,relief=RAISED).pack(side='left')
Button(frame,text='S',padx=10,pady=10,width=3,relief=RAISED).pack(side='left')
Button(frame,text='D',padx=10,pady=10,width=3,relief=RAISED).pack(side='left')













window.title('MY GUI WINDOW')
window.mainloop()


# In[37]:


# window=Tk()



# def open_():
#     new=Tk()
#     top=Toplevel()





# Button(window,text="ADD A NEW WINDOW",padx=10,pady=10,relief=RAISED,bd=5,command=open_).pack()














# window.title('MY GUI WINDOW')
# window.mainloop()


# In[43]:


# from tkinter import ttk

# window=Tk()

# note=ttk.Notebook(window)


# tab1=Frame(note)
# tab2=Frame(note)

# note.add(tab1,text='TAB 1')
# note.add(tab2,text='TAB 2')

# note.pack(expand=True,fill='both')


# Label(tab1,text="HELLO WORLD").pack()

# Label(tab2,text='HELLO MARS').pack()


# window.title('MY GUI WINDOW')
# window.mainloop()


# In[24]:


# from tkinter import *


# window=Tk()



# def start(event):
#     widget=widget.event
#     widget.startX=event.x
#     widget.startY=event.y
    

# def motion(event):
#     widget=widget.event
#     x=widget.winfo_x()-widget.start+event.x
#     y=widget.winfo_y()-widget.startY+event.y
#     widget.place(x=x,y=y)

    
    
# canvas=Canvas(window,height=500,width=500,bg='pink')
# canvas.place(x=0,y=0)


# canvas.bind('<Button-1>',start)
# canvas.bind('<B1-Motion>',motion)
# # canvas.create_line(0,0,500,500,fill='blue',width=5)
# # canvas.create_rectangle(500,250,100,300,fill='red',width=10)
# # canvas.create_polygon(250,0,0,300,500,300,fill='yellow')

# canvas.create_arc(0,0,500,500,fill='red',width=3,extent=180)
# canvas.create_arc(0,0,500,500,fill='white',width=3,extent=180,start=180)
# canvas.create_oval(190,190,310,310,width=5,fill='white')
# window.mainloop()





# print(dir(canvas))


# In[8]:


# from tkinter import *


# window=Tk()

# def task(event):
#     label.config(text=event.keysym)



    
    
 
# window.bind('<Key>',task)

# label=Label(window,font=('arial',100))
# label.pack()

# window.mainloop()


# In[13]:


# from tkinter import *


# window=Tk()

# def task(event):
#     label.config(text=str(event.x)+str(event.y))



    
    
# # window.bind('<Button-1>',task)
# # window.bind('<Button-2>',task)
# window.bind('<Enter>',task)

# label=Label(window,font=('arial',100))
# label.pack()

# window.mainloop()


# In[28]:


# from tkinter import *


# window=Tk()

# def start(event):
#     widget=event.widget
#     widget.startX=event.x
#     widget.startY=event.y
    

# def motion(event):
#     widget=widget.event
#     x=widget.winfo_x()-widget.start+event.x
#     y=widget.winfo_y()-widget.startY+event.y
#     widget.place(x=x,y=y)






# label=Label(window,bg='red',width=10,height=5)
# label.place(x=0,y=0)

# label2=Label(window,bg='blue',width=10,height=5)
# label2.place(x=100,y=150)

    
# canvas=Canvas(window,height=500,width=500,bg='pink')
# canvas.place(x=200,y=0)



# label.bind('<Button-1>',drag_start)
# label.bind('<B1-Motion>',drag_motion)


# label2.bind('<Button-1>',drag_start)
# label2.bind('<B1-Motion>',drag_motion)


# canvas.bind('<Button-1>',drag_start)
# canvas.bind('<B1-Motion>',drag_motion)

# frame=Frame(window,bg='pink')
# frame.pack()


# Button(frame,text='W',padx=10,pady=10,width=3,relief=RAISED).pack(side='top')
# Button(frame,text='A',padx=10,pady=10,width=3,relief=RAISED).pack(side='left')
# Button(frame,text='S',padx=10,pady=10,width=3,relief=RAISED).pack(side='left')
# Button(frame,text='D',padx=10,pady=10,width=3,relief=RAISED).pack(side='left')


# frame.bind('<Button-1>',drag_start)
# frame.bind('<B1-Motion>',drag_motion)


# window.mainloop()


# In[ ]:


from tkinter import *

def up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)



window=Tk()
window.geometry('500x500')
car=PhotoImage(file='car.png')


label=Label(window,image=car)
label.place(x=100,y=100)


window.bind('<w>',up)
window.mainloop()


# In[ ]:


#multiple 2d animations




from tkinter import *
import time


class Ball:
    def __init__(self,canvas,x,y,diameter,xvel,yvel,color):
        self.canvas=canvas
        self.image=canvas.create_oval(x,y,diameter,diameter,fill=color)
        self.xvel=xvel
        self.yvel=yvel
        
        
    def move(self):
        corr=canvas.coords(self.image)
        if corr[2]>=(self.canvas.winfo_width()) or corr[0]<0:
            self.xvel=-self.xvel
            
        if corr[3]>=(self.canvas.winfo_height()) or corr[1]<0:
            self.yvel=-self.yvel
            
            
        self.canvas.move(self.image,self.xvel,self.yvel)



window=Tk()


W=500
H=500


canvas=Canvas(window,width=W,height=H,bg='pink')
canvas.place(x=0,y=0)


volley=Ball(canvas,0,0,100,1,1,'white')
basket=Ball(canvas,0,0,50,3,2,'orange')
bowling=Ball(canvas,0,0,75,2,1,'black')


while True:
    volley.move()
    basket.move()
    bowling.move()
    window.update()
    time.sleep(0.01)




window.mainloop()


# In[ ]:


#clock program



from tkinter import *
from time import *


window=Tk()


def update():
    time=strftime('%I:%M:%S  %p')
    label.config(text=time)
    
    
    date=strftime('%B %d %Y %A')
    label2.config(text=date)

    window.after(1000,update)


label=Label(window,bg='black',fg='green',font=('arial',50))
label.pack()


label2=Label(window,bg='grey',fg='red',font=('arial',50))
label2.pack()




update()


window.mainloop()

