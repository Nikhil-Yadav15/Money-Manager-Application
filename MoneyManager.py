from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition, WipeTransition
from kivy.clock import Clock
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDFillRoundFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
##########################################################
import mysql.connector

mybd = mysql.connector.connect(host = "localhost", user = "root", passwd = "pass", database = "MoneyManage")

mycursor = mybd.cursor(buffered=True)
##########################################################

Window.size = (1536, 864)
kv = '''
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
<WindManager>:
    Screen:
        name: "Opening"
        MDFloatLayout:
            Image:
                id: opn_img
                source: "strtImgp.png"
                pos_hint: {"x": 0.2, "y": 0.37}
                size_hint: 0.6, 0.5
            ProgressBar:
                id: prg_bar
                color: 0.2,0.4,0.5,0.5
                max: 8
                min: 0
                value: root.prg_value
                pos_hint: {"x": 0, "top": 0}
                size_hint_y: 1
    Screen:
        name: "Sign Up"
        canvas.before:
            Color:
                rgba: 0/255, 15/255, 31/255, 1
            Rectangle:
                size: self.width, self.height

        MDCard:
            size_hint: 0.28, 1
            pos_hint: {"x": 0, "top": 1}
            md_bg_color: 0/255, 7/255, 15/255, 1
            padding: 20
            spacing: 30
            FloatLayout:
                Label:
                    text: "Hello Friend!"
                    color: 16/255, 140/255, 179/255, 1
                    font_size: 50
                    pos_hint: {"x": 0.01, "y": 0.1}
                Label:
                    text: "Let's get to know each other more"
                    font_size: 20
                    pos_hint: {"x": 0.01, "y": 0.01}

        MDCard:
            md_bg_color: 0/255, 7/255, 15/255, 1
            size_hint: 0.3, 0.65
            pos_hint: {"x": 0.5, "top": 0.8}
            padding: 20
            spacing: 30
        MDLabel:
            text: "Sign Up"
            font_size: 50
            size_hint: 0.2, 0.3
            pos_hint: {"x": 0.6, "y": 0.58}

        MDTextFieldRound:
            id: UPusername
            text: ""
            color_active: 255/255, 255/255, 255/255, 1
            normal_color: 215/255, 215/255, 215/255, 1
            icon_right_color: "black"
            hint_text_color: 0, 0, 0, 0.5
            hint_text: "Username"
            icon_right: "account"
            size_hint_x: None
            font_size: 20
            width: 200
            pos_hint: {"center_x": 0.65, "y": 0.57}

        MDTextFieldRound:
            id: UPpass
            hint_text: "Password"
            icon_right: "eye-off"
            icon_right_color: "black"
            hint_text_color: 0, 0, 0, 0.5
            color_active: 255/255, 255/255, 255/255, 1
            normal_color: 215/255, 215/255, 215/255, 1
            password: True
            size_hint_x: None
            font_size: 20
            width: 200
            pos_hint: {"center_x": 0.65, "y": 0.45}

        MDFillRoundFlatButton:
            text: "Join"
            md_bg_color: 0/255, 200/255, 186/255, 1
            text_color: 0/255, 7/255, 15/255, 1
            font_size: 17
            pos_hint: {"center_x": 0.65, "y": 0.35}
            on_press:
                root.SignUpCheck()
                
        MDTextButton:
            text: ""
            custom_color: 1, 1, 0, 1
            pos_hint: {"center_x": 0.71, "y": 0.457}
            on_press:
                root.changeIconUP()

        MDTextButton:
            text: "Already a user? Sign In"
            custom_color: 0, 1, 0, 1
            pos_hint: {"center_x": 0.65, "y": 0.28}
            on_press: 
                root.transition = SlideTransition()
                root.transition.direction = "right"
                root.current = "Sign In"
            
            
            
            
            
    Screen:
        name: "Sign In"
        canvas.before:
            Color:
                rgba: 0/255, 15/255, 31/255, 1
            Rectangle:
                size: self.width, self.height
        MDCard:
            md_bg_color: 0/255, 7/255, 15/255, 1
            size_hint: 0.6, 1
            pos_hint: {"x": 0.75, "y": 0}
            padding: 20
            spacing: 30
            
        Label:
            text: "Welcome Back!"
            color: 16/255, 140/255, 179/255, 1
            pos_hint: {"x": 0.38, "y": 0.15}
            font_size: 50
        Label:
            text: "We are glad you are back with us, your"
            pos_hint: {"x": 0.38, "y": 0.03}
            font_size: 20
        Label:
            text: " savings data is still safe with us."
            pos_hint: {"x": 0.38, "y": 0.001}
            font_size: 20
                
              
        MDCard:
            md_bg_color: 0/255, 7/255, 15/255, 1
            size_hint: 0.3, 0.65
            pos_hint: {"x": 0.2, "top": 0.8}
            padding: 20
            spacing: 30
    
        MDLabel:
            text: "Sign In"
            color: 1, 1, 1, 1
            font_size: 50
            size_hint: 0.2, 0.3
            pos_hint: {"x": 0.3, "y": 0.58}
        
        MDTextFieldRound:
            id: Inusername
            color_active: 255/255, 255/255, 255/255, 0.7
            normal_color: 225/255, 225/255, 225/255, 1
            hint_text: "Username"
            hint_text_color: 0, 0, 0, 0.5
            icon_right: "account"
            icon_right_color: "black"
            size_hint_x: None
            font_size: 20
            width: 200
            pos_hint: {"center_x": 0.35, "y": 0.57}
        
        MDTextFieldRound:
            id: Inpassword
            hint_text: "Password"
            hint_text_color: 0, 0, 0, 0.5
            icon_right: "eye-off"
            icon_right_color: "black" 
            color_active: 255/255, 255/255, 255/255, 1
            normal_color: 215/255, 215/255, 215/255, 1
            password: True
            size_hint_x: None
            font_size: 20
            width: 200
            pos_hint: {"center_x": 0.35, "y": 0.45}
            
        MDFillRoundFlatButton:
            text: "Validate"
            md_bg_color: 0/255, 200/255, 186/255, 1
            text_color: 0/255, 7/255, 15/255, 1
            font_size: 17
            pos_hint: {"center_x": 0.35, "y": 0.35}
            on_press: root.SignInCheck()
            
        MDTextButton:
            text: ""
            custom_color: 1, 1, 0, 1
            pos_hint: {"center_x": 0.41, "y": 0.456}
            on_press:
                root.changeIcon()
            
        MDTextButton:
            text: "Don't have an account? Create one"
            custom_color: 0, 1, 0, 1
            pos_hint: {"center_x": 0.35, "y": 0.28}
            on_press: 
                root.transition = SlideTransition()
                root.transition.direction = "left"
                root.current = "Sign Up"
                
        
                
        
                
    Screen:
        name: "Home Page"
        canvas.before:
            Color:
                rgba: 0/255, 15/255, 31/255, 1
            Rectangle:
                size: self.width, self.height
        MDNavigationLayout:
            ScreenManager:

                MDScreen:

                    BoxLayout:
                        orientation: "vertical"
                        MDToolbar:
                            md_bg_color: 0/255, 7/255, 15/255, 1
                            title: "Rural Finances"
                            specific_text_color: 1, 1, 1, 1
                            left_action_items: [["menu", lambda x: drawer.set_state("open")]]

                        FloatLayout:
                            MDCard:
                                md_bg_color: 1, 1, 1, 1
                                size_hint: 0.305, 0.22
                                pos_hint: {"x": 0.337, "top": 0.91}
                                padding: 20
                                spacing: 30
                            MDCard:
                                
                                md_bg_color: 0/255, 7/255, 15/255, 1
                                size_hint: 0.3, 0.2
                                pos_hint: {"x": 0.34, "top": 0.9}
                                padding: 20
                                spacing: 30
                                Label:
                                    
                                    text: "Currently You have:"
                                    font_size: 20
                                    pos_hint: {"x": 0.34, "top": 1.2}
                                Label:
                                    id: modifyAmount
                                    font_size: 20
                                    pos_hint: {"center_x": 0.2, "top": 1.2}
                            Label:
                                text: "Money in the Beginning:"
                                font_color: "white"
                                size_hint: 0.2, 0.3
                                font_size: 20
                                pos_hint: {"x": 0.329, "top": 0.9}
                            Label:
                                id: amountID
                                font_color: "white"
                                size_hint: 0.2, 0.3
                                font_size: 20
                                pos_hint: {"x": 0.465, "top": 0.9}
                            MDCard:
                                md_bg_color: 1, 1, 1, 1
                                size_hint: 0.405, 0.36
                                pos_hint: {"x": 0.297, "top": 0.41}
                                padding: 20
                                spacing: 30
                            MDCard:
                                md_bg_color: 0/255, 7/255, 15/255, 1
                                size_hint: 0.4, 0.34
                                pos_hint: {"x": 0.3, "top": 0.4}
                                padding: 20
                                spacing: 30
                                FloatLayout:
                                    Label:
                                        text: "Learn To Save Money"
                                        font_size: 20
                                        size_hint: 0.3, 0.4
                                        pos_hint: {"x": 0.34, "y": 0.8}
                                    Label:
                                        font_size: 18
                                        text: "I. Make a monthly budget of the money you will receive as well as your "
                                        size_hint: 0.3, 0.4
                                        pos_hint: {"x": 0.34, "top": 0.9}
                                    Label:
                                        font_size: 18
                                        text: "expenses. Spend not more than 30% of your income in purchasing"
                                        size_hint: 0.35, 0.4
                                        pos_hint: {"x": 0.3, "top": 0.78}
                                    Label:
                                        font_size: 18
                                        text: "desirable but not necessary things."
                                        size_hint: 0.35, 0.4
                                        pos_hint: {"x": 0.3, "top": 0.66}
                                    Label:
                                        font_size: 18
                                        text: "II. Investing: To earn more money from your saved money, invest it.       "
                                        size_hint: 0.3, 0.4
                                        pos_hint: {"x": 0.34, "top": 0.52}
                                    Label:
                                        font_size: 18
                                        text: " Investments can be of several types: crypto, stock market, SIPs, etc."
                                        size_hint: 0.35, 0.4
                                        pos_hint: {"x": 0.32, "top": 0.4}
                                    Label:
                                        font_size: 18
                                        text: "To learn more Log onto: www.moneyManage24.com"
                                        size_hint: 0.35, 0.4
                                        pos_hint: {"x": 0.3, "top": 0.28}


                            MDFillRoundFlatIconButton:
                                text: "  Add  "
                                font_size: 20
                                md_bg_color: 0/255, 7/255, 15/255, 1
                                line_color: 110/255, 217/255, 56/255, 1
                                line_width: 2
                                icon: "decagram"
                                icon_color: 110/255, 217/255, 56/255, 1
                                pos_hint: {"x": 0.1, "top": 0.3}
                                on_press: root.add()

                            MDFillRoundFlatIconButton:
                                text: "Subtract"
                                line_color: 255/255, 0/255, 48/255, 1
                                line_width: 2
                                md_bg_color: 0/255, 7/255, 15/255, 1
                                icon_color: 255/255, 0/255, 48/255, 1
                                icon: "decagram-outline"
                                font_size: 20
                                pos_hint: {"x": 0.8, "top": 0.3}
                                on_press: root.subtract()
            MDNavigationDrawer:
                id: drawer
                md_bg_color: 0, 13/255, 33/255, 1
                BoxLayout:
                    orientation: "vertical"
                    padding: "8dp"
                    spacing: "8dp"
                    Image:
                        source: "profile.png"

                    ScrollView:
                        BoxLayout:
                            orientation: "vertical"
                            spacing: "12dp"
                            MDRectangleFlatIconButton:
                                text: "Account"
                                icon: "account"
                                icon_color: 1, 1, 1, 1
                                line_width: 1.5
                                size_hint_x: 1
                                on_press: root.account()

                            MDRectangleFlatIconButton:
                                icon: "help-box"
                                text: "Help"
                                size_hint_x: 1
                                icon_color: 1, 1, 0, 1
                                line_width: 1.5
                                on_press: 
                                    root.help()
                                    drawer.set_state("close")
                            MDRectangleFlatIconButton:
                                text: "About Us"
                                icon: "notebook-edit"
                                icon_color: 102/255, 1, 51/255, 1
                                line_width: 1.5
                                size_hint_x: 1
                                on_press: root.aboutUs()
                            MDRectangleFlatIconButton:
                                text: "Log Out"
                                icon: "exit-run"
                                icon_color: 1, 0, 0, 1
                                line_width: 1.5
                                size_hint_x: 1
                                on_press: root.signOut()
                            Widget:      

'''

