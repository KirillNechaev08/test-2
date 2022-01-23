from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView



v1=""
v2=""
v3=""
v4=""
v5=""


class netotvet(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt= Label(text="НЕ ПРАВИЛЬНО ТЫ НЕ УМЁН В ЭТОЙ ТЕМЕ!!!!!!!")
        line1=BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line1.add_widget(txt)
        self.add_widget(line1)


class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', text='', **kwargs):
        super().__init__(text=text, **kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt = Label(text = "Гипер тест")
        name1 = Label(text = 'Введите имя:')
        name2= TextInput(text = "", multiline = False)
        btn = ScrButton(self, direction ='left', goal ='first', text ='Начать тест')
        line1= BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line1.add_widget(txt)
        line1.add_widget(name1)
        line1.add_widget(name2)
        line1.add_widget(btn)
        self.add_widget(line1)

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt= Label(text="вопрос номер 1")
        txt2 = Label(text="сам вопрос")
        btn1=ScrButton(self, direction ='left', goal ='net', text ='да')
        btn2=ScrButton(self, direction ='left', goal ='second', text ='нет')
        line1= BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line2 = BoxLayout(orientation="horizontal", padding = 8, spacing = 8)
        line1.add_widget(txt)
        line1.add_widget(txt2)
        line1.add_widget(line2)
        line2.add_widget(btn1)
        line2.add_widget(btn2)
        self.add_widget(line1)

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt= Label(text="вопрос номер 2")
        txt2 = Label(text="сам вопрос")
        btn1=ScrButton(self, direction ='left', goal ='net', text ='да')
        btn2=ScrButton(self, direction ='left', goal ='third', text ='нет')
        line1= BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line2 = BoxLayout(orientation="horizontal", padding = 8, spacing = 8)
        line1.add_widget(txt)
        line1.add_widget(txt2)
        line1.add_widget(line2)
        line2.add_widget(btn1)
        line2.add_widget(btn2)
        self.add_widget(line1)


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt= Label(text="вопрос номер 3")
        txt2 = Label(text="сам вопрос")
        btn1=ScrButton(self, direction ='left', goal ='net', text ='да')
        btn2=ScrButton(self, direction ='left', goal ='fourth', text ='нет')
        line1= BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line2 = BoxLayout(orientation="horizontal", padding = 8, spacing = 8)
        line1.add_widget(txt)
        line1.add_widget(txt2)
        line1.add_widget(line2)
        line2.add_widget(btn1)
        line2.add_widget(btn2)
        self.add_widget(line1)



class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt= Label(text="вопрос номер 4")
        txt2 = Label(text="сам вопрос")
        btn1=ScrButton(self, direction ='left', goal ='net', text ='да')
        btn2=ScrButton(self, direction ='left', goal ='fifth', text ='нет')
        line1= BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line2 = BoxLayout(orientation="horizontal", padding = 8, spacing = 8)
        line1.add_widget(txt)
        line1.add_widget(txt2)
        line1.add_widget(line2)
        line2.add_widget(btn1)
        line2.add_widget(btn2)
        self.add_widget(line1)



class FifthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt= Label(text="вопрос номер 5")
        txt2 = Label(text="сам вопрос")
        btn1=ScrButton(self, direction ='left', goal ='net', text ='да')
        btn2=ScrButton(self, direction ='left', goal ='end', text ='нет')
        line1= BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line2 = BoxLayout(orientation="horizontal", padding = 8, spacing = 8)
        line1.add_widget(txt)
        line1.add_widget(txt2)
        line1.add_widget(line2)
        line2.add_widget(btn1)
        line2.add_widget(btn2)
        self.add_widget(line1)

class EndScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        txt=Label(text="Молодец, ты прошёл тест!!!")
        line1 = BoxLayout(orientation="vertical", padding = 8, spacing = 8)
        line1.add_widget(txt)
        self.add_widget(line1)















class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name="main"))
        sm.add_widget(FirstScr(name="first"))
        sm.add_widget(SecondScr(name="second"))
        sm.add_widget(ThirdScr(name="third"))
        sm.add_widget(FourthScr(name="fourth"))
        sm.add_widget(FifthScr(name="fifth"))
        sm.add_widget(netotvet(name="net"))
        sm.add_widget(EndScr(name="end"))
        return sm





app = MyApp()
app.run()