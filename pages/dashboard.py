from flet import *
from utils.extras import *

class DashboardPage(Container):
  def __init__(self,switch_page):
    super().__init__()
    self.offset = transform.Offset(0,0,)
    self.expand = True
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
                  padding=padding.all(12),
                  border=border.only(bottom=border.BorderSide(1, 'black')),
                  bgcolor='white',
                  content=Row(
                    controls=[
                      Row(
                        alignment=alignment.center,
                        spacing=10,
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
                          Container( #notification icon container
                            content=IconButton(
                              icon=icons.NOTIFICATIONS,
                              icon_color=colors.BLACK,
                              icon_size=25,
                            )
                          ),
                            ]
                          )
                        ]
                      )
                    ]
                  )
                ),
                Container(
                  height=60,
                  padding=10,
                  bgcolor='black',
                  content=Row(
                    controls=[
                      Row(
                        alignment=alignment.center,
                        spacing=70,
                        controls=[
                      Container(
                  alignment=alignment.center,
                      content=CircleAvatar(
                        content=Text("S",
                                     size=25,
                                     font_family='montserrat semibold'),
                        color=colors.BLACK,
                        bgcolor=colors.PURPLE_200,
                      )
                      ),
                    Container( #text container starts here
                      content=Column( 
                        spacing=2,#text column starts here
                        controls=[
                          Container(
                      content=Text(
                      value='Account 1',
                      color='white',
                      font_family='montserrat light'
                            )
                          ),
                          Container(
                      content=Text(
                      value='0x02da....q12sd',
                      size=12,
                      color='white',
                      font_family='montserrat light'
                            )
                          )
                        ]
                      ), #text column ends here
                    ), #
                          Container(
                            content=IconButton(
                              icon=icons.MORE_VERT_ROUNDED,
                              icon_color='white',
                              icon_size=20
                            )
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
                    controls=[
                      Container(
                        padding=30,
                        content=Column( #text column starts here
                        controls=[
                          Container(
                      alignment=alignment.center,
                      content=Text(
                      value='0.1499 BTC',
                      size=28,
                      color='black',
                      font_family='montserrat semibold'
                            )
                          ),
                        ]
                        )
                      ),
                      
                Container(
                  height=100,
                  bgcolor='black',
                  content=Row(
                    controls=[
                      Row(
                        alignment=alignment.center,
                        spacing=70,
                        controls=[
                        #transfer controls
                        ]
                      )
                    ]
                  )
                ),
                Container(
                  bgcolor='black',
                  content=Column(
                    controls=[
                      Tabs(
                        tab_alignment=TabAlignment.FILL,
                        scrollable=False,
                        selected_index=1,
                        animation_duration=300,
                        label_color=colors.BLACK,
                        unselected_label_color=colors.BLACK,
                        indicator_color=colors.LIME_ACCENT_700,
                        indicator_thickness=4,
                        indicator_tab_size=True,
                        is_secondary=False,
                        tabs=[
            Tab(
                text="Assets",
                content=Container(
                  content=Text("This is Asset tabs",
                               font_family='montserrat medium',
                               color=colors.BLACK),
                ),
            ),
            Tab(
                text="NFT",
                content=Container(
                  content=Text("This is NFT tabs",
                               font_family='montserrat medium',
                               color=colors.BLACK),
                ),
            )
            ]
                      )
                    ]
                  )
                )
                    ]
                    )
                    ),
                    
                Container(
                  height=60,
                  padding=10,
                  bgcolor='black',
                  content=Row(
                    controls=[
                      Row(
                        alignment=alignment.center,
                        spacing=70,
                        controls=[
                          Container(
                            content=CircleAvatar(
                              bgcolor=colors.BLUE_900,
                            )
                          ),
                      Column(
                        spacing=2,
                        alignment=alignment.center,
                        controls=[
                          Container(
                            content=Text(
                              value='Account 1',
                              font_family='montserrat light',
                              text_align=alignment.center,
                            )
                          ), ##
                          Container(
                            content=Text(
                              value='0x02da....q12sd',
                              font_family='montserrat light',
                              size=12,
                            )
                          ), ##
                        ]
                      ), #
                          Container(
                            content=IconButton(
                              icon=icons.MORE_VERT,
                              icon_color='white'
                            )
                          )
                        ]
                      )
                    ]
                  )
                  
                ),
              ]
            ),
            )
        ]
        )
        
      )