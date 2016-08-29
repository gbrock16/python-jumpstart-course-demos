import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')


def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (92648)? ')

    html = get_html_from_web(code)

    report = get_weather_from_html(html)

    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

    # display for the forecast


def print_the_header():
    print('--------------------------------------')
    print('             WEATHER APP')
    print('--------------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCSS = 'div#location h1'
    # weatherConditionCSS = 'div#curCond span.wx-value'
    # weather TempCSS = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCSS = 'div#curTemp span.wx-data span.wx-unit'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)

    loc = soup.find(id='location').find('h1').get_text()
    # print(loc)

    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    # print(condition)

    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    # print(temp)

    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()
    # print(scale)

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(condition, temp, scale, loc)

    # return condition, temp, scale, loc

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()
