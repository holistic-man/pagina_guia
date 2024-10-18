import reflex as rx
from Guia_landing.codigo_pagina import create_page

def index() -> rx.Component:
    return rx.box(
        create_page(),
        #commet
    )


app = rx.App()
app.add_page(index)
#cambios