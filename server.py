from flask import Flask, render_template, request
from func.gpt_func import give_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        answer = give_response(user_input)
        print(answer)
    return render_template('index.html', answer=answer)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
