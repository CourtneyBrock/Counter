from flask import Flask, redirect, render_template, session

app = Flask(__name__)
app.secret_key = 'cookie'




@app.route("/")
def index():
    if 'key_name' in session:
        print('key exists!')
    else:
        print("key 'key_name' does NOT exist")
        if ("count" in session):
            session["count"] += 1
        else:
            session["count"] = 0
    return render_template("index.html", count = session["count"])  




@app.route("/destroy")
def clear_session():
    if ("count" in session):
        session.clear()
    return redirect("/")




@app.route("/login")
def visits():
    return redirect ("/")
    
    




if __name__=="__main__":
    app.run(debug=True)