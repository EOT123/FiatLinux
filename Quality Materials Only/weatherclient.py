import bs4
import requests


# mom's zip 98406, clintmorn 95368

def main():
    print_the_header()

    code = input("Enter zipcode and I will locate the weather from that region; example(85019):  ")
    print(code)

    get_html_from_web(code)

    get_weather_from_html(code)
    # display the forecast


def print_the_header():
    print("-----------------------------")
    print("         WEATHER APP")
    print("-----------------------------")
    print("")


def get_html_from_web(zipcode):
    url = "https://www.wunderground.com/weather/us/az/phoenix/{}".format(zipcode)
    print(url)
    response = requests.get(url)
    # print(response.status_code)
    print(response.text[0:500])


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    print(soup)


if __name__ == '__main__':
    main()
