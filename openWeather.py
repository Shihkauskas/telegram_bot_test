import requests
import config
import time

params = {
    'q': 'Chelyabinsk',
    'units': 'metric',
    'lang': 'ru',
    'appid': '11c0d3dc6093f7442898ee49d2430d20'
}


def weather():
    data_current = requests.get(config.current, params=params).json()
    current_weath = 'Температура в {}e \n\n\tтекущая температура: {}\u00b0'.format(
        data_current['name'],
        data_current['main']['temp']
    )

    return current_weath


def forecast():
    forecast = ''
    data_forecast = requests.get(config.forecast, params=params).json()
    for day_data in data_forecast['list'][2::8]:
        for weath in day_data['weather']:
            forecast += day_data['dt_txt'][0:10] + ' '
            forecast += 'мин: ' + format(day_data['main']['temp_min'], '.1f') + '\u00b0' + ' '
            forecast += 'макс: ' + format(day_data['main']['temp_max'], '.1f') + '\u00b0' + ' '
            forecast += weath['description'] + ' '
            forecast += '\n'
    return forecast
