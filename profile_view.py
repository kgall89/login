import flet as ft
import views.colors as c
from views.Router import Router, DataStrategyEnum
from State import global_state


def profileView(router):

    content = ft.Column(
        [
            ft.Container(
                bgcolor=c.white,
                padding=10,
                content=(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                  ft.Text("Athletic Training Room Check-In",
                                          size=50, color=c.blue, font_family="circular"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            ft.Row(
                                [
                                    ft.Image(src=f"/CagedLogo.png", width=600, border_radius=10, color=c.blue)
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ]
                    )
                )
            ),
            ft.Container(
                bgcolor=c.white,
                padding=10,
                content=(
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.CupertinoButton(
                                        bgcolor=c.gray,
                                        on_click=lambda _: page.go('/'),
                                        content=ft.Column(
                                            [
                                                ft.Icon(name=ft.icons.FACT_CHECK_OUTLINED, color=c.blue, size=250),
                                                ft.Text("   Check-In",
                                                        color=c.blue, font_family="circular", size=35)
                                            ],
                                        ),
                                    ),
                                    ft.CupertinoButton(
                                        bgcolor=c.gray,
                                        content=ft.Column(
                                            [
                                                ft.Icon(name=ft.icons.FACT_CHECK_OUTLINED, color=c.blue, size=250),
                                                ft.Text("   Check-In",
                                                        color=c.blue, font_family="circular", size=35)
                                            ],
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                        ]
                    )
                )
            )
        ]
    )

    return content
