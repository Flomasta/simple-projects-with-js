from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.context_processor
def menu_processor():
    menu = [{'name': 'Home', 'url': 'index'},
            {'name': 'About', 'url': 'about'},
            {'name': 'Projects', 'url': 'projects'}]
    return {'menu': menu}


@app.route('/')
def index():  # put application's code here
    title = 'Main Js'
    url_for('index')
    return render_template('index.html', title=title)


@app.route('/about/')
def about():
    title = 'About page'
    url_for('about')
    return render_template('about.html', title=title)


@app.route('/projects/')
def projects():
    url_for('projects')
    title = 'My Projects'
    return render_template('projects.html', title=title)


@app.route('/hex-colors/')
def hex_colors():
    url_for('hex_colors')
    title = 'Hex colors with JS'
    return render_template('hex-colors.html')


@app.route('/random-quotes/')
def random_quotes():
    url_for('random_quotes')
    title = 'Random quotes'
    return render_template('random-quotes.html')


@app.route('/expanding-cart/')
def expanding_cart():
    url_for('expanding_cart')
    title = 'Expanding carts'
    return render_template('expanding-cards.html', title=title)


@app.route('/steps/')
def steps():
    url_for('steps')
    title = 'Steps'
    return render_template('steps.html', title=title)


@app.route('/cool-article/')
def cool_article():
    url_for('cool_article')
    title = 'Cool article'
    return render_template('cool-article.html', title=title)


@app.route('/search-button/')
def search_button():
    url_for('search_button')
    title = 'Search button'
    return render_template('search-button.html', title=title)


@app.route('/blurry-loading/')
def blurry_loading():
    url_for('blurry_loading')
    title = 'Blurry loading'
    return render_template('blurry-loading.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
