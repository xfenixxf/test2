import requests


def get_weather(city):
    """
    Получение погоды для указанного города
    """
    # API для погоды (используем бесплатный OpenWeatherMap API)
    # Вам нужно зарегистрироваться на https://openweathermap.org/api и получить API ключ
    api_key = "YOUR_API_KEY"  # Замените на ваш реальный API ключ
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP

        data = response.json()

        # Извлекаем нужные данные
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        # Выводим информацию
        print(f"\n🌍 Погода в городе {city.upper()}:")
        print(f"🌡️ Температура: {temperature}°C")
        print(f"💧 Влажность: {humidity}%")
        print(f"☁️ Описание: {description}")
        print(f"💨 Скорость ветра: {wind_speed} м/с")

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при запросе: {e}")
    except KeyError:
        print(f"❌ Город '{city}' не найден. Проверьте название.")
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")


def main():
    """
    Основная функция программы
    """
    print("🌟 Добро пожаловать в программу погоды!")
    print("Введите название города для получения информации о погоде")
    print("Для выхода введите 'выход' или 'exit'\n")

    while True:
        city = input("🏙️ Введите название города: ").strip()

        if city.lower() in ['выход', 'exit', 'quit']:
            print("👋 До свидания!")
            break

        if city:
            get_weather(city)
            print()  # Пустая строка для разделения
        else:
            print("❌ Пожалуйста, введите название города\n")


if __name__ == "__main__":
    main()