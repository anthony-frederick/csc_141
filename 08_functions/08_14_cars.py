# Shows some info about a random car

def make_car(manufacturer, model_name, **car_attributes):
    """Dictionary that gives us things relating to a car"""
    car_attributes [manufacturer]= manufacturer
    car_attributes [model_name]= model_name
    return car_attributes
car_attributes = make_car('Daimler AG', 'Mercedes Benz', color = 'red', year= '2025')
print(car_attributes)