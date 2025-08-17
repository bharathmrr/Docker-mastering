from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return """
<html>
<body>
<h1>Hello, Docker!</h1>
<form action="/great" method="POST">
enter your name:<input type="text" name="username">
<input type="submit" value="Submit">
</form>
</body>
</html>
"""
@app.route('/great', methods=['POST'])
def great():
    username = request.form.get('username')
    return f"hello {username}, welcome to the world of Docker!"
if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1")