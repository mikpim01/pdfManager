from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfFileMerger
import os

class App:
    def __init__(self,parent,file_list=None):
        frame=Frame(parent)
        if not file_list:
            self.file_list=[]
        else:
            file_list=self.file_list
        parent.geometry('500x500')
        parent.title('PDF Manager')
        parent.iconbitmap('icon.ico')
        frame.pack()
        self.open_button=Button(frame,text="OPEN FILES",command=self.open_file)
        self.open_button.pack()
        self.merger_button=Button(frame,text="Merge Files",command=self.merge_pdf)
        self.merger_button.pack()
        
    #function to browse files
    def open_file(self):
        name = askopenfilenames(filetypes = (("Portable Document Files", "*.pdf"),))
        path_name=""
        for i in name:
            path_name=str(i).replace("/","//")
            if path_name not in self.file_list:
                self.file_list.append(path_name)
                self.labels=Label(text=i)
                self.labels.pack()
        print(self.file_list)
    #merge all selected pdf files
    def merge_pdf(self):
        merger=PdfFileMerger()
        for file in self.file_list:
            merger.append(file)
        desktop_file = os.path.expanduser("~/Desktop/merged.pdf")
        merger.write(desktop_file)
        merger.close()
#call the main function        
if __name__=="__main__":
    root=Tk()
    app=App(root)
    root.mainloop()
