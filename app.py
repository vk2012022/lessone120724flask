from flask import Flask
from datetime import datetime
import pytz  # Для учета часового пояса

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now(pytz.timezone("Europe/Moscow"))  # Адаптируйте к вашему часовому поясу
    current_time = now.strftime("%d-%m-%Y %H:%M:%S")
    return f'Текущие дата и время: {current_time}'

if __name__ == "__main__":
    app.run(debug=True)
