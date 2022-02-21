from flask import Flask
from flask import request
from flask import render_template

app = Flask(_name_)

#Pirmā lapa,kas tika ielādēta
@app.route('/')
def root():
    return render_template("index.html")

#Pārbaudes lapa,lai saprastu,kā kods vispār stradā
@app.route('/health')
def health():
    return "OK"

if _name_ == '__main__':
    app.run(debug="true")