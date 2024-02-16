from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        message = request.form['message']
        # Traitez les données du formulaire ici (par exemple, envoyez un email, sauvegardez les données dans une base de données, etc.)
        # Pour cet exemple, nous allons simplement afficher les données saisies
        return f"""
            <h2>Merci {firstname} {lastname} !</h2>
            <p>Votre message a été envoyé avec succès :</p>
            <p>{message}</p>
        """
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
