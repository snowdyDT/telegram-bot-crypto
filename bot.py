import flask
import util

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        msg = flask.request.get_json()
        chat_id, txt = util.parse_message(msg)
        util.tel_send_button(chat_id)
        if txt.lower() == "parsing":
            util.tel_send_message(chat_id, 'DONE')
        else:
            util.tel_send_message(chat_id, 'Please, click only on the button "Parsing"')

        return flask.Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


if __name__ == '__main__':
    app.run(debug=True)

