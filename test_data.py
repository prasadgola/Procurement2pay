# Cars and Parts Dataset
# Format: [Car Name, Transmission, Brakes, Electrical, Engine, Suspension, Exhaust, Cooling, Battery, Alternator, Radiator, Wheels, Tires, Steering, Oil Filter, Air Filter, Fuel Pump, Spark Plugs, Headlights, Windshield]

data = [
    ['Car 1', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 2', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 3', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 4', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 5', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 6', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 7', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 8', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 9', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'],
    
    ['Car 10', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield']
]


import pandas as pd

df = pd.DataFrame(data, columns=['Car', 'Transmission', 'Brakes', 'Electrical', 'Engine', 'Suspension', 'Exhaust', 'Cooling', 'Battery', 'Alternator', 'Radiator', 'Wheels', 'Tires', 'Steering', 'Oil Filter', 'Air Filter', 'Fuel Pump', 'Spark Plugs', 'Headlights', 'Windshield'])

print(df)