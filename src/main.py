import flet as ft


def main(page: ft.Page):
    page.title = "Calculator"
    result=ft.Text(value="0",color=ft.Colors.WHITE, size=20)
    page.add(
        ft.Container(
            expand=True,
            bgcolor="#212121",
            border_radius=ft.border_radius.all(10),
            alignment=ft.Alignment.CENTER,
        ft.Row(
            controls=[result],
            alignment=ft.MainAxisAlignment.END,
            ),
        
        ft.Row(
            controls=[
             ft.Button("AC",color=ft.Colors.BLACK, bgcolor="#CFD8DC" ),      
             ft.Button("+/-", color=ft.Colors.BLACK, bgcolor="#CFD8DC"),
             ft.Button("%",color=ft.Colors.BLACK, bgcolor="#CFD8DC"),
             ft.Button("/",color=ft.Colors.BLACK, bgcolor="#FF9800"),
        ]
        ),
        ft.Row(
            controls=[
              ft.Button("7",color=ft.Colors.WHITE, bgcolor="#45484C"),
              ft.Button("8",color=ft.Colors.WHITE, bgcolor="#45484C"),
              ft.Button("9",color=ft.Colors.WHITE, bgcolor="#45484C"),
              ft.Button("*",color=ft.Colors.BLACK, bgcolor="#FF9800"),
        ]
    ),
        ft.Row(
            controls=[
        ft.Button("4",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("5",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("6",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("-",color=ft.Colors.BLACK, bgcolor="#FF9800"),
        ]
    ),
        ft.Row(
            controls=[
        ft.Button("1",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("2",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("3",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("+",color=ft.Colors.BLACK, bgcolor="#FF9800"),
        ]
    ),
        ft.Row(
            controls=[
        ft.Button("0",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button(".",color=ft.Colors.WHITE, bgcolor="#45484C"),
        ft.Button("=",color=ft.Colors.BLACK, bgcolor="#FF9800"),
        ]
    ),
        ),
    )
    
if __name__ == "__main__":
 ft.run(main)
