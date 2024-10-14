from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/resp")
def render_resp():
    name1 = request.args['name1']
    name2 = request.args['name2']
    genre = request.args['genre']
    tennis = request.args['tennis']
    solo = request.args['Solo']
    reply1 = "hello " + name1 + " " + name2
    if genre == 'option1':
        reply2 = "Thats my favorite genre too, I like Minecraft!"
    else:
        reply2 = "I prefer sandbox games, like Minecraft"
    if tennis == 'option4':
        reply3 = "You are correct, Lucy would completely destory Tyler in a 1v1"
    else:
        reply3 = "Sorry but you are wrong, Tyler is no where near as good as Lucy if they played in a 1v1"
    if Solo == 'option10':
        reply4 = "Correct! Kenji fish slice is the only way to win solo showdown as long as you dont miss"
    if Solo == 'option9':
        reply4 = "Correct, Kit boxing is a guarenteed way to win solo showdown!"
    if Solo == 'option8':
        reply4 = "Correct, Edgar jump can kill anyone"
    if Solo == 'option7':
        reply4 = "No, unless you are Frank this is an absolute garbage and unwinable way to play solo showdown D:"
    if Solo == 'option6':
        reply4 = "You are a villain, no one likes you, delete the game you trashcan"
    return render_template('resp.html', r1 = reply1, r2 = reply2, r3 = reply3, r4 = reply4,  name1=name1, name2=name2, genre=genre, tennis=tennis, Solo=Solo)

if __name__=="__main__":
    app.run(debug=False)


#the fitnessgram pacer test is a multistage aerobic capacity test that progressively gets more difficult as it continues
