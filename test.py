import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def get_usd_to_rub_exchange_rate():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()

    usd_to_rub_rate = data['Valute']['USD']['Value']

    return usd_to_rub_rate


def get_exchange_rates_for_days(days):
    rates = []
    dates = []
    for i in range(days):
        date = datetime.now() - timedelta(days=i)
        formatted_date = date.strftime('%Y-%m-%d')
        formatted_date = formatted_date.replace('-', '/')
        url = f'https://www.cbr-xml-daily.ru/archive/{formatted_date}/daily_json.js'
        try:
            response = requests.get(url)
            print(response.status_code)
            data = response.json()
            usd_to_rub_rate = data['Valute']['USD']['Value']
            rates.append(usd_to_rub_rate)
            dates.append(formatted_date)
        except Exception as e:
            print(f"Ошибка при получении данных за {formatted_date}: {e}")
            try:
                rates.append(rates[i - 1])
            except:
                rates.append(None)
            dates.append(formatted_date)

    return dates[::-1], rates[::-1]  # Возвращаем даты и курсы в правильном порядке


'''# Получаем курсы за последние 7 дней
days = 10
dates, exchange_rates = get_exchange_rates_for_days(days)

# Строим график
plt.figure(figsize=(10, 5))
plt.plot(dates, exchange_rates, marker='o')
plt.title('Курс доллара к рублю за последние 7 дней')
plt.xlabel('Дата')
plt.ylabel('Курс USD/RUB')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
'''