from tkinter.filedialog import askopenfilename
from autocorrect import Speller
#Now to make things smooth, lets define a class to do all the work 
class FileWorker:
    def __init__(self):
        #first get in the needed files using askopenfilename 
        self.file_to_work = askopenfilename()
        
        #the file to work is a string which we can work with
        #Now lets configure the autocorrect model 
        
        self.gizmo = Speller().autocorrect_sentence
    def getcontent(self):
        """
            Now let's get the content of the file, for this project i will deal with txt files 
            only, as a task an improvement, make yours versatile to handle pdfs and docx
        """
        with open(self.file_to_work,'r') as f:
            self.file = f.read()
    def correctAndWrite(self):
        #Now to correct the contents
        self.corrected = self.gizmo(self.file)
        
        #now write content to new file
        with open(f'corrected-file.txt','w') as g:
            g.write(self.corrected)
    def rollOver(self):
        self.getcontent()
        self.correctAndWrite()
while True:
    FileWorker().rollOver()
        
        
        
