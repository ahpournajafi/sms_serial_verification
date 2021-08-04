from flask import Flask, jsonify, request
from pandas import read_excel
import requests
import config
app=Flask(__name__)
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

def import_database_from_excel(filepath):
    ''' gets an excel filename and import lookup data (data and failures) frok it '''
    # df contain lookup data in the form of
    # Reference Number	Description	Start Serial	End Serial	Date
    df = read_excel(filepath, 0) 
    for index,(line,ref,  desc, start_serial, end_serial, date) in df.iterrows():
        print(line,ref,  desc, start_serial, end_serial, date)
    df = read_excel(filepath, 1) # sheet one contains failed serial number . only one column .
    for index, i in df.iterrows():
        print(i[0])

def check_serial():
    pass


if __name__=="__main__":
    # send_sms('Hi There', '09375546640') جهت تست برنامه که نیازی به ران کردن هم نیست
    # app.run("127.0.0.1" , 5000, debug=True)
    import_database_from_excel('../../../data.xlsx')