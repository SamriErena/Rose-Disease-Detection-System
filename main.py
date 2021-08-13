from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3

# 133, 248, 224
# Window.size = (1440, 2960)
LoginPage = '''
ScreenManager:
    LoginScreen:
    HomeScreen:
    SignupScreen:
    DiagnoseScreen:
    ResultScreen:
    ScanScreen:
        
        
# login screen begins here       
<LoginScreen>:
    name: "login"
    Image: 
        source: 'background_login.jpg'
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False
    BoxLayout:
        orientation:'vertical'
        padding : '25dp'
        spacing: '-2dp'
        MDLabel:
            text: ' '            
            font_size : '45dp'
            
        MDTextField:
            id : username
            hint_text: 'username or id'
            line_color_normal: app.theme_cls.accent_color
            font_size : '25dp'
            helper_text: "This field  is required"
            helper_text_mode: "on_focus"
            bold : 'True'
            #mode: "fill"
            #mode: "rectangle"
        MDTextField:
            id : password
            hint_text: 'password'
            line_color_normal: app.theme_cls.accent_color
            helper_text: "This field  is required"
            helper_text_mode: "on_focus"
            font_size : '25dp'
            password : 'True'
        MDTextButton:
            text:'forgot your password?'
            pos_hint : {"center_x":.7}
            padding: [10,30]
            bold : 'True'
            theme_text_color: "Custom"
            text_color : 1,1,1,1
        MDRoundFlatButton : 
            text : 'login' 
            width : 22
            font_size : 17
            pos_hint : {"center_x":.5}
            on_press: root.manager.current="home"
            padding: [10,40]
            
        MDTextButton:
            text : "Don't have an account? sign up"
            pos_hint : {"center_x":.6}
            on_press: root.manager.current="signup"
            theme_text_color: "Custom"
            text_color : 1,1,1,1
            padding: [30,10]
            bold : 'True'
        ScrollView: 

#login page ends here
#signup page starts here    
<SignupScreen>:
    name: "signup"
    #firstName_signup : firstName_signup
    #lastName_signup : lastName_signup
    #userName_signup : userName_signup
    #password_signup : password_signup
    #idNumber_signup : idNumber_signup
    #gender_signup : gender_signup
    #assignedGHN_signup : assignedGHN_signup
    orientation: 'vertical'
    Image: 
        source: 'background_signup.jpg'
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False
    
    BoxLayout:
        orientation: 'vertical'
        padding : '25dp'
        MDLabel:
            text : 'Sign up'
            font_style : 'Button'
            font_size : 40
            bold : True
            halign : 'left' 
            theme_text_color: "Custom"
            text_color : 0,1,0,1 
                 
        MDTextField : 
            hint_text : "First name"
            id : firstName_signup
            max_text_length: 10
            line_color_normal: app.theme_cls.accent_color
            
        MDTextField : 
            hint_text : "Last Name"
            max_text_length: 10
            id : lastName_signup
            line_color_normal: app.theme_cls.accent_color
        MDTextField : 
            hint_text : "User Name"
            max_text_length: 10
            id : userName_signup
            line_color_normal: app.theme_cls.accent_color
        MDTextField : 
            hint_text : "Password"
            max_text_length: 10
            id : Password_signup
            icon_right : 'eye-off'
            password : True
            line_color_normal: app.theme_cls.accent_color
        MDTextField : 
            hint_text : "ID number"
            id : idNumber_signup
            max_text_length: 10 
            line_color_normal: app.theme_cls.accent_color    
        BoxLayout:  
            orientation: 'horizontal'
            MDLabel:
                text: 'Job status'
                theme_text_color: "Custom"
                text_color : 1,1,1,1
            MDDropDownItem : 
                id : drop_item_job
                text : 'Scouter'          
        MDLabel:
            text: '  '
        BoxLayout:  
            orientation: 'horizontal'
            MDLabel:
                text: 'Gender'
                theme_text_color: "Custom"
                text_color : 1,1,1,1
                id: gender_signup                
            MDDropDownItem : 
                id : drop_item_gender
                text : 'Female' 
        MDTextField : 
            hint_text : "Assigned Greenhouse Number"
            max_text_length: 10
            id : assigned_signup
            line_color_normal: app.theme_cls.accent_color                  
        MDRoundFlatButton : 
            text : 'sign up' 
            width : 22
            font_size : 15
            pos_hint : {"center_x":.75}
            on_press : root.signup()
        MDLabel:
            text: 'already have an account? log in'
            halign: 'right'
            theme_text_color: "Custom"
            text_color : 1,1,1,1
            #on_press: root.manager.current="login"

#signup page ends here   

     
#the homepage starts here            
            
<MySwiper@MDSwiperItem>
    
<HomeScreen>:
    name: "home"
    Image: 
        source: 'background.jpg'
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False
    
        
    MDNavigationLayout:
        ScreenManager:
            Screen:                
                BoxLayout:
                    orientation: 'vertical'                    
                    MDToolbar:
                        title: "search here"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [['magnify', lambda x: x]]
                    
                    BoxLayout:
                        padding: '13dp'
                        
                        MDTextField:
                            id: toolbar
                            hint_text:'    View rose pictures here'
                            font_size : '20dp'
                            pos_hint : {"center_x":.5}
                            line_color_normal: app.theme_cls.accent_color
                            readonly: True 
                        
            
                    MDSwiper:
                        size_hint_y: None
                        height: root.height - toolbar.height - dp(400)
                        y: root.height - self.height - toolbar.height - dp(20)
                
                        MySwiper:
                            FitImage:
                                source: "images/1.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/2.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/3.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/4.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/5.jpg"
                                radius: [10,]
                    
                    
                    BoxLayout:
                        padding: '13dp'
                        MDTextField:
                            id: toolbar
                            hint_text:'    View Disease library here'
                            font_size : '20dp'
                            pos_hint : {"center_x":.5}
                            line_color_normal: app.theme_cls.accent_color
                            readonly: True    
                    MDSwiper:
                        size_hint_y: None
                        height: root.height - toolbar.height - dp(400)
                        y: root.height - self.height - toolbar.height - dp(20)
                
                        MySwiper:
                            FitImage:
                                source: "images/infected/1.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/infected/2.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/infected/3.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/infected/4.jpg"
                                radius: [10,]
                
                        MySwiper:
                            FitImage:
                                source: "images/infected/5.jpg"
                                radius: [10,]
                    ScrollView:
                    

                    MDBottomNavigation: 
                        id: bottom_nav                       
                        panel_color: 1,1,1,1  
                        MDFloatingActionButtonSpeedDial:
                            data :  app.data              
                        MDBottomNavigationItem:                            
                            text: "Home"
                            icon: 'home'
                        MDBottomNavigationItem:                            
                            text: "Diagnose"
                            icon: 'medical-bag'
                        MDBottomNavigationItem:
                            text: "History"
                            icon: 'history'
                        MDBottomNavigationItem: 
                            text: ""
                            icon: 'blank'
                        
 #on_release: root.manager.current="diagnose"                   
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'mine.png'
                MDLabel:
                    text: '  Samrawit Erena'
                    size_hint_y: None
                    height : self.texture_size[1]
                    font_style: 'Subtitle1'
                MDLabel:
                    text: '  Samri.erena12@gmail.com'
                    font_style: 'Caption'
                    size_hint_y: None
                    height : self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "About Us"
                            IconLeftWidget:
                                icon: "help-circle" 
                        OneLineIconListItem:
                            text: "Exit"
                            IconLeftWidget:
                                icon: "logout"         
                         
                                
                                
#Home page ends here


# Diagnose page starts here

<DiagnoseScreen>:
    name: "diagnose"
    Image: 
        source: 'background.jpg'
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False
    
    BoxLayout : 
        padding : '1dp'
        orientation : 'vertical'
        
        MDLabel:
            text: "please select the symptoms"
            halign:'center'
            font_size : '21dp'
            theme_text_color: "Custom"
            text_color : 0,1,0,1
        BoxLayout:
            
            MDCheckbox:
                size_hint: None, None
                size: "48dp", "48dp"
                pos_hint: {'center_x': .5, 'center_y': .5}
                theme_text_color: "Custom"
                text_color : 1,1,1,1
            MDLabel: 
                text : "looks like a fine, soft powder sprinkled on the plant"
                theme_text_color : "Custom"
                text_color : (1,1,1,1)
        BoxLayout:
            
            MDCheckbox:
                size_hint: None, None
                size: "48dp", "48dp"
                pos_hint: {'center_x': .5, 'center_y': .5}
                theme_text_color: "Custom"
                text_color : 1,1,1,1
            MDLabel: 
                text : 'bright red new growth that never turn green'
                theme_text_color : "Custom"
                text_color : (1,1,1,1)
        BoxLayout:
            MDCheckbox:
                size_hint: None, None
                size: "48dp", "48dp"
                pos_hint: {'center_x': .5, 'center_y': .5}
                theme_text_color: "Custom"
                text_color : 1,1,1,1
            MDLabel: 
                text : 'flower buds emerge in tiny, tight clusters'
                theme_text_color : "Custom"
                text_color : (1,1,1,1)
        BoxLayout:
            MDCheckbox:
                size_hint: None, None
                size: "48dp", "48dp"
                pos_hint: {'center_x': .5, 'center_y': .5}
                theme_text_color: "Custom"
                text_color : 1,1,1,1
            MDLabel: 
                text : 'rapidly expanding black spots surrounded by a yellow area on rose leaves'
                theme_text_color : "Custom"
                text_color : (1,1,1,1)
        ScrollView: 
    MDRoundFlatButton : 
        text : 'Search'
        pos_hint : {"center_x":.5, "center_y":.1}
        width : 220
        font_size : 15
        theme_text_color: "Custom"
        text_color : 0,1,0,1

#Diagnose page ends here  

#result screen starts here
<ResultScreen>:
    name: "result"
    
    
#result screen ends here

#scan screen begins here
<ScanScreen>:
    name: "scan"
    BoxLayout:
        padding: '5dp'
        orientation: 'vertical'
        
        BoxLayout:
            Image:
                source: 'background.jpg'    
           
        MDRoundFlatButton:
            text: 'Scan'
            pos_hint : {"center_x":.5}
            width : 65
            font_size : 20
    ScrollView:
    
#scan screen ends here
'''


