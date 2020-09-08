from PyDictionary import *
from tkinter import *
import tkinter.messagebox
import win32com.client
import pyttsx3





class dictionary:
     def __init__(self,root):
          self.root=root
          self.root.title("Dictionary")
          self.root.geometry("500x510")
          self.root.resizable(0,0)
          self.root.iconbitmap("dicname.ico")






#=====================================================
          def on_enter1(e):
            but_tran['background']="black"
            but_tran['foreground']="cyan"
  
          def on_leave1(e):
            but_tran['background']="SystemButtonFace"
            but_tran['foreground']="SystemButtonText"


          def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
          def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



          def on_enter3(e):
            but_speak['background']="black"
            but_speak['foreground']="cyan"
  
          def on_leave3(e):
            but_speak['background']="SystemButtonFace"
            but_speak['foreground']="SystemButtonText"

          def clear():
                texttopaste1.delete('1.0',END)
                texttopaste.delete('1.0',END)


          def speak():
               try:
                   
                    
                    speaker=win32com.client.Dispatch("SAPI.spVoice")
                    sentences=texttopaste1.get("1.0","end")
                    if sentences==" ":
                         tkinter.messagebox.askretrycancel("info","please enter some thing to find meaning")

                    else:
                         
##                         converter=pyttsx3.init()
##                         converter.setProperty('rate',110)
##                         converter.setProperty('volume',0.8)
##                         voices=converter.getProperty('voices')
##                         converter.setProperty("voice",voices[0].id)
##                         converter.say(sentences)
##                         converter.runAndWait()
                         speaker.Speak(sentences)

               except:
                    tkinter.messagebox.askretrycancel("info","internal error")
               
               
               
               




            
            
          def findmeaning():
               try:
                    
                     texttopaste1.delete('1.0',END)
                     texts=texttopaste.get("1.0","end")
                     #dics=PyDictionary(str(texts))
                     #meanings=dics.printMeanings()
                     #change=str(meanings)
                     #texttopaste1.insert("end",change)
                     #print(meanings)
                     
                     disc=PyDictionary()
                     meaning=disc.meaning(texts)

                     
                     try:
                          
                          texttopaste1.insert("end",*meaning['Adjective'])
                          #texttopaste1.insert("end",*meaning['Noun'])
                          #texttopaste1.insert("end",*meaning['Verb'])
                          #texttopaste1.insert("end",*meaning['AdVerb'])
                          
                     except:
                         pass

                     
                     try:
                         
                          texttopaste1.insert("end",*meaning['Noun'])
                     except:
                         pass

                    
                     try:
                          
                          texttopaste1.insert("end",*meaning['Verb'])
                     except:
                        pass

                     
                     try:
                         
                          texttopaste1.insert("end",*meaning['AdVerb'])
                     except:
                         pass
               
                         
               except:
                    tkinter.messagebox.askretrycancel("info","Something went wrong or network error")


#==============================Frames========================
          MainFrame1=Frame(self.root,width=500,height=510,relief="sunken",bd=4)
          MainFrame1.place(x=0,y=0)

          FristFrame=Frame(MainFrame1,width=495,height=300,relief="raised",bd=4,bg="green")
          FristFrame.place(x=0,y=0)

          SecondFrame=Frame(MainFrame1,width=495,height=195,relief="raised",bd=4)
          SecondFrame.place(x=0,y=300)


#=========================FristFrame==================================
          Labframe=LabelFrame(FristFrame,height=290,width=485,bd=3,text="DICTIONARY")
          Labframe.place(x=1,y=0)

          Scol=Scrollbar(Labframe,orient="vertical")
          Scol.grid(column=10,sticky="NS")
        
          texttopaste=Text(Labframe,height=10,width=57,font=('times new roman',12,'bold'),yscrollcommand=Scol.set)
          texttopaste.grid(row=0,column=0)
          Scol.config(command=texttopaste.yview)


          but_tran=Button(FristFrame,text="meaning",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=findmeaning)
          but_tran.place(x=20,y=230)
          but_tran.bind("<Enter>",on_enter1)
          but_tran.bind("<Leave>",on_leave1)


          but_speak=Button(FristFrame,text="Speak",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=speak)
          but_speak.place(x=170,y=230)
          but_speak.bind("<Enter>",on_enter3)
          but_speak.bind("<Leave>",on_leave3)



          but_clear=Button(FristFrame,text="clear",width=13,font=('times new roman',11,'bold'),height=0,cursor="hand2",command=clear)
          but_clear.place(x=340,y=230)
          but_clear.bind("<Enter>",on_enter2)
          but_clear.bind("<Leave>",on_leave2)


#=========================SecondFrame=========================================

          Scol1=Scrollbar(SecondFrame,orient="vertical")
          Scol1.grid(column=10,sticky="NS")
        
          texttopaste1=Text(SecondFrame,height=10,width=58,font=('times new roman',12,'bold'),yscrollcommand=Scol1.set)
          texttopaste1.grid(row=0,column=1)
          Scol1.config(command=texttopaste1.yview)
            

          



if __name__=="__main__":
     root=Tk()
     app=dictionary(root)
     root.mainloop()
