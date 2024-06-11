from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, joinedload
from flask_sqlalchemy import SQLAlchemy
from models.motorcycles import Base, Motorcycle, Performance, Dimensions, Brakes, Engine, Suspension, Tires, Miscellaneous


class Database:

    def __init__(self, app):
        self.uri = app.config['SQLALCHEMY_DATABASE_URI']
        self.db = SQLAlchemy(app)
        self.engine = create_engine(self.uri)
        self.Session = scoped_session(sessionmaker(bind=self.engine, autocommit=False, autoflush=False))

    def create_motorcycle(self, data):
        session = self.Session()
        motorcycle = Motorcycle(**data)

        session.add(motorcycle)
        session.commit()
        session.close()
        return motorcycle

    def get_motorcycles(self, **data):
        session = self.Session()

        motorcycle = session.query(Motorcycle).filter_by(**data).all()
        session.close()
        return motorcycle
    
    def get_all_motorcycles(self):
        session = self.Session()

        motorcycles = session.query(Motorcycle).all()
        session.close()
        return motorcycles
    
    def get_motorcycle_by_id(self, id):
        session = self.Session()

        motorcycle = session.query(Motorcycle)\
                    .options(joinedload(Motorcycle.performance),
                                joinedload(Motorcycle.dimensions),
                                joinedload(Motorcycle.brakes),
                                joinedload(Motorcycle.engine),
                                joinedload(Motorcycle.suspension),
                                joinedload(Motorcycle.tires),
                                joinedload(Motorcycle.miscellaneous))\
                    .filter(Motorcycle.id == id).first()
        session.close()
        return motorcycle
    
    def get_motorcycles(self):
        session = self.Session()

        motorcycles = session.query(Motorcycle).all()
        session.close()
        return motorcycles

    def update_motorcycle(self, id, data):
        session = self.Session()

        motorcycle = session.query(Motorcycle).filter(Motorcycle.id == id).first()
        for key, value in data.items():
            setattr(motorcycle, key, value)
        session.commit()
        session.close()
        return motorcycle

    def delete_motorcycle(self, id):
        session = self.Session()

        motorcycle = session.query(Motorcycle).filter(Motorcycle.id == id).first()
        session.delete(motorcycle)
        session.commit()
        session.close()
        return motorcycle

    def create_performance(self, motorcycle_id, data):
        session = self.Session()

        performance = Performance(motorcycle_id=motorcycle_id, **data)
        session.add(performance)
        session.commit()
        session.close()
        return performance

    def get_performance(self, motorcycle_id):
        session = self.Session()

        performance = session.query(Performance).filter(Performance.motorcycle_id == motorcycle_id).first()
        session.close()
        return performance

    def update_performance(self, motorcycle_id, data):
        session = self.Session()

        performance = session.query(Performance).filter(Performance.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(performance, key, value)
        session.commit()
        session.close()
        return performance

    def delete_performance(self, motorcycle_id):
        session = self.Session()

        performance = session.query(Performance).filter(Performance.motorcycle_id == motorcycle_id).first()
        session.delete(performance)
        session.commit()
        session.close()
        return performance

    def create_dimensions(self, motorcycle_id, data):
        session = self.Session()

        dimensions = Dimensions(motorcycle_id=motorcycle_id, **data)
        session.add(dimensions)
        session.commit()
        session.close()
        return dimensions
    
    def get_dimensions(self, motorcycle_id):
        session = self.Session()

        dimensions = session.query(Dimensions).filter(Dimensions.motorcycle_id == motorcycle_id).first()
        session.close()
        return dimensions
    
    def update_dimensions(self, motorcycle_id, data):
        session = self.Session()

        dimensions = session.query(Dimensions).filter(Dimensions.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(dimensions, key, value)
        session.commit()
        session.close()
        return dimensions
    
    def delete_dimensions(self, motorcycle_id):
        session = self.Session()

        dimensions = session.query(Dimensions).filter(Dimensions.motorcycle_id == motorcycle_id).first()
        session.delete(dimensions)
        session.commit()
        session.close()
        return dimensions
    
    def create_brakes(self, motorcycle_id, data):
        session = self.Session()

        brakes = Brakes(motorcycle_id=motorcycle_id, **data)
        session.add(brakes)
        session.commit()
        session.close()
        return brakes
    
    def get_brakes(self, motorcycle_id):
        session = self.Session()

        brakes = session.query(Brakes).filter(Brakes.motorcycle_id == motorcycle_id).first()
        session.close()
        return brakes
    
    def update_brakes(self, motorcycle_id, data):
        session = self.Session()

        brakes = session.query(Brakes).filter(Brakes.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(brakes, key, value)
        session.commit()
        session.close()
        return brakes

    def delete_brakes(self, motorcycle_id):
        session = self.Session()

        brakes = session.query(Brakes).filter(Brakes.motorcycle_id == motorcycle_id).first()
        session.delete(brakes)
        session.commit()
        session.close()
        return brakes
    
    def create_engine(self, motorcycle_id, data):
        session = self.Session()

        engine = Engine(motorcycle_id=motorcycle_id, **data)
        session.add(engine)
        session.commit()
        session.close()
        return engine
    
    def get_engine(self, motorcycle_id):
        session = self.Session()

        engine = session.query(Engine).filter(Engine.motorcycle_id == motorcycle_id).first()
        session.close()
        return engine
    
    def update_engine(self, motorcycle_id, data):
        session = self.Session()

        engine = session.query(Engine).filter(Engine.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(engine, key, value)
        session.commit()
        session.close()
        return engine

    def delete_engine(self, motorcycle_id):
        session = self.Session()

        engine = session.query(Engine).filter(Engine.motorcycle_id == motorcycle_id).first()
        session.delete(engine)
        session.commit()
        session.close()
        return engine
    
    def create_suspension(self, motorcycle_id, data):
        session = self.Session()

        suspension = Suspension(motorcycle_id=motorcycle_id, **data)
        session.add(suspension)
        session.commit()
        session.close()
        return suspension
    
    def get_suspension(self, motorcycle_id):
        session = self.Session()

        suspension = session.query(Suspension).filter(Suspension.motorcycle_id == motorcycle_id).first()
        session.close()
        return suspension
        
    def update_suspension(self, motorcycle_id, data):
        session = self.Session()

        suspension = session.query(Suspension).filter(Suspension.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(suspension, key, value)
        session.commit()
        session.close()
        return suspension

    def delete_suspension(self, motorcycle_id):
        session = self.Session()

        suspension = session.query(Suspension).filter(Suspension.motorcycle_id == motorcycle_id).first()
        session.delete(suspension)
        session.commit()
        session.close()
        return suspension
    
    def create_tires(self, motorcycle_id, data):
        session = self.Session()

        tires = Tires(motorcycle_id=motorcycle_id, **data)
        session.add(tires)
        session.commit()
        session.close()
        return tires
    
    def get_tires(self, motorcycle_id):
        session = self.Session()

        tires = session.query(Tires).filter(Tires.motorcycle_id == motorcycle_id).first()
        session.close()
        return tires
    
    def update_tires(self, motorcycle_id, data):
        session = self.Session()

        tires = session.query(Tires).filter(Tires.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(tires, key, value)
        session.commit()
        session.close()
        return tires
    
    def delete_tires(self, motorcycle_id):
        session = self.Session()

        tires = session.query(Tires).filter(Tires.motorcycle_id == motorcycle_id).first()
        session.delete(tires)
        session.commit()
        session.close()
        return tires

    def create_miscellaneous(self, motorcycle_id, data):
        session = self.Session()

        miscellaneous = Miscellaneous(motorcycle_id=motorcycle_id, **data)
        session.add(miscellaneous)
        session.commit()
        session.close()
        return miscellaneous
    
    def get_miscellaneous(self, motorcycle_id):
        session = self.Session()

        miscellaneous = session.query(Miscellaneous).filter(Miscellaneous.motorcycle_id == motorcycle_id).first()
        session.close()
        return miscellaneous

    def update_miscellaneous(self, motorcycle_id, data):
        session = self.Session()

        miscellaneous = session.query(Miscellaneous).filter(Miscellaneous.motorcycle_id == motorcycle_id).first()
        for key, value in data.items():
            setattr(miscellaneous, key, value)
        session.commit()
        session.close()
        return miscellaneous
    
    def delete_miscellaneous(self, motorcycle_id):
        session = self.Session()

        miscellaneous = session.query(Miscellaneous).filter(Miscellaneous.motorcycle_id == motorcycle_id).first()
        session.delete(miscellaneous)
        session.commit()
        session.close()
        return miscellaneous
    
