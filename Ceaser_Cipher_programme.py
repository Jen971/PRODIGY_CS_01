from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, key, mode='encrypt'):
    result = ''
    key = int(key)
    if mode == 'decrypt':
        key = -key
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + key) % 26 + offset)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form.get('text') or ''
        key = request.form.get('key') or 0
        mode = request.form.get('mode')
        if text and key:
            result = caesar_cipher(text, key, mode)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
