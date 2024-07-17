from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    images = [
        "../static/image/img_6.png",
        "../static/image/img_7.png",
        "../static/image/img_8.png"
    ]
    accordion_items = [
        {
            "title": "Сохранение разнообразия",
            "content": "Защита и восстановление естественных экосистем и видов, которые в них обитают, с целью поддержания их разнообразия и функциональности."
        },
        {
            "title": "Снижение загрязнения окружающей среды",
            "content": "Борьба с выбросами вредных веществ в воздух, воду и почву, а также управление отходами для уменьшения их воздействия на природу."
        },
        {
            "title": "Устойчивое использование природных ресурсов",
            "content": "Рациональное и ответственное использование природных ресурсов, таких как вода, древесина и полезные ископаемые, для обеспечения их доступности для будущих поколений и минимизации разрушения окружающей среды."
        }
    ]
    return render_template('home.html', images=images, accordion_items=accordion_items)

@app.route('/about')
def about():
    cards = [
        {
            "title": "Заголовок карточки 1",
            "image": "../static/image/img_2.png",
            "content": "Пример текста для карточки, который демонстрирует содержание."
        },
        {
            "title": "Заголовок карточки 2",
            "image": "../static/image/img_3.png",
            "content": "Пример текста для карточки, который демонстрирует содержание."
        },
        {
            "title": "Заголовок карточки 3",
            "image": "../static/image/img_5.png",
            "content": "Пример текста для карточки, который демонстрирует содержание."
        }
    ]
    return render_template('about.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
