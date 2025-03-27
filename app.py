from flask import Flask, request, url_for, redirect, session
app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def home():
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f4f4f9;
                color: #333;
                text-align: center;
                padding: 20px;
            }}
            a {{
                display: inline-block;
                margin: 10px;
                padding: 12px 24px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                font-weight: bold;
            }}
            a:hover {{
                background-color: #45a049;
            }}
            h1 {{
                color: #333;
                font-size: 32px;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to the Homepage</h1>
        <a href="{url_for('profile')}">Go to Profile</a>
        <a href="{url_for('submit')}">Go to Submit Page</a>
    </body>
    </html>
    '''

@app.route('/profile')
def profile():
    name = session.get('name', 'Guest')
    age = session.get('age', 'Unknown')
    return f'''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #f0f8ff;
                text-align: center;
                color: #333;
                padding: 20px;
            }}
            h1 {{
                color: #5a5a5a;
                font-size: 32px;
            }}
            p {{
                font-size: 18px;
                margin-top: 10px;
            }}
            a {{
                margin-top: 20px;
                display: inline-block;
                padding: 10px 20px;
                background-color: #ff6347;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #ff4500;
            }}
        </style>
    </head>
    <body>
        <h1>Profile Page</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Age:</strong> {age}</p>
        <a href="{url_for('home')}">Back to Homepage</a>
    </body>
    </html>
    '''

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        session['name'] = request.form.get('name', 'Unknown')
        session['age'] = request.form.get('age', 'Unknown')
        return redirect(url_for('profile'))

    return '''
    <html>
    <head>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #fafad2;
                text-align: center;
                color: #333;
                padding: 20px;
                margin: 0;
            }
            .form-container {
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
                display: inline-block;
                width: 60%;
                text-align: left;
            }
            h1 {
                color: #333;
                font-size: 36px;
                margin-bottom: 20px;
            }
            label {
                font-size: 18px;
                margin-bottom: 10px;
                display: block;
                color: #555;
            }
            input {
                margin: 10px 0;
                padding: 12px 20px;
                border-radius: 5px;
                border: 1px solid #ccc;
                font-size: 16px;
                width: 100%;
            }
            input[type="submit"] {
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
                width: 100%;
                padding: 15px;
                font-size: 18px;
                border-radius: 5px;
            }
            input[type="submit"]:hover {
                background-color: #45a049;
            }
            .back-link {
                margin-top: 20px;
                display: inline-block;
                padding: 12px 24px;
                background-color: #ff6347;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            .back-link:hover {
                background-color: #ff4500;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Submit Your Information</h1>
            <form method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required><br>
                <label for="age">Age:</label>
                <input type="number" id="age" name="age" required><br>
                <input type="submit" value="Submit">
            </form>
            <a href="{url_for('home')}" class="back-link">Back to Homepage</a>
        </div>
    </body>
    </html>
    '''

    if request.method == 'POST':
        session['name'] = request.form.get('name', 'Unknown')
        session['age'] = request.form.get('age', 'Unknown')
        return redirect(url_for('profile'))

    return '''
    <html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                background-color: #fafad2;
                text-align: center;
                color: #333;
                padding: 20px;
            }}
            form {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            input {{
                margin: 10px;
                padding: 12px 20px;
                border-radius: 5px;
                border: 1px solid #ccc;
                font-size: 16px;
            }}
            input[type="submit"] {{
                background-color: #4CAF50;
                color: white;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background-color: #45a049;
            }}
            h1 {{
                color: #333;
                font-size: 32px;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 12px 24px;
                background-color: #ff6347;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }}
            a:hover {{
                background-color: #ff4500;
            }}
        </style>
    </head>
    <body>
        <h1>Submit Your Information</h1>
        <form method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" required><br>
            <label for="age">Age:</label><br>
            <input type="number" id="age" name="age" required><br><br>
            <input type="submit" value="Submit">
        </form>
        <a href="{url_for('home')}">Back to Homepage</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
