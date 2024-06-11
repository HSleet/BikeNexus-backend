from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, inspect
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    __abstract__ = True  # Mark the class as abstract
    def to_dict(self):
        # Serialize columns
        dict_repr = {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
        
        # Serialize relationships
        for name, relation in inspect(self).mapper.relationships.items():
            value = getattr(self, name)
            if value is None:
                dict_repr[name] = None
            elif relation.uselist:  # Handle lists for one-to-many relationships
                dict_repr[name] = [item.to_dict() for item in value]
            else:  # Handle single items for one-to-one relationships
                dict_repr[name] = value.to_dict()
        return dict_repr


class Motorcycle(Base):
    __tablename__ = 'motorcycles'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    profile = Column(Text, nullable=True)
    category = Column(String, nullable=True)
    engine_type = Column(String, nullable=True)
    engine_details = Column(Text, nullable=True)
    
    performance = relationship("Performance", back_populates="motorcycle", uselist=False)
    dimensions = relationship("Dimensions", back_populates="motorcycle", uselist=False)
    brakes = relationship("Brakes", back_populates="motorcycle", uselist=False)
    engine = relationship("Engine", back_populates="motorcycle", uselist=False)
    suspension = relationship("Suspension", back_populates="motorcycle", uselist=False)
    tires = relationship("Tires", back_populates="motorcycle", uselist=False)
    miscellaneous = relationship("Miscellaneous", back_populates="motorcycle", uselist=False)


class Performance(Base):
    __tablename__ = 'performance'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    power = Column(String, nullable=True)
    top_speed = Column(String, nullable=True)
    power_weight_ratio = Column(String, nullable=True)
    
    motorcycle = relationship("Motorcycle", back_populates="performance")


class Dimensions(Base):
    __tablename__ = 'dimensions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    dry_weight = Column(String, nullable=True)
    overall_height = Column(String, nullable=True)
    overall_length = Column(String, nullable=True)
    overall_width = Column(String, nullable=True)
    seat_height = Column(String, nullable=True)
    wheelbase = Column(String, nullable=True)
    ground_clearance = Column(String, nullable=True)
    
    motorcycle = relationship("Motorcycle", back_populates="dimensions")


class Brakes(Base):
    __tablename__ = 'brakes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    front_brakes = Column(String, nullable=True)
    rear_brakes = Column(String, nullable=True)
    
    motorcycle = relationship("Motorcycle", back_populates="brakes")


class Engine(Base):
    __tablename__ = 'engine'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    displacement = Column(String, nullable=True)
    torque = Column(String, nullable=True)
    bore_x_stroke = Column(String, nullable=True)
    compression = Column(String, nullable=True)
    fuel_system = Column(String, nullable=True)
    fuel_control = Column(String, nullable=True)
    ignition = Column(String, nullable=True)

    motorcycle = relationship("Motorcycle", back_populates="engine")


class Suspension(Base):
    __tablename__ = 'suspension'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    front_suspension = Column(String, nullable=True)
    rear_suspension = Column(String, nullable=True)
    front_wheel_travel = Column(String, nullable=True)
    rear_wheel_travel = Column(String, nullable=True)
    
    motorcycle = relationship("Motorcycle", back_populates="suspension")

class Tires(Base):
    __tablename__ = 'tires'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    front_tire = Column(String, nullable=True)
    rear_tire = Column(String, nullable=True)
    
    motorcycle = relationship("Motorcycle", back_populates="tires")

class Miscellaneous(Base):
    __tablename__ = 'miscellaneous'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    motorcycle_id = Column(Integer, ForeignKey('motorcycles.id'))
    gearbox = Column(String, nullable=True)
    color_options = Column(String, nullable=True)
    starter = Column(String, nullable=True)
    clutch = Column(String, nullable=True)
    instruments = Column(String, nullable=True)
    rake_fork_angle = Column(String, nullable=True)
    
    motorcycle = relationship("Motorcycle", back_populates="miscellaneous")
