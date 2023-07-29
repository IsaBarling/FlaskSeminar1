from flask import Flask, render_template

app = Flask(__name__)

# Предположим, у вас есть данные о предметах в каждой категории
clothes_data = [
    {'name': 'Футболка', 'color': 'красный', 'price': 500},
    {'name': 'Шорты', 'color': 'синий', 'price': 700},
]

shoes_data = [
    {'name': 'Кроссовки', 'color': 'черный', 'price': 1500},
    {'name': 'Сандалии', 'color': 'коричневый', 'price': 1000},
]

jacket_data = [
    {'name': 'Пальто', 'color': 'черный', 'price': 2500},
    {'name': 'Куртка', 'color': 'серый', 'price': 1800},
]

@app.route('/')
def index():
    return render_template('base.html', title='Главная')

@app.route('/products/')
def products():
    print(clothes_data)
    print(shoes_data)
    print(jacket_data)

    return render_template('products.html', title='Товары', items_clothing=clothes_data, items_shoes=shoes_data, items_jackets=jacket_data)

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html', title='Контакты')

if __name__ == '__main__':
    app.run()
