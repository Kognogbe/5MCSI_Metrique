from flask import Flask, render_template

app = Flask(__name__)

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route('/')
def hello_world():
    return render_template('hello.html')
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
