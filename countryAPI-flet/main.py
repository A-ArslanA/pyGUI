import flet as ft
import requests


def main(page: ft.Page):
    page.title = 'Que'
    page.theme_mode = 'dark' 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    userInput = ft.TextField(hint_text='Country name:', label='Enter country name', width=200)
    official_name = ft.Text('')
    capital = ft.Text('')
    currency = ft.Text('')
    languages = ft.Text('')

    def get_country_info(e):
        url = f"https://restcountries.com/v3.1/name/{userInput.value}"

        try:
            response = requests.get(url)
            response.raise_for_status() 

            country_data = response.json()[0]
            # print("API Response:", country_data)  # вывод ответа от API

            official_name.value = country_data['name']['official']
            capital.value = ''.join(country_data['capital'])
            currency.value = country_data['currencies']
            languages.value = ', '.join(country_data['languages'].values())
            page.update()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")

        return None


    page.add(
        ft.Row([ft.Icon(ft.icons.HOME)],alignment=ft.MainAxisAlignment.CENTER),

        ft.Row(
            [
                ft.Text('This app return info about Country! 🎓', size=20),
            ],
            alignment=ft.MainAxisAlignment.CENTER

        ),

        ft.Row(
            [
                userInput
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row(
            [
                ft.IconButton(ft.icons.SEARCH, icon_color=ft.colors.GREEN_200, on_click=get_country_info)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),

        ft.Row([official_name], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([capital], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([currency], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([languages], alignment=ft.MainAxisAlignment.CENTER),
    )


ft.app(target=main)
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)

