from flask import Flask
from flask_restful import Api 
from db import Database
from resources.motorcycles import Motorcycles

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///motorcycles.db'

app.database = Database(app)


api.add_resource(Motorcycles, '/motorcycles', '/motorcycles/', '/motorcycles/<int:bike_id>')

if __name__ == '__main__':
    app.run(debug=True)


