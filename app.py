from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
""" secret_key se generuje pomoc os.urandom(počet znaku davej 24)
    ale obecně je to prostě velké náhodné číslo
    proměnnou secret_key nikdy nesdílím v depozitáři tak jako teď
"""

app.secret_key = b'os.urandom(24)' 


@app.route("/")
def index():
    return render_template("base.html.j2", a=12, b=3.14)


@app.route("/abc/", methods=["GET"])
def abc():
    session['user'] = 'karel'
    try:
        x = request.args.get("x") 
        y = request.args.get("y")
        soucet = int(x) + int(y)
    except TypeError:
        soucet = None
    except ValueError:
        soucet = "Nedělej si srandu!!!"
    
    slovo = request.args.get('slovo')
    if slovo:
        session['slovo'] = slovo

    return render_template("abc.html.j2", soucet=soucet)


@app.route("/abc/", methods=["POST"])
def abc_post():

    jmeno = request.form.get("jmeno")
    heslo = request.form.get("heslo")
    print("POST:", jmeno, heslo)

    return redirect(url_for("abc"))


@app.route("/banany/<parametr>")
def banany(parametr):
    return render_template("banany.html.j2", parametr=parametr)


@app.route("/kvetak/")
def kvetak():
    return render_template("kvetak.html.j2")

@app.route("/Login/", methods=["GET"])
def login():
    if request.method== "GET":
        login=request.args.get("login")
        passwd= request.args.get("password")
        print(name, passwd)
    return render_template("login.html.j2")
    

@app.route("/Login/", methods=["POST"])
def login_post():
    login= request.form.get("login")
    passwd= request.form.get("password")
    print(login, password)
    if login =="mici36" and passwd =="1234":
        session["user"]=login
        flash("úspěšně jses přihlasil", "pass")
    else:
        flash("neplatné přihlašovací údaje", "err")
    return redirect(url_for("login.html.j2"))
