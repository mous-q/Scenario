from flask import Flask, request, redirect, url_for, render_template
import os
from text_control import Scenary
from main import main

scene = None
FOLDER = 'scenaries'
filename=''
app = Flask(__name__)
flag = False

app.config['FOLDER'] = FOLDER

@app.route('/scene_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        global filename
        filename = file.filename
        file.save(os.path.join(app.config['FOLDER'], filename))
        return redirect(url_for('menu'))
    return render_template("upload_page.html")

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template("home_page.html")

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template("menu_page.html")

@app.route('/prepare', methods=['GET', 'POST'])
def do_prep():
    if request.method == 'POST':
        global filename
        print(filename)
        markers =  request.form['markers'].lower().split('@')
        global scene

        

        scene = Scenary(f'scenaries/{filename}', markers)
        return redirect(url_for('rep'))
    return render_template("mark_page.html")


@app.route('/rep', methods = ['GET', 'POST'])
def rep():
    if request.method == 'POST':
        return redirect(url_for('foo'))
    return render_template('RH-page.html')


@app.route('/fake')
def foo():
    main(scene)
    return redirect(url_for('home_page'))

@app.get('/now')
def show_current():
    with open('current.txt', 'r', encoding='utf-8') as file:
        c_text = file.read()

    return render_template('new_page.html', text = c_text)

if __name__ == '__main__':
    app.run(debug=True)