class WindManager(ScreenManager):
    prg_value = NumericProperty()

    def SignInCheck(self):
        mycursor.execute("SELECT username, password FROM userInfo")
        for i, z in mycursor:
            if i == self.ids.Inusername.text.lower() and z == str(self.ids.Inpassword.text.lower()):
                global user
                user = i
                self.current = "Home Page"
                self.transition = WipeTransition()
                self.displayAmount()
                self.ids.Inusername.text = ""
                self.ids.Inpassword.text = ""
                self.ids.drawer.set_state("close")
                break
        else:
            self.informIn()

    def SignUpCheck(self):
        self.inputBool = 1
        mycursor.execute("SELECT username FROM userInfo")
        for u in mycursor:
            if self.ids.UPusername.text.lower() == str(u)[2: -3]:

                self.inputBool = 0
                self.informUP()
            elif str(self.ids.UPusername.text).strip() == "":
                self.inputBool = 0
                self.informIn()

        if self.inputBool:

            sql = "INSERT INTO userInfo (username, password) VALUES( %s, %s)"
            val = (str(self.ids.UPusername.text.lower()), str(self.ids.UPpass.text.lower()))
            mycursor.execute(sql, val)
            mybd.commit()

            global user
            user = self.ids.UPusername.text
            self.ids.Inusername.text = ""
            self.ids.Inpassword.text = ""
            self.AmountPo()


    def displayAmount(self):
        global user
        sql1 = "SELECT amount, modifiedAmount FROM userInfo WHERE username = %s"
        mycursor.execute("SELECT amount, modifiedAmount FROM userInfo WHERE username = %s", (str(user),))
        for i, z in mycursor:
            self.ids.amountID.text = "₹" + str(i)
            self.ids.modifyAmount.text = "₹" + str(z)

    def informUP(self):
        self.dialog = MDDialog(title = "Sorry!", text = "Entered username has been choosed", buttons = [MDRaisedButton(text = "Ok", on_press = lambda dt: self.dialog.dismiss())])
        self.dialog.open()
    def informIn(self):
        self.dialogin = MDDialog(title="Sorry!", text="Invalid username or password", buttons=[MDRaisedButton(text="Ok", on_press=lambda dt: self.dialogin.dismiss())])
        self.dialogin.open()
    def AmountPo(self):
        self.po = Popup()
        self.po.title = "Amount"
        self.po.size_hint = 0.4, 0.4
        self.po.title_align = "center"
        self.po.auto_dismiss = False
        self.po.title_size = 20
        self.po.open()
        self.po.background_color = (45 / 255, 68 / 255, 71 / 255, 1)
        self.po.separator_color = (68 / 255, 173 / 255, 1, 1)

        self.flt = FloatLayout()
        self.flt.input = MDTextField(hint_text="Enter amount",
                                     required = True,
                                     helper_text="Only Input Absolute Number not greater than 10Lakh",
                                     max_text_length = 7,
                                     helper_text_mode="on_focus",
                                     font_size=20,
                                     size_hint=(0.6, 0.6),
                                     on_text_validate = lambda dt: self.enteringMoney(),
                                     pos_hint={"x": 0.2, "y": 0.6})
        self.flt.add_widget(self.flt.input)
        self.flt.button = MDFillRoundFlatButton(text="Confirm",
                                                size_hint=(0.12, 0.14),
                                                font_size=17,
                                                text_color=(0 / 255, 7 / 255, 15 / 255, 1),
                                                md_bg_color=(0 / 255, 200 / 255, 186 / 255, 1),
                                                padding=10,
                                                elevation=20,
                                                pos_hint={"x": 0.4, "y": 0.3},
                                                on_press=lambda dt: self.enteringMoney())

        self.flt.add_widget(self.flt.button)
        self.po.content = self.flt

    def enteringMoney(self):
        if self.flt.input.text is None or self.flt.input.text == "":
            pass
        else:
            global user

            sql = "UPDATE userInfo SET amount = %s, modifiedAmount = %s WHERE username = %s"
            val = (self.flt.input.text, self.flt.input.text, str(user))
            mycursor.execute(sql, val)
            mybd.commit()
            self.displayAmount()
            self.po.dismiss()
            self.current = "Home Page"

    def add(self):
        self.Addpo = Popup()
        self.Addpo.title = "Addition of Money"
        self.Addpo.size_hint = 0.4, 0.4
        self.Addpo.title_align = "center"
        self.Addpo.title_size = 20
        self.Addpo.open()
        self.Addpo.background_color = (45/255, 68/255, 71/255, 1)
        self.Addpo.separator_color = (68/255, 173/255, 1, 1)

        self.AddFlt = FloatLayout()
        self.AddFlt.input = MDTextField(hint_text="Enter here",
                                        required=True,
                                        helper_text = "Only Input Absolute Number not greater than 10Lakh",
                                        helper_text_mode = "on_focus",
                                        max_text_length=7,
                                        font_size=20,
                                        size_hint=(0.6, 0.6),
                                        pos_hint={"x": 0.2, "y": 0.6})
        self.AddFlt.add_widget(self.AddFlt.input)
        self.AddFlt.button = MDFillRoundFlatButton(text="Confirm",
                                            size_hint=(0.12, 0.14),
                                            font_size=17,
                                            text_color = (0 / 255, 7 / 255, 15 / 255, 1),
                                            md_bg_color = (0/255, 200/255, 186/255, 1),
                                            padding=10,
                                            elevation=20,
                                            pos_hint={"x": 0.4, "y": 0.3},
                                            on_press=lambda dt: self.adding())

        self.AddFlt.add_widget(self.AddFlt.button)
        self.Addpo.content = self.AddFlt

    def subtract(self):
        self.Subpo = Popup()
        self.Subpo.title = "Subtraction of Money"
        self.Subpo.size_hint = 0.4, 0.4
        self.Subpo.title_align = "center"
        self.Subpo.title_size = 20
        self.Subpo.open()
        self.Subpo.background_color = (45 / 255, 68 / 255, 71 / 255, 1)
        self.Subpo.separator_color = (68 / 255, 173 / 255, 1, 1)

        self.SubFlt = FloatLayout()
        self.SubFlt.input = MDTextField(hint_text="Enter here",
                                        required = True,
                                        helper_text = "Only Input Absolute Number not greater than 10Lakh",
                                        helper_text_mode = "on_focus",
                                        max_text_length=7,
                                        font_size=20,
                                        size_hint=(0.6, 0.6),
                                        pos_hint={"x": 0.2, "y": 0.6})
        self.SubFlt.add_widget(self.SubFlt.input)
        self.SubFlt.button = MDFillRoundFlatButton(text="Confirm",
                                                   size_hint=(0.12, 0.14),
                                                   font_size=17,
                                                   text_color=(0 / 255, 7 / 255, 15 / 255, 1),
                                                   md_bg_color=(0 / 255, 200 / 255, 186 / 255, 1),
                                                   padding=10,
                                                   elevation=20,
                                                   pos_hint={"x": 0.4, "y": 0.3},
                                                   on_press=lambda dt: self.subtracting())

        self.SubFlt.add_widget(self.SubFlt.button)
        self.Subpo.content = self.SubFlt

    def adding(self):
        if self.AddFlt.input.text is None or self.AddFlt.input.text == "":
            self.AddFlt.input.helper_text = "Do not leave it blank"
            self.AddFlt.input.helper_text_mode = "persistent"
        else:
            global user
            mycursor.execute("SELECT modifiedAmount FROM userInfo WHERE username = %s", (user, ))
            for i in mycursor:
                self.varI = str(i)[1: -2]
            updateamount = int(self.varI) + int(self.AddFlt.input.text)
            mycursor.execute("UPDATE userInfo SET modifiedAmount = %s WHERE username = %s", (str(updateamount), user))
            mybd.commit()
            self.Addpo.dismiss()
            self.ids.modifyAmount.text = "₹" + str(updateamount)

    def subtracting(self):
        if self.SubFlt.input.text is None or self.SubFlt.input.text == "":
            self.SubFlt.input.helper_text = "Do not leave it blank"
            self.SubFlt.input.helper_text_mode = "persistent"
        else:
            global user
            mycursor.execute("SELECT modifiedAmount FROM userInfo WHERE username = %s", (user,))
            for i in mycursor:
                self.varI = str(i)[1: -2]
            updateamount = int(self.varI) - int(self.SubFlt.input.text)
            mycursor.execute("UPDATE userInfo SET modifiedAmount = %s WHERE username = %s", (str(updateamount), user))
            mybd.commit()
            self.Subpo.dismiss()
            self.ids.modifyAmount.text = "₹" + str(updateamount)

    def account(self):
        global user
        mycursor.execute("SELECT password FROM userInfo WHERE username = %s", (user,))
        for i in mycursor:
            self.accountPass = str(i)[1: -2]
        self.showAccount()
    def showAccount(self):
        global user
        self.dialogAcc = MDDialog(title="Your Detail", text = f"Username: {user}\n\nPassword: {str(self.accountPass)[1:-1]}",
                                 buttons=[MDRaisedButton(text="Ok", on_press=lambda dt: self.dialogAcc.dismiss())])
        self.dialogAcc.open()
    def signOut(self):
        self.dialogOut = MDDialog(title="You are about to Log Out",
                                  buttons=[MDFlatButton(text="CANCEL", on_press=lambda dt: self.dialogOut.dismiss()), MDRaisedButton(text="Ok", on_press=lambda dt: self.out())])
        self.dialogOut.open()
        global user
        user = ""
    def out(self):
        self.current = "Sign In"
        self.dialogOut.dismiss()
    def changeIcon(self):
        if self.ids.Inpassword.icon_right == "eye-off":
            self.ids.Inpassword.icon_right = "eye"
        else:
            self.ids.Inpassword.icon_right = "eye-off"
        if self.ids.Inpassword.password == True:
            self.ids.Inpassword.password = False
        else:
            self.ids.Inpassword.password = True
    def changeIconUP(self):
        if self.ids.UPpass.icon_right == "eye-off":
            self.ids.UPpass.icon_right = "eye"
        else:
            self.ids.UPpass.icon_right = "eye-off"
        if self.ids.UPpass.password == True:
            self.ids.UPpass.password = False
        else:
            self.ids.UPpass.password = True

    def help(self):
        self.HPpo = Popup()
        self.HPpo.title = "Help"
        self.HPpo.size_hint = 0.8, 0.6
        self.HPpo.title_align = "center"
        self.HPpo.auto_dismiss = False
        self.HPpo.title_size = 20
        self.HPpo.open()
        self.HPpo.background_color = (102/255, 125/255, 130/255, 1)
        self.HPpo.separator_color = (68 / 255, 173 / 255, 1, 1)

        self.HPFlt = FloatLayout()
        self.HPFlt.input = Label(text="Rular Finances is an app to help teenage rural people to manage their savings in a systematic manner",
                                font_size=25,
                                size_hint=(0.6, 0.6),
                                pos_hint={"x": 0.19, "y": 0.5})
        self.HPFlt.add_widget(self.HPFlt.input)
        self.HPFlt.input1 = Label(text="I. To see the amount you have: Go to Home In the middle of the screen, you would find the amount you have announced to have. ",
                                 font_size=20,
                                 size_hint=(0.6, 0.6),
                                 pos_hint={"x": 0.2, "y": 0.4})
        self.HPFlt.add_widget(self.HPFlt.input1)
        self.HPFlt.input2 = Label(text = "II. To add your savings: Go to Home, Click on the button Add Money,  and add the amount of money you possess.",
                                  font_size=20,
                                  size_hint=(0.6, 0.6),
                                  pos_hint={"x": 0.139, "y": 0.3})
        self.HPFlt.add_widget(self.HPFlt.input2)
        self.HPFlt.input3 = Label(text = "III. To subtract your savings: Go to Home, Click on the button Subtract Money,  and subtract the amount of money you spend.",
                                  font_size=20,
                                  size_hint=(0.6, 0.6),
                                  pos_hint={"x": 0.183, "y": 0.2})
        self.HPFlt.add_widget(self.HPFlt.input3)
        self.HPFlt.button = MDFillRoundFlatButton(text="OK",
                                                  size_hint=(0.1, 0.1),
                                                  font_size=17,
                                                  md_bg_color=(0 / 255, 200 / 255, 186 / 255, 1),
                                                  text_color=(0 / 255, 7 / 255, 15 / 255, 1),
                                                  pos_hint={"x": 0.4, "y": 0.3},
                                                  on_press=lambda dt: self.HPpo.dismiss())

        self.HPFlt.add_widget(self.HPFlt.button)
        self.HPpo.content = self.HPFlt

    def aboutUs(self):
        self.USpo = Popup()
        self.USpo.title = "About Us"
        self.USpo.size_hint = 0.5, 0.4
        self.USpo.title_align = "center"
        self.USpo.auto_dismiss = False
        self.USpo.title_size = 20
        self.USpo.open()
        self.USpo.background_color = (102/255, 125/255, 130/255, 1)
        self.USpo.separator_color = (68 / 255, 173 / 255, 1, 1)

        self.USFlt = FloatLayout()
        self.USFlt.input = Label(text="We are two students of class 11th who aim to simplify the process of saving pocket",
                                font_size=18,
                                size_hint=(0.6, 0.6),
                                pos_hint={"center_x": 0.5, "y": 0.5})
        self.USFlt.add_widget(self.USFlt.input)
        self.USFlt.input0 = Label(text = " money for rural people. We are passionate about this app and how it can help others",
                                font_size=18,
                                size_hint=(0.6, 0.6),
                                pos_hint={"center_x": 0.5, "y": 0.35})
        self.USFlt.add_widget(self.USFlt.input0)
        self.USFlt.input1 = Label(text="get most out of their money. ",
                                font_size=18,
                                size_hint=(0.6, 0.6),
                                pos_hint={"center_x": 0.21, "y": 0.2})

        self.USFlt.add_widget(self.USFlt.input1)
        self.USFlt.button = MDFillRoundFlatButton(text="OK",
                                                  size_hint=(0.1, 0.17),
                                                  font_size=17,
                                                  md_bg_color=(0 / 255, 200 / 255, 186 / 255, 1),
                                                  text_color=(0 / 255, 7 / 255, 15 / 255, 1),
                                                  pos_hint={"x": 0.4, "y": 0.27},
                                                  on_press=lambda dt: self.USpo.dismiss())

        self.USFlt.add_widget(self.USFlt.button)
        self.USpo.content = self.USFlt




Builder.load_string(kv)


class Manage(MDApp):
    def build(self):
        self.title = "Money Manager"
        self.icon = "manage_logo.ico"
        self.theme_cls.theme_style = "Dark"
        Clock.schedule_once(lambda dt: self.update_opn_pg(), 2)
        Clock.schedule_once(lambda dt: self.inc_val(), 2)
        Clock.schedule_once(lambda dt: self.move_screen(), 6.5)
        Clock.schedule_once(lambda dt: self.max_scr(), 0)
        return WindManager()

    def update_opn_pg(self):
        self.root.ids.prg_bar.pos_hint = {"x": 0, "top": 0.7}

    def inc_val(self):
        Clock.schedule_interval(lambda dt: self.update_prg_value(), 1)

    def update_prg_value(self):
        self.root.prg_value += 2

    def max_scr(self):
        MDApp.get_running_app().root_window.maximize()

    def move_screen(self):
        self.root.transition = WipeTransition()
        self.root.transition.duration = 1
        self.root.current = "Sign In"

if __name__ == "__main__":
    Manage().run()
