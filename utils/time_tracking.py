import time

def count_time_sync(function):
    """Декоратор для оценки ввремени работы приложения."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        processing_time = time.time() - start_time
        print(f"Время обработки: {processing_time}")

    return wrapper

def count_time_async(function):
    """Декоратор для оценки времени работы асинхронного приложения."""

    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await function(*args, **kwargs)
        processing_time = time.time() - start_time
        print(f"Время обработки: {processing_time}")
        return result

    return wrapper