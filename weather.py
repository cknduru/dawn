import requests
import subprocess
import json

API_KEY = '02ca068cb18a28713c42fd8c6356a025'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

# data for latest request
last_weather = ''

def get_weather_desc(js):
    return js['weather'][0]['description']

def mock_weather():
    file = open('/home/pi/temp/json.j', 'r')
    return file.read()

def parse_raw_response(raw):
    parsed_json = json.loads(raw)
    return parsed_json    

def get_raw_response():
    #cmd = "curl -s --request GET --url \'http://api.openweathermap.org/data/2.5/weather?q=Aalborg%2Cdk&units=metric&appid=02ca068cb18a28713c42fd8c6356a025\'"
    #proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    
    #lines = ''

    #for line in proc.stdout.readlines(): #read and store result in log file
    #    lines += line
    
    #j = parse_raw_response(lines)
    #print(j)
    global last_weather
    last_weather = get_weather_desc(parse_raw_response(mock_weather()))

def update_weather():
    get_raw_response()
