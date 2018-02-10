from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfFileMerger
import os

class App:
    def __init__(self,parent,file_list=None):
        frame=Frame(parent)#create a frame on root window
        if not file_list:
            self.file_list=[] #if no list exist create a list
        else:
            file_list=self.file_list
        parent.geometry('500x500')#size of the window
        parent.title('PDF Manager')
        parent.iconbitmap('icon.ico')
        frame.pack() #makes frame visible
        self.open_button=Button(frame,text="OPEN FILES",command=self.open_file)
        self.open_button.pack()
        self.listbox_area=Listbox(frame,width=50)
        self.listbox_area.pack()
        self.remove_button=Button(frame,text="Remove File",command=self.remove_file)
        self.remove_button.pack()
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
                self.listbox_area.insert('end',i)
        print(self.file_list)
    
    def remove_file(self):
        selected_file = self.listbox_area.curselection()
        self.listbox_area.delete(selected_file)
        del self.file_list[selected_file[0]]
        print(self.file_list)
        print(selected_file[0])
        
    #merge all selected pdf files
    def merge_pdf(self):
        merger=PdfFileMerger()
        for file in self.file_list:
            merger.append(file)
        desktop_file = os.path.expanduser("~/Desktop/merged.pdf")
        merger.write(desktop_file)
        merger.close()
        self.listbox_area.delete(0,END) #remove all filenames from listbox after merging
        del self.file_list[:] #delete the list 

#call the main function        
if __name__=="__main__":
    root=Tk()
    app=App(root)
    root.mainloop()
