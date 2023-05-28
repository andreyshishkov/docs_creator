import tkinter as tk
from windows.act_window import ActWindow
from windows.escort_window import EscortWindow


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('520x300')
        self.title('Автоформирование документов')

        self.create_buttons()

    def create_buttons(self):
        button1 = tk.Button(
            self,
            text='АКТ',
            width=40,
            command=self.create_act_window
        )
        button1.pack(pady=10)

        button2 = tk.Button(
            self,
            text='Сопровод.',
            width=40,
            command=self.create_escort_window
        )
        button2.pack(pady=10)

        button3 = tk.Button(
            self,
            text='ОТЧЕТ',
            width=40
        )
        button3.pack(pady=10)

    def create_act_window(self):
        window = ActWindow(self)
        window.grab_focus()

    def create_escort_window(self):
        window = EscortWindow(self)
        window.grab_focus()

    def run(self):
        self.mainloop()

