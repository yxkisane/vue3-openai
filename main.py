import openai
from flask import Flask, request, make_response
from flask_cors import CORS

server = Flask(__name__)
CORS(server, resources=r'/*')

openai.api_key = ''


def get_completion(message):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{message}",
            temperature=0.9,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=None
        )
    except Exception as e:
        print(e)
        return e
    return response["choices"][0].text


@server.route('/', methods=['GET', 'POST'])
def get_request_json():
    res = {
            'code': 0,
            'answer': "",
            }
    if request.method == 'POST':
        message=request.get_json()['message']
        answer = get_completion(message)
        res['answer']=answer
        return make_response(res)
    return make_response(res)


if __name__ == '__main__':
    server.run(debug=True, host='0.0.0.0', port=8701)
