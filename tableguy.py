#!/usr/bin/env python3

from tkinter import Tk, Entry, Button, Label, Text, END

'''
chartguy.py
-----------

'''

class Window(object):

    def __init__(self, master):
        
        self.master = master

        self.label_cols = Label(self.master, text='Number of Columns')
        self.label_rows = Label(self.master, text='Number of Rows')
        
        self.entry_cols = Entry(self.master)
        self.entry_rows = Entry(self.master)

        self.btn = Button(self.master, text='Generate', command=self.create_table)
        
        self.out = Text(self.master)
        self.out.config(width=100)

        self.label_cols.grid(row=0, column=0, sticky='E')
        self.entry_cols.grid(row=0, column=1, sticky='W')

        self.label_rows.grid(row=1, column=0, sticky='E')
        self.entry_rows.grid(row=1, column=1, sticky='W')

        self.btn.grid(row=2, column=0, columnspan=2)
        self.out.grid(row=3, column=0, columnspan=2)

    def create_table(self):

        table = ''

        cols = self.entry_cols.get()
        rows = self.entry_rows.get()

        if (rows.isdigit() and int(rows) > 0) and (cols.isdigit() and int(cols) > 0):

            for r in range(int(rows) + 2):

                if r is not 0:
                    table = table + '\n'

                for c in range(int(cols) + 1):

                    if r is 1 and c is not int(cols):
                        table = table + '|---'
                    else:
                        table = table + '|   '

        self.out.delete(1.0, END)
        self.out.insert(END, table)

root = Tk()
root.title('ChartGuy')
m = Window(root)
root.mainloop()
