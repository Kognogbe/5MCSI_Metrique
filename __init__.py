from flask import Flask, render_template
import requests 

app = Flask(__name__)

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route('/')
def hello_world():
    return render_template('hello.html')
@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=59738d3765db6902c9ab2d58c9c8b580')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
@app.route('/histogramme/')
def get_weather_data():
    api_url = 'https://samples.openweathermap.org/data/2.5/forecast?q=Paris,fr&appid=59738d3765db6902c9ab2d58c9c8b580' # Remplacez "xxx" par votre clé d'API OpenWeatherMap
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        daily_weather = []

        # Filtrer les données pour n'inclure que les températures et les dates du jour
        for forecast in data['list']:
            date = forecast['dt_txt'].split(' ')[0]
            temperature = forecast['main']['temp']
            daily_weather.append({'date': date, 'temperature': temperature})

        return render_template('histogramme.html', weather_data=daily_weather)
    else:
        return 'Erreur lors de la récupération des données météorologiques', 500

if __name__ == "__main__":
    app.run(debug=True)
