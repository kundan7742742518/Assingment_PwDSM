# ABS = 1
"""
#Flask is a web application framework written in Python.

Lightweight: Flask is a lightweight framework because it is independent of 
external libraries and it gives a quick start for web development having complex 
applications.
"""
# ANS = 2

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!!'

# if __name__ == '__main__':
#     app.run()
""""
I don't know how to attech screenshoot whith vs code if you run this code.
You will getting your ans.
"""
# ANS = 3

""""
In Flask, App routing refers to the process of mapping URLs to view functions.

URL Mapping
Easy to Maintain
Modularization
Flexibility
"""

# ANS = 4

# from flask import Flask

# app = Flask(__name__)

# @app.route('/Welcome')
# def hello_world():
#     return 'Welcome to ABC Corporation'

# @app.route('/')
# def hello_world_1():
#     dic = {"Company Name": "ABC Corporation",
#             "Location" : "India",
#             "Contact Detail": 999-999-9999}
#     return dic

# if __name__ == '__main__':
#     app.run()

""""
I don't know how to use add screenshot run my program and see the ans.
"""

# ANS = 5

""""
Using a (render templet) function 
"""
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def URL_rtl():
    return render_template('index.html')

if __name__ == ("__main__"):
    app.run()
