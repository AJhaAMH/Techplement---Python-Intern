from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    use_uppercase = 'uppercase' in request.form
    use_lowercase = 'lowercase' in request.form
    use_numbers = 'numbers' in request.form
    use_specials = 'specials' in request.form

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials)
        return render_template('index.html', password=password)
    except ValueError as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)

