from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if(email != "abc@gmail.com" or password != "1234"):
            return "Invalid credentials !!"
        else:
            return "Successfully logged in !!"
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
