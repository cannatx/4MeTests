import requests
import bs4
import collections #para ordenar las tuplas

WeatherReport = collections.namedtuple('WeatherReport',
                                        'cond, temp, scale, loc'
                                        )

def main():
    print_the_header()
    code = input('What ZIPcode do you want the weather for.... (#####)? ')
    html = get_html_from_web(code)
    #report = get_weather_from_html(html)

    #print('The temp in {} is {} and {} {}'.format(
    #    report.loc,
    #    report.temp,
    #    report.scale,
    #    report.cond
    #))

    #print('The temp in {} is {} and {} {}'.format(
    #    report[2],
    #    report[0],
    #    report[1],
    #    report[3]
    #))


def print_the_header():
    print('----------------------------------------')
    print('           Wheather APP                 ')
    print('----------------------------------------')
    print('')


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    #print(url)
    response = requests.get(url)
    #print(response.status_code)
    #print(response.js)

    print(response.text)

    return response.text



def get_weather_from_html(html):
    #cityCss = 'div#location h1'
    #weatherConditionCss = 'div#curCond span.wx-value'
    #weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    #weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'


    soup = bs4.BeautifulSoup(html, 'html.parser')
    #print(soup)
    loc = soup.find(id='location').find('h1').get_text()
    #print(loc)

    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = clenup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = clenup_text(condition)
    temp = clenup_text(temp)
    scale = clenup_text(scale)


    #print(condition, temp, scale, loc)

    #return condition, temp, scale, loc  # tupla sin collection

    report = WeatherReport(cond=condition,temp=temp, loc=loc, scale=scale)
    return report

def find_city_and_state_from_location(loc_: str):
    parts = loc.split('\n')
    return parts[0].strip()


def cleanup_text(text_: str):  # estamos diciendo el tipo de dato que sera con lo que aparecerán los metodos en la ayuda
    if not text:        # text == false so no text
        return text

    text = text.strip()
    return text



if __name__ == '__main__':
    main()