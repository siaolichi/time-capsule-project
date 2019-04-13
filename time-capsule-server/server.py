from flask import Flask, request, render_template, make_response, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import sys
import os
import re
import json
from models import seq2seq_res
from models import luis_response
from models.luis_sdk import LUISClient

APPID = '27ed8363-23a9-4c7f-9be9-2e087b81f57a'
APPKEY = '5aadbf6e015245c59e2dd38f06d33b41'
CLIENT = LUISClient(APPID, APPKEY, True)
app = Flask(__name__)
CORS(app)

"""
# BUILD CHATBOT RESPONSE
"""
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Time Capsule API"

@app.route("/response", methods=["POST"])
def reponse():
    data = request.json
    user_sentence = data['user_sentence']
    data = json.dumps(data)
    client_data = CLIENT.predict(user_sentence)
    luis_intent = luis_response.process_res(client_data)
    if (luis_intent['score'] < 0.5) or (luis_intent['intent'] == 'None'):
        print('[answer from seq2seq]')
        respond = dict(channel='seq2seq', response=seq2seq_res.response(user_sentence))
    else:
        print('[answer from LUIS]')
        respond = dict(channel='LUIS', response=luis_intent['response'])
    resp = make_response(jsonify(respond))
    resp.status_code = 200
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@app.route("/sound", methods=["POST"])
def generateTTS():
    data = request.json["generate_sound"]
    data = re.sub(r" ", "+", data)
    input_text = re.sub(r"\!|\.|\,|\?|\"", "", data)
    response_sound_text = (
        '<audio src="http://localhost:59125/process?INPUT_TYPE=TEXT&amp;OUTPUT_TYPE=AUDIO&amp;INPUT_TEXT='
        + input_text
        + '&;AUDIO_OUT=WAVE_FILE&amp;LOCALE=en_US&amp;VOICE=new_voice&amp;AUDIO=WAVE_FILE" autoplay="" controls=""></audio>'
    )
    # print(response_sound_text)
    resp = make_response(response_sound_text)
    resp.status_code = 200
    # resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8090)
