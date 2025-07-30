from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route("/videogame")
def index():
    image1= "https://i.pinimg.com/736x/a4/73/cd/a473cda6c0a58d9b2e2bc2292d16c334.jpg"
    image2= "https://preview.redd.it/who-else-vividly-remembers-the-monopoly-man-with-a-monocle-v0-yamto4atoe5a1.jpg?width=640&crop=smart&auto=webp&s=4ac305734613dc641bf47c3169faca87291b6bf4"
    return render_template("videogame.html", image1=image1, image2=image2 )

@app.route("/videogame2")
def index2():
    image3="/static/image3.png"
    image4="/static/image4.png" 
    return render_template("videogame.html", image1=image3, image2=image4 )
    



if __name__ == '__main__':
    app.run(debug=True)
