import re
import requests

api_url = "http://ohmanda.com/api/horoscope/"
response = requests.get(api_url)

href_regex = r'href=[\'"]?([^\'" >]+)'
allURLs = re.findall(href_regex, response.text)
allURLs = list(dict.fromkeys(allURLs))

if (response.ok):
    day = int(input("Input birthday: "))
    month = input("Input month of birth (e.g. march, july etc): ")
    if 'dec' in month:
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif 'jan' in month:
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif 'feb' in month:
        astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif 'mar' in month:
        astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif 'apr' in month:
        astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif 'may' in month:
        astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif 'jun' in month:
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif 'jul' in month:
        astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif 'aug' in month:
        astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif 'sep' in month:
        astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif 'oct' in month:
        astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif 'nov' in month:
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    else:
        print("Error 404: Can't communicate with API")
        raise SystemExit

astro_url = [url for url in allURLs if url.__contains__(astro_sign.lower())][0]

responseHoroscope = requests.get(astro_url)
horoscopeData = responseHoroscope.json()
sign = horoscopeData.get('sign')
date = horoscopeData.get('date')
horoscope = horoscopeData.get('horoscope')

print(f'Star Sign: {sign}')
print(f'Date: {date}')
print(f'Horoscope: {horoscope}.')
