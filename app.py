from flask import Flask, request,redirect
from flask_mail import Mail, Message

#from decouple import Env

#env = Env()
#env.read_env()

app = Flask(__name__)
email = os.environ.get('EMAIL')
api_key = os.environ.get('API_KEY')

app.config['MAIL_SERVER'] = email
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = api_key
app.config['MAIL_DEFAULT_SENDER'] =email
app.config['MAIL_USE_TLS']=False  #SSL stands for Secure Sockets Layer, and is a protocol that protects communication over the internet
app.config['MAIL_USE_SSL']=True
mail = Mail(app)

@app.route('/',methods=['GET', 'POST'])
def print_array():
    # Create an array of dictionaries
    my_array = [
    {"email": "ap4992@srmist.edu.in", "Cont": "Hi dude","mission":"save the world"},
    {"email": "adhavanponram@gmail.com", "Cont": "Hi Adhavan","mission":"Never give up"},
    {"email": "Superhero8871@gmail.com", "Cont": "Hi Hero","mission":"win the war at any cause"}
    ]
# Loop through the array and print the contents of each dictionary
    for item in my_array:
        def message(Var1,Var2,Var3):
              msg = Message(subject= Var1, sender='Superhero8871@gmail.com', recipients=[Var2])
              msg.body = str(Var3)
              mail.send(msg)
              print(msg)
              print(Var2)
              print(Var3)
        message(item["mission"],item["email"],(item["Cont"]))
    return 'Array printed!'

if __name__ == '__main__':
    app.run()
