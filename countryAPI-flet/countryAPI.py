import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, есть ли ошибки при запросе(400-500)

        country_data = response.json()[0]
        # print("API Response:", country_data)  # вывод ответа от API

        official_name = country_data['name']['official']
        capital = ''.join(country_data['capital'])
        currency = country_data['currencies']
        language = ', '.join(country_data['languages'].values())
            
            

        return {
            'Official Name': official_name,
            'Capital': capital,
            'Currency': currency,
            'Language': language
        }

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

    return None

def main():
    country_name = input("Enter country name: ")
    country_info = get_country_info(country_name)

    if country_info:
        print("\nInfo about country:")
        for key, value in country_info.items():
            print(f"{key}: {value}")
    else:
        print("Could not get country information..")

if __name__ == "__main__":
    main()
