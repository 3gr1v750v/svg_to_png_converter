"""Конвертирование картинок SVG в PNG в асинхронном режиме."""

import asyncio
import os

import aiohttp
import cairosvg

from utils import count_time_async

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


async def save_image(session, url):
    """
    Скачивание и конвертирование картинок из SVG в PNG.

    Функция получает название SVG изображения и сохраняет PNG с аналогичным
    названием. Размер PNG изображения может регулироваться в настройках,
    размер изменяется пропорционально по соотношинию сторон.

    :return: Сохранение .png изображений в папку png_images
    :rtype: None
    """

    file_name = url.split('/')[-1]
    name = ''.join(file_name[:len(file_name) - 4])

    if not os.path.exists(f'png_images/{name}.png'):
        try:
            async with session.get(url) as response:
                    svg = await response.read()
            cairosvg.svg2png(bytestring=svg, write_to=f'png_images/{name}.png',
                             output_height=1080)
        except Exception:
            print(f"Ошибка скачивания: {url}")
@count_time_async
async def svg_saver():
    """
    Создание списка задач на асинхронное выполнение.

    :return: Список асинхронных задач.
    :rtype: None
    """

    tasks = []

    async with aiohttp.ClientSession() as session:
        for url in get_urls():
            tasks.append(save_image(session, url))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(svg_saver())
