# gui/main_frame.py
# @dev this is the main grafical user interface 

import wx
import wx.grid as gridlib
from src.db_connection import get_db_connection
import csv

class main_window(wx.Frame):
    def __init__(self, *args, **kw):
        super(main_window, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.grid = gridlib.Grid(self.panel)

        self.load_tables()
        self.create_layout()
        
    # @dev loading the tables 
    def load_tables(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        self.tables = [table[0] for table in cursor.fetchall()]
        cursor.close()
        connection.close()

    def create_layout(self):
        self.grid.CreateGrid(len(self.tables), 2)
        self.grid.SetColLabelValue(0, "Export")
        self.grid.SetColLabelValue(1, "Table Name")

        for index, table in enumerate(self.tables):
            self.grid.SetCellValue(index, 1, table)
            self.grid.SetCellEditor(index, 0, gridlib.GridCellBoolEditor())
            self.grid.SetCellRenderer(index, 0, gridlib.GridCellBoolRenderer())

        save_button = wx.Button(self.panel, label="Save", size=(100, 30))
        save_button.Bind(wx.EVT_BUTTON, self.on_save)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(save_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.panel.SetSizerAndFit(sizer)
        self.SetTitle("MySQL DB App")
        self.Show()

    # @dev saving
    def on_save(self, event):
        selected_tables = [self.grid.GetCellValue(i, 1) for i in range(len(self.tables)) if self.grid.GetCellValue(i, 0) == '1']
        
        # @dev the database connection 
        connection = get_db_connection()
        cursor = connection.cursor()

        for table in selected_tables:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()

            #@dev converting tables to csv file
            with open(f"{table}.csv", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([i[0] for i in cursor.description])  
                writer.writerows(rows)  

        cursor.close()
        connection.close()
        wx.MessageBox("Export succesfull!", "Success", wx.OK | wx.ICON_INFORMATION)
