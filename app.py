from flet import *
import pickle
from utils.extras import *
from pages.mainpage import MainPage
from pages.login import LoginPage
from pages.signup import SignupPage
from pages.dashboard import DashboardPage
# from service.auth import get_user,authenticate, verify_token, register_user, is_valid_email
import asyncio

class WindowDrag(UserControl):
#   def __init__(self):
#     # super().__init__()
#     # self.color = color
  def build(self):
    return Container(content=WindowDragArea(height=10,content=Container(bgcolor='#f2f2f2')))


class App(UserControl):
  def __init__(self,pg:Page):
    # super().__init__()

    pg.window_title_bar_hidden = True
    pg.window_frameless = True
    pg.window_title_bar_buttons_hidden = True
    pg.bgcolor = colors.TRANSPARENT
    pg.window_bgcolor = colors.TRANSPARENT
    pg.fonts = {
    "Montserrat ThinItalic":"fonts/Montserrat/Montserrat-ThinItalic.ttf",
    "Montserrat Thin":"fonts/Montserrat/Montserrat-Thin.ttf",
    "Montserrat Semibold":"fonts/Montserrat/Montserrat-Semibold.ttf",
    "Montserrat SemiboldItalic":"fonts/Montserrat/Montserrat-SemiboldItalic.ttf",
    "Montserrat Regular":"fonts/Montserrat/Montserrat-Regular.ttf",
    "Montserrat MediumItalic":"fonts/Montserrat/Montserrat-MediumItalic.ttf",
    "Montserrat Medium":"fonts/Montserrat/Montserrat-Medium.ttf",
    "Montserrat LightItalic":"fonts/Montserrat/Montserrat-LightItalic.ttf",
    "Montserrat Light":"fonts/Montserrat/Montserrat-Light.ttf",
    "Montserrat Italic":"fonts/Montserrat/Montserrat-Italic.ttf",
    "Montserrat ExtraLightItalic":"fonts/Montserrat/Montserrat-ExtraLightItalic.ttf",
    "Montserrat ExtraLight":"fonts/Montserrat/Montserrat-ExtraLight.ttf",
    "Montserrat ExtraBold":"fonts/Montserrat/Montserrat-ExtraBold.ttf",
    "Montserrat ExtraBoldItalic":"fonts/Montserrat/Montserrat-ExtraBoldItalic.ttf",
    "Montserrat BoldItalic":"fonts/Montserrat/Montserrat-BoldItalic.ttf",
    "Montserrat Bold":"fonts/Montserrat/Montserrat-Bold.ttf",
    "Montserrat BlackItalic":"fonts/Montserrat/Montserrat-BlackItalic.ttf",
    "Montserrat Black":"fonts/Montserrat/Montserrat-Black.ttf",
  }
    pg.window_width = base_width
    pg.window_height = base_height



    # auth = asyncio.run(verify_token(asyncio.run(load_token())))
    self.pg  = pg
    self.pg.spacing = 0
    self.delay = 0.1
    self.anim = animation.Animation(300,AnimationCurve.EASE_IN_OUT_CUBIC)
    self.main_page = DashboardPage(self.switch_page)
    self.screen_views = Stack(
      
      
        expand=True,
        controls=[
          self.main_page
        ]
      )

    self.init_helper()

  def switch_page(self,e):
    if e.control.data == 'register':
      name = self.signup_page.name_box.value
      password = self.signup_page.password_box.value
      email = self.main_page.email_input.content.value
   
      user = register_user(name, email, password)
      self.screen_views.controls.clear()
      self.screen_views.controls.append(DashboardPage(self.switch_page,email,))
      self.screen_views.update()
      return


    elif e.control.data == 'process_login':
      email = self.main_page.email_input.content.value
      if is_valid_email(email):
        user = get_user(email)
        if user:
          id = user[0]
          self._name = user[1]
          self._email = user[2]
          self.screen_views.controls.clear()
          self.login_page = LoginPage(self.switch_page,name=self._name,email=self._email,dp='')
          # self.login_page.content.on_focus = self.hide_error
          self.screen_views.controls.append(self.login_page)
          self.screen_views.update()
        else:
          self.screen_views.controls.clear()  
          self.signup_page = SignupPage(self.switch_page,email)
          self.screen_views.controls.append(self.signup_page)
          self.screen_views.update()
      else:
        self.main_page.email_input.bgcolor = input_error_bg
        self.main_page.email_input.border = border.all(width=2,color=input_error_outline)
        
        self.main_page.main_content.controls.insert(1,self.main_page.error)

        self.main_page.update()
        # self.main_page.email_input.update()
        
      
    elif e.control.data == 'main_page':
      self.screen_views.controls.clear()
      self.screen_views.controls.append(self.main_page)
      self.screen_views.update()
      
    elif e.control.data == 'login_clicked':
      password = self.login_page.pwd_input.content.value
      email = self.login_page.email

      auth = authenticate(email,password)
      if auth:
        asyncio.run(save_token(auth))
        self.screen_views.controls.clear()
        self.screen_views.controls.append(DashboardPage(self.switch_page,email))
        self.screen_views.update()

      else:
        self.login_page.login_box.controls.insert(4,self.login_page.error)  
        self.login_page.pwd_input.bgcolor = input_error_bg
        self.login_page.pwd_input.border=border.all(width=2, color=input_error_outline)
        self.login_page.pwd_input.update()
        self.login_page.login_box.update()

    elif e.control.data == 'logout':
      try:
        os.remove('token.pkl')  
      except:
        pass
      self.screen_views.controls.clear()
      self.screen_views.controls.append(self.main_page)
      self.screen_views.update()

    


      

  def init_helper(self):
    self.pg.add(
      WindowDrag(),
      self.screen_views 
    )


app(target=App, assets_dir='assets')