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
    return """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Contactez-nous</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    padding: 20px;
                }
                form {
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
                input[type="text"], textarea {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    box-sizing: border-box;
                }
                textarea {
                    height: 150px;
                }
                input[type="submit"] {
                    background-color: #4CAF50;
                    color: white;
                    padding: 12px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    float: right;
                }
                input[type="submit"]:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h2>Ma page de contact</h2>
            <form action="/contact/" method="post">
                <label for="fname">Prénom :</label>
                <input type="text" id="fname" name="firstname" placeholder="Votre prénom.." required>

                <label for="lname">Nom :</label>
                <input type="text" id="lname" name="lastname" placeholder="Votre nom.." required>

                <label for="message">Message :</label>
                <textarea id="message" name="message" placeholder="Votre message.." required></textarea>

                <input type="submit" value="Envoyer">
            </form>
        </body>
        </html>
    """

if __name__ == '__main__':
    app.run(debug=True)

