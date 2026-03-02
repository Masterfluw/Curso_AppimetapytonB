from flask import Flask, render_template
app = Flask(_name_)
@app.route('/')
def hola_mundo():
    return render_template('holaflask.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,debug=True)
