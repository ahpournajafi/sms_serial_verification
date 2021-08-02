from flask import Flask, jsonify, request
import requests
import config

# @app.route('/')
# def main_page():
#     '''
#     This Is The Main Page Of Site
#     '''
#     return 'Hello'

@app.route('/v1/process', methods=['POST'])

def process():
    '''This Is A Call Back From Kavehnegar . Will Get Sender And Message And Will Check If IT Is Valid , Then Answer Back .'''
    data=request.form
    sender=data['from']
    message=data['message']
    print(f'Recevied {message} From {sender}')
    send_sms('Hi '+message, sender )
    ret={"message":"Processed"}
    return jsonify(ret), 200

def send_sms(message, receptor):
    '''This Function Will Get MSISDN Then Uses From Kavehnegar To Send SMS . '''
    url = f'https://api.kavenegar.com/v1/{config.API_KEY}/sms/send.json'
    data={
        "message": message,
        "receptor": receptor
    }
    r = requests.post(url, data)
    print(f'message *{message}* sent . status code is {r.status_code}')
def check_serial():
    pass


if __name__=="__main__":
    # send_sms('Hi There', '09375546640') جهت تست برنامه که نیازی به ران کردن هم نیست
    # app.run("127.0.0.1" , 5000, debug=True)