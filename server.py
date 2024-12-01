from flask import Flask, render_template

app = Flask(__name__)

@app.get('/now')
def show_current():
    with open('current.txt', 'r', encoding='utf-8') as file:
        c_text = file.read()
    return render_template('text.html', text = c_text)

if __name__ == '__main__':
    app.run(debug=True)