import PySimpleGUI as sg


lbl1 = sg.Text(text= 'Select Files To Compress')
btn1 = sg.FileBrowse(button_text='Choose')
lbl2 = sg.Text(text= 'Select Destination Folder')
btn2 = sg.FileBrowse(button_text='Choose')
txt1 = sg.InputText(tooltip='files to compress')
txt2 = sg.InputText(tooltip='destination folder')
btn3 = sg.Button(button_text='Compress')
window =  sg.Window(title= 'To Do', layout=[
                                            [lbl1,txt1,btn1],
                                            [lbl2,txt2,btn2],
                                            [btn3]])
window.read()
window.close()