from flask import Flask, request, redirect, url_for, render_template
import os
import speech_recognition as sr
from test_m import get_speech
from text_control import get_text, Scenary, cut

scene = None
FOLDER = 'scenaries'
filename=''
app = Flask(__name__)

app.config['FOLDER'] = FOLDER

@app.route('/scene_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        global filename
        filename = file.filename
        file.save(os.path.join(app.config['FOLDER'], filename))
        return redirect(url_for('menu'))
    return '''
    <!doctype html>
    <title>Загрузить новый файл</title>
    <h1>Загрузить новый файл</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </html>
    '''

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return '''
    <!doctype html>
    <title>It will be a home page</title>
    <h1>Home page</h1>
    <form action='/menu'>
      <input type=submit value="go to menu">
    </form>
    </html>
    '''

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return '''
    <!doctype html>
    <title>Загрузить новый файл</title>
    <h1>It is menu</h1>
    <form action='/scene_upload'>
    <table>
      <tr><td><input type=submit value="Upload scene"></td><tr>
    </table>
    </form>
    <form action='/prepare'>
    <table>
    <tr><td><input type=submit value="Start rep"></td><tr>
    </table>
    </html>
    '''

@app.route('/prepare', methods=['GET', 'POST'])
def do_prep():
    if request.method == 'POST':
        global filename
        print(filename)
        markers =  request.form['markers'].split('@')
        global scene

        scene = Scenary(f'scenaries/{filename}', markers)
        return redirect(url_for('rep'))
    return '''
    <!doctype html>
    <title>Choose words-markers</title>
    <h1>Choose words-markers</h1>
    <form method=post>
      <input type=text name='markers' placeholder="Input phrases with @ as a delimiter" width=400px>
    </form>
    </html>
    '''


@app.route('/rep')
def rep():
        
    global scene
    txt = get_speech()
        
    try:
        if scene.markers[scene.current] in txt:
            scene.next()

    except:
        pass
    finally:
        return render_template("text.html", text=scene.show_current())




app.run(debug=True)

