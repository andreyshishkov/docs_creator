import tkinter as tk
from windows.base_window import BaseWindow
from office_utils.table_functions import get_df, get_row
from office_utils.word_functions import create_document
from office_utils.time import get_time
from office_utils.open_doc import open_doc, get_absolute_path


class ActWindow(BaseWindow):

    def __init__(self, parent):
        super().__init__(parent, width=520, height=300)

    def create_doc(self):
        df = get_df(self.table_path)
        columns = df.columns
        row_nums = self.row_num_entry.get().split(',')
        row_nums = [int(x) for x in row_nums]

        data_rows = [list(columns)]
        for row_num in row_nums:
            data_row = get_row(df, row_num - 1)
            data_row = [str(x) for x in data_row]
            data_rows.append(data_row)

        name = f'documents/acts/{get_time()}.odt'
        create_document(name, data_rows,)

        abs_path = get_absolute_path(name)
        open_doc(abs_path)
