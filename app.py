from flask import Flask, render_template


app = Flask('__name__')




@app.route('/')
def home():

    return render_template('home.html')



if "__main__" == __name__:
    app.run(debug=True)
