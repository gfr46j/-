from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

users = {None: "Анонімний користувач"}
CURRENT_USER_ID = None

PRODUCTS = [
    {'id': 1, 'name': 'Антуріум', 'price': 320, 'image': 'anthurium.jpg', 'category': 'plants', 'desc': 'Яскрава кімнатна рослина'},
    {'id': 2, 'name': 'Фікус', 'price': 280, 'image': 'ficus.jpg', 'category': 'plants', 'desc': 'Невибаглива зелена рослина'},
    {'id': 3, 'name': 'Монстера', 'price': 520, 'image': 'monstera.jpg', 'category': 'plants', 'desc': 'Велике декоративне листя'},
    {'id': 4, 'name': 'Драцена', 'price': 300, 'image': 'dracaena.jpg', 'category': 'plants', 'desc': 'Очищає повітря'},
    {'id': 5, 'name': 'Арека', 'price': 450, 'image': 'areca.jpg', 'category': 'plants', 'desc': 'Домашня пальма'},

    {'id': 6, 'name': 'Орхідея', 'price': 600, 'image': 'orchid.jpg', 'category': 'flowers', 'desc': 'Елегантна квітка'},
    {'id': 7, 'name': 'Бегонія', 'price': 200, 'image': 'begonia.jpg', 'category': 'flowers', 'desc': 'Компактна та яскрава'},
    {'id': 8, 'name': 'Фіалка', 'price': 150, 'image': 'violet.jpg', 'category': 'flowers', 'desc': 'Класична кімнатна'},
    {'id': 9, 'name': 'Гібіскус', 'price': 350, 'image': 'hibiscus.jpg', 'category': 'flowers', 'desc': 'Великі квіти'},
    {'id': 10, 'name': 'Калатея', 'price': 400, 'image': 'calathea.jpg', 'category': 'flowers', 'desc': 'Декоративне листя'},

    {'id': 11, 'name': 'Маммілярія', 'price': 210, 'image': 'mammillaria.jpg', 'category': 'cactus', 'desc': 'Маленький кактус'},
    {'id': 12, 'name': 'Опунція', 'price': 120, 'image': 'opuntia.jpg', 'category': 'cactus', 'desc': 'Лопатевий кактус'},
    {'id': 13, 'name': 'Ехінопсис', 'price': 180, 'image': 'echinopsis.jpg', 'category': 'cactus', 'desc': 'Цвіте вночі'},
    {'id': 14, 'name': 'Цереус', 'price': 250, 'image': 'cereus.jpg', 'category': 'cactus', 'desc': 'Високий кактус'},
    {'id': 15, 'name': 'Астрофітум', 'price': 300, 'image': 'astrophytum.jpg', 'category': 'cactus', 'desc': 'Зіркоподібний'},

    {'id': 16, 'name': 'Ґрунт універсальний', 'price': 90, 'image': 'soil1.jpg', 'category': 'soil', 'desc': 'Для всіх рослин'},
    {'id': 17, 'name': 'Ґрунт для орхідей', 'price': 95, 'image': 'soil2.jpg', 'category': 'soil', 'desc': 'Легкий субстрат'},
    {'id': 18, 'name': 'Ґрунт для кактусів', 'price': 80, 'image': 'soil3.jpg', 'category': 'soil', 'desc': 'Добрий дренаж'},
    {'id': 19, 'name': 'Торфʼяний ґрунт', 'price': 70, 'image': 'soil4.jpg', 'category': 'soil', 'desc': 'Для розсади'},
    {'id': 20, 'name': 'Перліт', 'price': 75, 'image': 'soil5.jpg', 'category': 'soil', 'desc': 'Покращує ґрунт'},

    {'id': 21, 'name': 'Керамічний вазон', 'price': 250, 'image': 'pot1.jpg', 'category': 'pots', 'desc': 'Міцний'},
    {'id': 22, 'name': 'Пластиковий вазон', 'price': 120, 'image': 'pot2.jpg', 'category': 'pots', 'desc': 'Легкий'},
    {'id': 23, 'name': 'Скляний вазон', 'price': 180, 'image': 'pot3.jpg', 'category': 'pots', 'desc': 'Сучасний'},
    {'id': 24, 'name': 'Вазон з піддоном', 'price': 300, 'image': 'pot4.jpg', 'category': 'pots', 'desc': 'Зручний'},
    {'id': 25, 'name': 'Деревʼяний вазон', 'price': 200, 'image': 'pot5.jpg', 'category': 'pots', 'desc': 'Еко стиль'},

    {'id': 26, 'name': 'Камінці', 'price': 150, 'image': 'decor1.jpg', 'category': 'decor', 'desc': 'Для декору'},
    {'id': 27, 'name': 'Фігурки', 'price': 60, 'image': 'decor2.jpg', 'category': 'decor', 'desc': 'Прикраса'},
    {'id': 28, 'name': 'Мох', 'price': 110, 'image': 'decor3.jpg', 'category': 'decor', 'desc': 'Натуральний'},
    {'id': 29, 'name': 'Підставка', 'price': 90, 'image': 'decor4.jpg', 'category': 'decor', 'desc': 'Для вазонів'},
    {'id': 30, 'name': 'Кора', 'price': 130, 'image': 'decor5.jpg', 'category': 'decor', 'desc': 'Для мульчі'},
]

theme = {
    "accent_text_color": "#6ab2f2",
    "bg_color": "#17212b",
    "button_color": "#5288c1",
    "button_text_color": "#ffffff",
    "bottom_bar_bg_color": "#ffffff",
    "destructive_text_color": "#ec3942",
    "header_bg_color": "#17212b",
    "hint_color": "#708499",
    "link_color": "#6ab3f3",
    "secondary_bg_color": "#232e3c",
    "section_bg_color": "#17212b",
    "section_header_text_color": "#6ab3f3",
    "subtitle_text_color": "#708499",
    "text_color": "#f5f5f5"
}

@app.route("/")
def index():
    category = request.args.get("category")
    query = request.args.get("q", "")

    products = PRODUCTS
    if category:
        products = [p for p in products if p["category"] == category]
    if query:
        products = [p for p in products if query.lower() in p["name"].lower()]

    return render_template("index.html", products=products, user=users[CURRENT_USER_ID])

@app.route("/add_to_cart/<int:pid>",)
# @app.route("/add_to_cart/<int:pid>", methods=["POST"])
def add_to_cart(pid):
    cart = session.get("cart", [])
    cart.append(pid)
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart_ids = session.get("cart", [])
    items = [p for p in PRODUCTS if p["id"] in cart_ids]
    return render_template("cart.html", items=items)

@app.route("/remove/<int:pid>")
def remove(pid):
    cart = session.get("cart", [])
    if pid in cart:
        cart.remove(pid)
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/buy", methods=["GET", "POST"])
def buy():
    # telegram data which needs to be parsed and validated to identify the user
    # tg_init_data = request.form.get('tg_init_data')
    history = session.get("history", [])
    cart_ids = session.get("cart", [])
    for p in PRODUCTS:
        if p["id"] in cart_ids:
            history.append(p)
    session["history"] = history
    session["cart"] = []
    return redirect(url_for("history"))

@app.route("/history")
def history():
    return render_template("history.html", history=session.get("history", []))

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        PRODUCTS.append({
            "id": len(PRODUCTS) + 1,
            "name": request.form["name"],
            "price": int(request.form["price"]),
            "image": request.form["image"],
            "category": request.form["category"],
            "desc": request.form["desc"]
        })
        return redirect("/")
    return render_template("add_product.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

