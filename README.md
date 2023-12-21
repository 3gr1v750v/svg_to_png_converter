# Конвертирование изображений SVG в PNG

# О проекте
Конвертация SVG изображений в PNG в синхронном и асинхронном режиме.

Асинхронный режим работает быстрее, однако в зависимости от хоста, на котором
лежат SVG файлы, соединение может быть разорвано хостом при превышении
количества одновременных попыток скачивания изображений.

Дополнительно в проект добавлен декоратор для оценки времени исполнения
конвертации изображений.

Изображения сохраняются в папку: png_images

# Технологии
- Python 3.11
- cairosvg
- requests
- asyncio
- aiohttp

# Установка и запуск
Документация библиотеки cairosvg: https://cairosvg.org/documentation/

**Windows**

Дополнительно необходимо скачать и установить в операционной системе
`gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe`

Ссылка: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

**Linux**

Необходимо установить в операционную систему следующие пакеты
- cairo
- python3-dev
- libffi-dev

```
RUN apt-get -y install libcairo2-dev libffi-dev python3-dev
```