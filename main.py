import csv
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.ttk as ttk


class TabellengeneratorGui:
    def __init__(self, root):
        self.data = []
        self.filename = ''
        self.delimiter = tk.StringVar(value=';')
        main_frame = ttk.Frame(root)
        main_frame.grid()
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(column=0, row=0, rowspan=2)
        open_btn = ttk.Button(btn_frame, text="Öffnen", command=self.open_file)

        open_btn.grid(column=0, row=0)
        convert_btn = ttk.Button(btn_frame, text="LaTeX")
        convert_btn.grid(column=0, row=1)
        delimiter_entry = ttk.Entry(btn_frame, textvariable=self.delimiter, width=1)
        delimiter_entry.grid(column=1, row=0)
        latex_label = ttk.Label(main_frame, text="LaTex")
        latex_label.grid(column=1, row=2)
        info_frame = ttk.LabelFrame(main_frame)
        info_frame.grid(row=0, rowspan=2, column=1)
        self.info_label_1 = ttk.Label(info_frame, text='n Zeilen')
        self.info_label_1.grid(column=0, row=0)
        self.info_label_2 = ttk.Label(info_frame, text='m Spalten')
        self.info_label_2.grid(column=0, row=1)
        latex_frame = ttk.Frame(main_frame)
        latex_frame.grid(column=1, row=3)
        latex_text = tk.Text(latex_frame)
        latex_text.grid(column=0, row=0)
        text_scrollbar = ttk.Scrollbar(latex_frame, orient=tk.VERTICAL, command=latex_text.yview)
        latex_text.configure(yscrollcommand=text_scrollbar.set)
        text_scrollbar.grid(column=1, row=0, sticky='ns')
        table_label = ttk.Label(main_frame, text="Tabellendaten")
        table_label.grid(column=0, row=2)
        table_frame = ttk.Frame(main_frame)
        table_frame.grid(column=0, row=3, sticky='ns')
        tree = ttk.Treeview(table_frame, show='headings', height=18)
        tree.grid(column=0, row=0)
        # add a scrollbar
        table_scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=table_scrollbar.set)
        table_scrollbar.grid(row=0, column=1, sticky='ns')
        self.generate_sample_data(tree)

    def generate_sample_data(self, tree):
        # define columns
        columns = ('first_name', 'last_name', 'email')
        tree.configure(columns=columns)
        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')
        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
            # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)

    def open_file(self):
        filetypes = (
            ('CSV-Datei', '*.csv'),
            ('Alle Dateien', '*.*')
        )
        self.filename = fd.askopenfilename(title='CSV-Datei öffnen', filetypes=filetypes)
        self.data = []
        max_columns = 0
        with open(self.filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=self.delimiter.get().strip())
            for row in csv_reader:
                if max_columns < len(row):
                    max_columns = len(row)
                self.data.append(row)
        self.info_label_1.configure(text=f"{len(self.data)} Zeilen")
        self.info_label_2.configure(text=f"{max_columns} Spalten")


if __name__ == '__main__':
    root = tk.Tk()
    gui = TabellengeneratorGui(root)
    root.mainloop()
