from flask import Flask, request, redirect, url_for, render_template
import os
from text_control import Scenary
from main import main
from flask import jsonify
from multiprocessing import Process, Queue 

scene = None
FOLDER = 'scenaries'
filename='' 
app = Flask(__name__)
flag = False
main_queue = Queue()

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
    p = Process(target=main, args=(scene, main_queue))
    p.start()
    return redirect(url_for('show_current'))

@app.get('/now')
def show_current():

    return render_template('new_page.html')
 
@app.get('/newtext')
def show_current_text():
    c_text, roles, next = main_queue.get()
    roles = ' '.join(roles)
    next = ' '.join(next)

    print(c_text, roles, next)

    data = { "text" : c_text , "roles": roles, "next" : next } 
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

