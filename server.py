"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""

    return render_template("form.html")

@app.route('/results')
def show_results():
    """Show resulting message."""
    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')

    if cheery:
        msg = "You are good"

    elif honest:
        msg = "dadadaa"
    elif dreary:
        msg = "HOHOHOHOHOH"


    return render_template("results.html", message= msg)

@app.route("/save-name", methods=['POST'])
def save_name():
    
    name = request.form.get('name')#value name taken from homepaeg.html
    session['name']=name
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
