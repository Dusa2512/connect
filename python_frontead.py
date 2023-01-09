import PySimpleGUI as sg
import pandas as pd
import os


df=pd.read_excel("C:\Python\Data\Phân tích Data\demo1.xlsx")
print(df)

rw=df.columns.values.tolist()
cl=df.values.tolist()
print(rw)
print(cl)
sg.theme("DarkTeal9")
directory = os.getcwd()
layout=[
        [sg.Text("Auto arrange file",background_color="Green",text_color="Yellow",justification="Left")],
        [sg.Text("Tên File",size=(7,1)),sg.Input(key="Tên File",size=(61,4)),sg.Text("Bộ",size=(3,1)),
        sg.Combo(["Tư vấn trước","Báo cáo KTKT","Hồ sơ MT","KQ LCNT"],key="Bộ",size=(58,5))],
        [sg.Text("Ngày lưu",size=(7,1)),sg.Input(key="Ngày lưu",size=(61,4)),sg.Text("Mã",size=(3,1)),
        sg.Input(key="Mã",size=(58,5))],
        [sg.Text("Agree",size=(7,1)),sg.Radio("Yes","g",True,key="g1"),sg.Radio("No","g",key="g2")],
        [sg.Button('Save',key='Save'),sg.Button('exit',key='exit'),sg.FileBrowse(initial_folder=directory,file_types=
                                                                                 [("file",".xlsx"),("file",".csv"),("file",".docx")]),sg.InputText(key="bro",size=(30,2))],
         [sg.Table(values=cl
            ,headings=rw
            ,key="table",row_height=30,justification="Center",expand_x=True,expand_y=True)]
    
   
    
        ]
window=sg.Window("Automation arrange",layout)


while True:
        event ,values = window.read()
        values["Agree"] = "OK" if values["g1"] else "error"
        del values["g1"]
        del values["g2"]
        del values["table"]
        
        if event == sg.WINDOW_CLOSED or event=='exit' :
                break
        if event == 'Save' :
                df = df.append(values,ignore_index= True )
                df.to_excel("C:\Python\Data\Phân tích Data\demo1.xlsx",index= False)
                df = pd.read_excel("C:\Python\Data\Phân tích Data\demo1.xlsx")
                val = df.values.tolist()
                window["table"].update(values = val)

