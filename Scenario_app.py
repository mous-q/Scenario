from flask import Flask, request, redirect, url_for, render_template
import os
from text_control import Scenary
from main import main
from flask import jsonify
from multiprocessing import Process, Queue
import sys


FOLDER = 'scenaries'
filename = None

main_queue: Queue = Queue()


app = Flask(__name__)
app.config['FOLDER'] = FOLDER



# @app.route('/start', methods=['GET', 'POST'])
# def home_page():
#     return render_template("home_page.html")


@app.get('/home')
def home_page():
    return render_template('home_page.html')


@app.route('/home/menu', methods=['GET', 'POST'])
def menu():
    return render_template("menu_page.html")


@app.route('/home/create_scenary')
def create_scenary():
    return render_template('creation.html')


@app.route('/home/create_scenary/scene_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        global filename
        filename = '_'.join(file.filename.split())
        file.save(os.path.join(app.config['FOLDER'], filename))
        return redirect(url_for('create_scenary'))
    return render_template("upload_page.html")


@app.route('/home/create_scenary/get_markers', methods = ['GET', 'POST'])
def get_markers():
    global filename
    if request.method == 'POST':
        markers = request.json['markers']
        with open(os.path.join(sys.path[0], os.path.normpath(f'scenaries/{filename.replace('.txt', '')}_mr.txt')), 'w', encoding='utf-8') as file:
            file.write('@'.join(markers))
        return {'message' : 'Success'}
    
    
    file = open(os.path.join(sys.path[0], os.path.normpath(f'scenaries/{filename}')), 'r', encoding='utf-8')

    return render_template('test.html', text = file.read())


@app.route('/home/menu/rehearsal', methods=['GET', 'POST'])
def start_rehearsal():
    if request.method == 'POST':
        filename = request.json['name']
        p = Process(target=main, args=(Scenary(filename), main_queue))
        p.start()
        return redirect(url_for('show_current'))
    return render_template('rehearsal.html')


@app.get('/home/menu/rehearsal/show_current')
def show_current():
    return render_template('new_page.html')


@app.get('/newtext')
def newtext():
    c_text, roles, next = main_queue.get()
    roles = ' '.join(roles)
    next = ' '.join(next)

    data = { "text" : c_text , "roles": roles, "next" : next }
    return jsonify(data)


@app.get('/files')
def files():
    files: list[str] = os.listdir(os.path.join(sys.path[0], os.path.normpath('scenaries')))
    files = [file.replace('.txt', '') for file in files if not(file.endswith('mr.txt'))]
    data = {"files" : files}
    return jsonify(data)



if __name__ == '__main__':
    app.run()