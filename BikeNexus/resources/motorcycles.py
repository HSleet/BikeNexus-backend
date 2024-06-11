from flask import request, current_app, jsonify
from flask_restful import Resource
from sqlalchemy import inspect


class Motorcycles(Resource):
    def __init__(self):
        self.database = current_app.database

    def get(self, bike_id=None):
        data = request.get_json()
        if bike_id:
            query_result = self.database.get_motorcycle_by_id(bike_id)
            if query_result:
                return query_result.to_dict()
            
            return {'message': 'Motorcycle not found'}, 404
        elif data:
            return self.database.get_motorcycles(data)
        
        return self.database.get_all_motorcycles()

    def post(self):
        data = request.get_json()
        self.database.create_motorcycle(data)
        return {'message': 'Motorcycle added successfully'}, 201

    def delete(self):
        data = request.get_json()
        self.database.delete_motorcycle(data['id'])
        return {'message': 'Motorcycle deleted successfully'}, 200
    
    def put(self):
        data = request.get_json()
        self.database.update_motorcycle(data['id'], data['make'], data['model'], data['year'])
        return {'message': 'Motorcycle updated successfully'}, 200