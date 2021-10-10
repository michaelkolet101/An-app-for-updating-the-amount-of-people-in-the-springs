from kivy.core.text import LabelBase
from re import MULTILINE
from kivy.app import App
from kivy.core import text
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

m = " "
dic_of_ucvas ={
    "lipta":"8",
    "umfi":"12",
    "soko":"4",
    "livne":"5",
    "lavan":"20",
    "tut":"6"
    }

class EUCALIPTUS(App):
    
    
    
    def callback(self, instens):
        try:
          m = self.user.text
          self.greeting.text = " אנשים במעיין"[::-1] + dic_of_ucvas[m]  + "  ישנם "[::-1]
        except:
          self.greeting.text = "enter again"
    
    def updat(self, instens):
        self.user.text = " "
        dic_of_ucvas[m] = self.user.text
        self.button1.text="Please confirm the update"


    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.window.size_hint = (0.6, 0.9)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        


        #add widgets to window
        self.img = Image(source = "DSC09931.jpg", size_hint = (2, 3) )
        self.window.add_widget(self.img)
        
        self.greeting = Label(
                            text = "הכנס שם מעיין"[::-1],
                            font_size = 30,
                            font_name = "arial 1.ttf",
                            color = "#00FFCE"
                            )
        self.window.add_widget(self.greeting)
       
        self.user = TextInput(
                            text = " "[::-1],
                            multiline = False,
                            padding_y =(5,5),
                            size_hint = (1, 0.4),
                            font_name = "arial 1.ttf"
                            )
        self.window.add_widget(self.user)
        
        self.button = Button(text = "אישור"[::-1], size_hint = (0.5, 0.3), bold =True, background_color = "#00FFCE",font_name = "arial 1.ttf")
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        self.button1 = Button(text = "עדכן את כמות האנשים"[::-1], size_hint = (0.5, 0.3), bold =True, background_color = "yellow",font_name = "arial 1.ttf")
        self.button1.bind(on_press = self.callback)
        self.window.add_widget(self.button1)
        

        return self.window

    
        
        

if __name__ == "__main__":
    EUCALIPTUS().run()
