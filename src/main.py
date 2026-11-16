import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    page.window.width = 320
    page.window.height = 480

    display = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, read_only=True)

    def on_click(e):
        key = e.control.content
        if key == "C":
            display.value = "0"
        elif key == "=":
            try:
                display.value = str(eval(display.value))
            except Exception:
                display.value = "Error"
        else:
            display.value = key if display.value in ("0", "Error") else display.value + key
        page.update()

    keys = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    page.add(
        display,
        *[
            ft.Row([ft.Button(content=k, on_click=on_click, expand=True ) for k in row])
            for row in keys
        ],
    )


ft.run(main)