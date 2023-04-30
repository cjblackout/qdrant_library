import flet as ft
import os
from retrieve import retrieve

#default values for Flet
DEFAULT_FLET_PATH = ''
DEFAULT_FLET_PORT = 8080

def main(page: ft.Page):
    def search(e):
        if new_task.value != "":  #If the search bar is not empty
            results = retrieve(new_task.value)  #Get the results from the retrieve function
            for i in range(len(results)):  #Update the cards with the results
                cards.controls[i].content.disabled = False  #Enable the card
                cards.controls[i].content.content.value = results[i]  #Update the card with the result
                cards.controls[i].content.content.update()  #Update the card
        page.update()

    #Set the title and the top markdown
    page.title = "Book Search"
    top_markdown = "Made by Rishabh Saxena for [qdrant.tech](https://qdrant.tech/) with [Flet](https://flet.dev), Sentence Transformers and Python. [Source Code](https://github.com/cjblackout/qdrant_library), [Dataset](https://huggingface.co/datasets/bookcorpusopen)."
    page.add(ft.Markdown(
            top_markdown,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        ))
    
    #Add the search bar and the cards
    new_task = ft.TextField(hint_text="Enter sentence to be searched", on_submit=search)
    page.add(new_task, ft.FloatingActionButton(icon=ft.icons.SEARCH, on_click=search))
    text1 = ft.Text(size=20,color=ft.colors.BLUE_GREY_400,weight=ft.FontWeight.BOLD,)
    text2 = ft.Text(size=20,color=ft.colors.BLUE_GREY_400,weight=ft.FontWeight.BOLD,)
    text3 = ft.Text(size=20,color=ft.colors.BLUE_GREY_400,weight=ft.FontWeight.BOLD,)
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

if __name__ == "__main__":
    flet_path = os.getenv("FLET_PATH", DEFAULT_FLET_PATH)  #Get the path to the flet file
    flet_port = int(os.getenv("FLET_PORT", DEFAULT_FLET_PORT))  #Get the port to run the flet app on
    ft.app(name=flet_path, target=main, view=None, port=flet_port)   #Run the flet app