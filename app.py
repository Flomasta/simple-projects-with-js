from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def hello_world():  # put application's code here
    title = 'Main Js'
    return render_template('index.html', title=title)


@app.route('/about/<username>')
def about(username):
    title = 'About page'
    return render_template('about.html', title=title, user=username)


@app.route('/projects/', methods=['GET', 'POST'])
def myProjects():
    if request.method == 'GET':
        print(request.args.get('data'))
        print(request.args.get('lalal'))
    title = 'My Projects'
    return render_template('projects.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
