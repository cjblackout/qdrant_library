import flet as ft
import os
from retrieve import retrieve

DEFAULT_FLET_PATH = ''  # or 'ui/path'
DEFAULT_FLET_PORT = 8080

def main(page: ft.Page):
    def search(e):
        if new_task.value != "":
            results = retrieve(new_task.value)
            text1.value = results[0].payload["book_title"].replace("-", " ") + " with a match of  " + str(round(results[0].score*100)) + "%"
            cards.controls[0].content.disabled = False
            text2.value = results[1].payload["book_title"].replace("-", " ") + " with a match of  " + str(round(results[1].score*100)) + "%"
            cards.controls[1].content.disabled = False
            text3.value = results[2].payload["book_title"].replace("-", " ") + " with a match of  " + str(round(results[2].score*100)) + "%"
            cards.controls[2].content.disabled = False
        cards.controls[0].content.content.update()
        cards.controls[1].content.content.update()
        cards.controls[2].content.content.update()
        page.update()

    new_task = ft.TextField(hint_text="Enter sentence to be searched")

    page.title = "Book Search"
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=search))
    text1 = ft.Text()
    text2 = ft.Text()
    text3 = ft.Text()
    cards = ft.Column([
            ft.Card(
                        content=ft.Container(
                            content=text1,
                            width=400,
                            padding=10,
                        ),
                        disabled=True
                    ),
            ft.Card(
                        content=ft.Container(
                            content=text2,
                            width=400,
                            padding=10,
                        ),
                        disabled=True
                    ),
            ft.Card(
                        content=ft.Container(
                            content=text3,
                            width=400,
                            padding=10,
                        ),
                            
                    ),
        ])
    page.add(cards)

#ft.app(target=)
if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))
    ft.app(name=flet_path, target=main, view=None, port=flet_port)