class HomeScreen(Screen):
    pass


class LoginScreen(Screen):
    pass


class ResultScreen(Screen):
    pass


class SignupScreen(Screen):

    pass
# firstname = objectProperty(None)


class DiagnoseScreen(Screen):
    pass


class ScanScreen(Screen):
    pass


sm = ScreenManager()

sm.add_widget(LoginScreen(name="login"))
sm.add_widget(HomeScreen(name="home"))
sm.add_widget(SignupScreen(name="signup"))
sm.add_widget(DiagnoseScreen(name="diagnose"))
sm.add_widget(ResultScreen(name="result"))
sm.add_widget(ScanScreen(name="scan"))


# the sqlite part is written in here

# class scouter():
#
#   def add_firstname(self, firstname):
#      self.firstname = firstname
#
#   def add_lastname(self, lastname):
#      self.lastname = lastname
#
#   def add_username(self, username):
#      self.username = username
#
#   def add_password(self, password):
#      self.password = password
#
#  def add_idnumber(self, idnumber):
#       self.idnumber = idnumber
#
#   def add_gender(self, gender):
#      self.gender = gender
#
# def add_assignedGHN(self, assignedGHN):
#       self.assignedGHN = assignedGHN
#
# the sqlite part ends here


# The main class starts here
class RoseDiseaseDetectionApp(MDApp):
    data = {
        "Camera": "camera",
        "Gallery": "image-album"

    }

    def build(self):
        return Builder.load_string(LoginPage)
        # self.theme_cls.primary_palette = "Green"
        # self.theme_cls.accent_palette = "Green"
        # conn = sqlite3.connect('scouter_data.db')
        # c = conn.cursor()
        # c.execute(""" CREATE TABLE if not exists scouter_data(
        #                    first_name text,
        #                   last_name text,
        #                  username text,
        #                 password text,
        #                idNumber text,
        #               gender text,
        #              assignedGHN integer
        # )
        #        """)
        # conn.commit()
        # conn.close()


    #def signup(self):

    # conn = sqlite3.connect('scouter_data.db')
    # c = conn.cursor()
    # firstname = self.root.ids.firstName_signup.text
    # lastname = self.root.ids.lastName_signup.text
    # username = self.root.ids.userName_signup.text
    # password = self.root.ids.password_signup.text
    # idnumber = self.root.ids.idNumber_signup.text
    # gender = self.root.ids.gender_signup.text
    # assignedGHN = self.root.ids.assignedGHN_signup.text

    # if not firstname:
    #   return toast('firstName not valid')
    # elif not username:
    #   return toast('username is not valid')
    # elif not lastname:
    #   return toast('lastname is not valid')
    # elif not password:
    #   return toast('password is not valid')
    # elif not idnumber:
    #   return toast('id number is not valid')
    # elif not gender:
    #   return toast('gender is not valid')
    # elif not assignedGHN:
    #   return toast('assigned GHN is not valid')

    # c.execute(
    #    "INSERT INTO scouter_data VALUES (:firstname, :lastname, :username, :password, :idNumber, :gender, :assignedGHN)",
    #    {
    #        'first': self.root.ids.firstName_signup.text,
    #        'lastname': self.root.ids.lastName_signup.text,
    #        'username': self.root.ids.userName_signup.text,
    #        'password': self.root.ids.password_signup.text,
    #        'idNumber': self.root.ids.idNumber_signup.text,
    #        'gender': self.root.ids.gender_signup.text,
    #        'assignedGHN': self.root.ids.assignedGHN_signup.text,
    #
    #           })
    #      print('signup successful')
    #     conn.commit()
    #    conn.close()

   # def login_user(self):


# conn = sqlite3.connect('scouter_data.db')
#   c = conn.cursor()
#  c.execute("SELECT username,password FROM customers")
# users = c.fetchall()
# username = self.root.ids.username.text
# password = self.root.ids.password.text
# word = ''
# i = 0
# Loop thru records
# for user in users:
#   if

#    word = f'{word}\n{user[0][i]}'
#    self.root.ids.word_label.text = f'{word}'
# conn.commit()
# conn.close()


# the main class ends here
RoseDiseaseDetectionApp().run()
