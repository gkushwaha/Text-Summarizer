from tkinter import*
from tkinter import BOTH, END, LEFT
from tkinter.filedialog import *
from tkinter import StringVar
from mainprogram import*

class Window(Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.add_stuff()
		self.pack()
		
	def add_stuff(self):
		self.lab1 = Label(self)
		self.lab1["text"]="Please Enter a Valid URL \n for Text Summary"
		self.lab1["font"]="red"
		self.lab1["pady"]=10
		self.lab1.grid(row=0, column=0)

		self.entry1 = StringVar()
		self.entry2 = StringVar()

		self.lab2 = Entry(self)
		self.lab2["textvariable"] = self.entry1
		self.lab2["bg"] = "white"
		self.lab2["bd"] = 5
		#self.lab2["text"]="Please Enter No. of Sentences \n You Want To See Your Summary "
		self.lab2.grid(row=1, column=0)

		self.lab3 = Label(self)
		self.lab3["text"]="Please Enter No. of Sentences \n You Want To See Your Summary"
		self.lab3["font"]="red"
		self.lab3["pady"]=10
		self.lab3.grid(row=0, column=1)

		self.lab4 = Entry(self)
		self.lab4["bg"] = "white"
		self.lab4["bd"] = 5
		self.lab4["textvariable"] = self.entry2
		self.lab4.grid(row=1, column=1)

		self.but1 = Button(self)
		self.but1["text"]="Select"
		self.but1.grid(row=1, column=2)
		self.but1["font"]="red"
		self.but1["activebackground"]="silver"
		self.but1["pady"]=5
		self.but1["padx"]=5
		#self.but1.grid( row=1, column=2)
		self.but1["command"]=self.output

		
		self.but2 = Button(self)
		self.but2["text"]="Refresh"
		#self.but2.grid(row=1, column=2)
		self.but2["font"]="red"
		self.but2["activebackground"]="silver"
		self.but2["pady"]=5
		self.but2["padx"]=5
		self.but2.grid( row=1, column=3)
		self.but2["command"]=self.refresh
		


		self.lb = Text(self)
		self.lb["height"]=30
		self.lb["width"]=70
		self.lb["bd"] = 5
		self.lb["font"] = 40
		self.lb.grid(row = 4, column=2)
		self.lb["state"]="disable"

	def output(self):
		summary=[]
		
		self. value1= self.entry1.get()
		self.value2=self.entry2.get()
		self.lb["fg"] = "Red"
		self.lb["state"]="normal"
		self.lb.insert(INSERT, "This is " + self.value2 + " sentence summary of " + self.value1)
		self.lb.insert(INSERT, '\n')
		self.lb.insert(INSERT, "___________________________________________________________________")
		self.lb.insert(INSERT, '\n')
		themain=mainprogram(self.value1, self.value2)
		summary, title=themain.final()

		self.final_output(summary, title)

	def final_output(self, summary, title):
		self.lb.insert(INSERT, '\n')
		self.lb.insert(INSERT, "Title: " + title)
		self.lb.insert(INSERT, '\n')
		self.lb.insert(INSERT, "_____________________________________________________________________")
		self.lb.insert(INSERT, '\n')
		self.lb.insert(INSERT, '\n')
		
		for  i in summary:
			self.lb.insert(INSERT, i)
			self.lb.insert(INSERT, '\n')
			self.lb.insert(INSERT, '\n')

		self.lb["state"]="disable"
		self.but1["state"]="disable"

	def refresh(self):
		self.lb["state"]="normal"
		self.lb.delete('1.0', END)
		self.lb["state"]="disable"
		self.lab2.delete(0, END)
		self.lab4.delete(0, END)
		self.but1["state"]="normal"


r=Tk()
app = Window(r)
app.master.title("Simple Text Summarization")
#r.geometry("1100x700")
r.mainloop()