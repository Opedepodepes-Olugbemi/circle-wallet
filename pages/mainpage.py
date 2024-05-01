from flet import *
from utils.extras import *

#main class
class MainPage(Container):
  def __init__(self,switch_page):

#def the page values
    super().__init__()
    self.expand = True
    self.offset = transform.Offset(0,0,)
    self.content = Container(
      height=base_height,
      width=base_width,
      bgcolor=base_color,
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      expand=True,
      content=Stack(
        controls=[
          Container(
            expand=True,
            content=Column(
              expand=True,
              spacing=0,
              controls=[ #custom app bar made using container
                Container(
                  height=70,
                  border=border.only(bottom=border.BorderSide(1, 'black')),
                  padding=padding.all(12),
                  bgcolor='white',
                  content=Row( #app bar has a row direction
                    controls=[
                      Row(
                        alignment=alignment.center,
                        spacing=50,
                        controls=[
                          Container(
                            content=Image( #app icon container
                              src=f"assets/images/upchainx2.png",
                              scale=1,
                            )
                          ),
                          Row( #row for dropdown option and notification button
                            controls=[
                            Container(
                            content=Dropdown(
                                options=[
                                dropdown.Option("Ethereum Mainnet"),
                                dropdown.Option("ETH Sepolia"),
                                dropdown.Option("Avalanche"),
                            ],
                            dense=True,
                            border_color='black',
                            focused_border_color='black',
                            border_radius=30,
                            border_width=1,
                            width=200,
                            item_height=50,
                            autofocus=False,
                            icon_enabled_color='black',
                            value='ETH Sepolia',
                            fill_color="white",
                            filled=True,
                            color='black',

                          ),
                          ),
                          # Container( #notification icon container
                          #   content=IconButton(
                          #     icon=icons.NOTIFICATIONS_ROUNDED,
                          #     icon_color=colors.BLACK,
                          #     icon_adaptive=True,
                          #   )
                          # ),
                            ]
                          )
                        ]
                      )
                    ]
                  )
                ), #app image container
                Container(
                  alignment=alignment.center,
                  expand=True,
                  bgcolor='white',
                  content=Column(
                    controls=[ #mainpage control
                    Container(
                  alignment=alignment.center,
                  padding=45,
                      content=Image( # image source
                        src=f"assets/images/playstore.png",
                        height=140,
                        width=140,
                      ),
                    ),
                    Container( #text container starts here
                      content=Column( #text column starts here
                        controls=[
                          Container(
                      alignment=alignment.center,
                      content=Text(
                      value='Open UpChainX',
                      size=30,
                      color='black',
                      font_family='montserrat bold'
                            )
                          ),
                          Container(
                      alignment=alignment.center,
                      content=Text(
                      value='Your programmable wallet',
                      size=15,
                      color='black',
                      font_family='montserrat medium'
                            )
                          )
                        ]
                      ), #text column ends here
                    ),
                    Container( #container for pin and button
                      content=Column(
                        controls=[
                      Container(
                        alignment=alignment.center,
                        content=TextField(
                        label="PIN",
                        border=InputBorder.UNDERLINE,
                        hint_text="Enter text here",
                        width=250,
                        keyboard_type=KeyboardType.PHONE,
                        color="black",
                        input_filter=InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
                        password=True,
                        can_reveal_password=True,
                      )
                      ),
                      Container(
                        alignment=alignment.center,
                        margin=10,
                        content=Column(
                          controls=[
                          Container(
                        alignment=alignment.center,
                        width=250,
                        bgcolor=base_black,
                        height=45,
                        border_radius=30,
                        content=Text(
                          value='Unlock',
                          size=15,
                          color='white',
                          font_family='montserrat medium',
                        )
                      ),
                          ]
                        )
                      ),
                      Container(
                        alignment=alignment.center,
                        content=Text(
                          value='Forgot PIN?',
                          size=12,
                          color='blue',
                          style=TextStyle(
                            decoration=TextDecoration.UNDERLINE,
                            decoration_color='blue'),
                          font_family='montserrat medium',
                          
                        )
                      )
                        ]
                      )
                    )
                    ]
                  )
                )
              ]
            )

          )
        ]
      )
    )