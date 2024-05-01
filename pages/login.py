from flet import *
from utils.extras import *

class LoginPage(Container):
  def __init__(self,switch_page):

#def the page values
    super().__init__()
    self.expand = True
    self.offset = transform.Offset(0,0,)
    self.content = Container(
      height=base_height,
      width=base_width,
      bgcolor='white',
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      expand=True,
      content=Stack(
        controls=[
          Container(
            expand=True,
            content=Column(
              expand=True,
              spacing=0,
              controls=[
                Container(
                  height=70,
                  border=border.only(bottom=border.BorderSide(1, 'black')),
                  padding=padding.all(12),
                  bgcolor='white',
                  content=Row(
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
                          #     icon=icons.NOTIFICATIONS,
                          #     icon_color=colors.BLACK,
                          #     icon_size=25,
                          #   )
                          # ),
                            ]
                          )
                        ]
                      )
                    ]
                  )
                ),
                
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
                      value='Join the UpChainX',
                      size=26,
                      color='black',
                      font_family='montserrat semibold'
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
                          value='Sign Up With Google',
                          size=14,
                          color='white',
                          font_family='montserrat medium',
                        )
                      ),
                      Container(
                        alignment=alignment.center,
                        width=250,
                        border=border.all(1, colors.BLACK),
                        height=45,
                        border_radius=30,
                        content=Text(
                          value='Sign Up With Discord',
                          size=14,
                          color='black',
                          font_family='montserrat medium',
                        )
                      ),
                          ]
                        )
                      ),
                        ]
                      )
                    )
                    ]
                  )
                ),
              ]
            )
          )
        ]
      )
    )