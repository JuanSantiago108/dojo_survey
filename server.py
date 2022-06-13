
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'




# @app.route('/todos')

@app.route('/')
@app.route('/result')
def creat():
    return render_template("index.html")



@app.route('/process',methods = ['POST'] )
def get_():
    session["new_info"] = {
        "fname": request.form["fname"],
        "dojo_loaction": request.form["dojo_loaction"],
        "favorite_language": request.form["favorite_language"],
        "commit": request.form["commit"],
    }
    return redirect("/process/new")


@app.route("/process/new")
def display_create_todo():
    return render_template( "result.html" )






if __name__=="__main__":
    app.run(debug=True)