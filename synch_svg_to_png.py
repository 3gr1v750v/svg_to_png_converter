"""Конвертирование картинок SVG в PNG в синхронном режиме."""

import os
import requests

import cairosvg

from utils import count_time_sync


def get_urls():
    """
    Списко ссылок с SVG изображениями на обработку.

    :return: Словарь с ссылками
    :rtype: dict
    """
    url_list = {
        'https://plan.cdn.legenda-dom.ru/vPVXVhjrpR/fZ7RNrHD3hQYKmZ.svg',
        'https://plan.cdn.legenda-dom.ru/vPVXVhjrpR/hDWM6QB3hVpszHC.svg',
        'https://plan.cdn.legenda-dom.ru/vPVXVhjrpR/jvBY34mS7j0zNhs.svg'
    }
    return url_list


@count_time_sync
def svg_saver():
    """
    Скачивание и конвертирование картинок из SVG в PNG.

    Функция получает название SVG изображения и сохраняет PNG с аналогичным
    названием. Размер PNG изображения может регулироваться в настройках,
    размер изменяется пропорционально по соотношинию сторон.

    :return: Сохранение .png изображений в папку png_images
    :rtype: None
    """
    for url in get_urls():
        file_name = url.split('/')[-1]
        name = ''.join(file_name[:len(file_name) - 4])

        if not os.path.exists(f'png_images/{name}.png'):
            try:
                response = requests.get(url)
                svg = response.content
                cairosvg.svg2png(bytestring=svg,
                                 write_to=f'png_images/{name}.png',
                                 output_height=1080)
            except ValueError:
                print(f"Ошибка скачивания: {url}")


if __name__ == '__main__':
    svg_saver()
