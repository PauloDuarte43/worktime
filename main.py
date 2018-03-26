#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from Tkinter import *
from datetime import datetime, timedelta


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("WorkTime")
        self.root.resizable(0, 0)
 
        self.input_start_time_info = Label(text="Inicio")
        self.input_start_time_info.grid(row=0, column=0)
        self.input_start_time = Entry()
        self.input_start_time.insert(END, "08:30")
        self.input_start_time.grid(row=0, column=1)

        self.label_now_info = Label(text="Agora")
        self.label_now_info.grid(row=1, column=0)
        self.label_now = Label(text="")
        self.label_now.grid(row=1, column=1)
        
        self.time_worked_info = Label(text="Tempo trabalhado")
        self.time_worked_info.grid(row=2, column=0)
        self.time_worked = Label(text="")
        self.time_worked.grid(row=2, column=1)
        
        self.remaining_working_time_info = Label(text="Tempo restante")
        self.remaining_working_time_info.grid(row=3, column=0)
        self.remaining_working_time = Label(text="")
        self.remaining_working_time.grid(row=3, column=1)

        self.end_work_time_info = Label(text="Fim do turno")
        self.end_work_time_info.grid(row=4, column=0)
        self.end_work_time = Label(text="")
        self.end_work_time.grid(row=4, column=1)

        self.update_clock()
        self.update_work_time()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label_now.configure(text=now)
        self.root.after(1000, self.update_clock)

    def update_work_time(self):
        text_time_worked = ""
        text_remaining_working_time = ""
        text_end_work = ""
        try:
            t = datetime.strptime(self.input_start_time.get(), "%H:%M")
        except ValueError:
            t = datetime.strptime("08:30", "%H:%M")

        t_now = datetime.now()
        total_work_delta = timedelta(hours=9, minutes=30)
        delta_now = timedelta(hours=t_now.hour, minutes=t_now.minute, seconds=t_now.second)
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)

        total_work_time = delta_now - delta  

        text_time_worked = str(total_work_time)
        text_remaining_working_time = str(total_work_delta - total_work_time)
        text_end_work = delta + total_work_delta

        self.time_worked.configure(text=text_time_worked)
        self.remaining_working_time.configure(text=text_remaining_working_time)
        self.end_work_time.configure(text=text_end_work)
        self.root.after(1000, self.update_work_time)

if __name__ == "__main__":
    app=App()

