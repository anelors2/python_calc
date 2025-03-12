import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"

    page.window.width = 350
    page.window.height = 470
    page.window.resizable = False
    page.bgcolor = "#2d2d2d"

    result_text = ft.Text(value="", color="#ffffff", size=28, text_align="right")

    all_values=""

    def EnterValues(e):
        nonlocal all_values
        all_values+= str(e.control.text)
        result_text.value = all_values
        page.update()
    
    def Clear(e):
        nonlocal all_values
        all_values = ""
        result_text.value = ""
        page.update()
    
    def Calculate(e):
        nonlocal all_values
        try:
            result = eval(all_values)
            result_text.value = str(result)
        except:
            result_text.value = ""
        page.update()
    
    def Backspace(e):
        nonlocal all_values
        all_values = all_values[:-1]
        result_text.value = all_values
        page.update()
    

    display = ft.Container(               
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        content=result_text,
        alignment=ft.alignment.center_right,
    )
    
    #Style buttons
    style_number = {
        "height": 60,
        "expand": 1,
        "bgcolor": "#37474F",
        "color": "#ffffff",
    }

    style_operator = {
        "height": 60,
        "expand": 1,
        "color": "#ffffff",
        "bgcolor": "#FFA000"
    }

    style_equal = {
        "height": 60,
        "expand": 1,
        "color": "#ffffff",
        "bgcolor": "#42d442"
    }

    style_clear = {
        "height": 60,
        "expand": 1,
        "color": "#ffffff",
        "bgcolor": "#F44336"
    }

    buttons_grid = [
        [
        ("C", style_clear, Clear),
        ("%", style_operator, EnterValues),
        ("/", style_operator, EnterValues),
        ("*", style_operator, EnterValues)
        ],
        [
            ("7", style_number, EnterValues),
            ("8", style_number, EnterValues),
            ("9", style_number, EnterValues),
            ("-", style_operator, EnterValues)
        ],
        [
            ("4", style_number, EnterValues),
            ("5", style_number, EnterValues),
            ("6", style_number, EnterValues),
            ("+", style_operator, EnterValues)
        ],
        [
            ("1", style_number, EnterValues),
            ("2", style_number, EnterValues),
            ("3", style_number, EnterValues),
            ("=", style_equal, Calculate)
        ],
        [
            ("0", {**style_number, "expand":2}, EnterValues),
            (".", style_operator, EnterValues),
            ("⌫", style_clear, Backspace)
        ]
           ]
    
    buttons = []
    for row in buttons_grid:
        row_control = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), padding=0),
                
            )
            row_control.append(btn)
        buttons.append(ft.Row(controls=row_control, spacing=5))

    page.add(
        ft.Column(
            [
                display,
                ft.Column(controls=buttons, spacing=5)
                
            ]
        )
    )
    

ft.app(target=main)