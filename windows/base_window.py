import tkinter as tk
import tkinter.filedialog as fd


class BaseWindow(tk.Toplevel):

    def __init__(self, parent, width=800, height=500, title='Автоформирование акта',):
        super().__init__(parent)
        self.title(title)
        self.geometry(f'{width}x{height}')

        self.row_number = 0
        self.table_path = 0

        self.row_num_entry = None

        self.create_row_num_entry()
        self.choose_table_button('Выберите электронную таблицу')
        self.create_doc_button()

    def create_row_num_entry(self):
        frame = tk.Frame(
            self
        )
        label = tk.Label(
            frame,
            text='Выберите номер записи:',
            width=40
        )
        label.pack()
        self.row_num_entry = tk.Entry(
            frame,
            width=45
        )
        self.row_num_entry.pack()

        frame.pack(pady=20)

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()

    def choose_table_button(self, title):
        button = tk.Button(
            self,
            text=title,
            command=self.choose_table
        )
        button.pack(pady=20)

    def create_doc_button(self):
        button = tk.Button(
            self,
            text='Создать документ',
            command=self.create_doc
        )
        button.pack()

    @staticmethod
    def _choose_file():
        filetypes = (
            ('OpenDocument', '*.odt'),
            ('Электронная таблица', '*.ods'),
            ("Любой", "*"),
        )
        filename = fd.askopenfilename(title="Открыть файл", initialdir="/",
                                      filetypes=filetypes)
        return filename

    def choose_table(self):
        table_path = self._choose_file()
        self.table_path = table_path

    def create_doc(self):
        pass
