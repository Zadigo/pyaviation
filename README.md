# Py Aviation

The "aviation" project regroups a set of formulas and general principles for aviation for Python.


# Getting started

To start using the module, you can start by creating a aircraft model from one of the base aircraft manufacturers.

```
from pyaviation.aircraft import Cessna

airplane = Cessna()
```

This creates a blank airplane model on which you can call a variety of functions.

Python aviation comes however with a set of built in aircraft models that you can use.

```
from pyaviation.models  import A320

aircraft = A320()
```

## The flight mixin and basic calculations

The flight mixin regroups all the main definitions for calculating items related to flight.

Provided you've constructed an airplane like above, you can do the following.

### Calculating basic speed

```
airplane.calculate_speed(50, 2)

>> 
```

### Calculting distance

```
airplane.calculate_distance( , )

>> 
```

### Calculate duration

```
airplane.calculate_duration( , )

>> 
```

### Calculate arrival time

```
airplane.calculate_arrival_time( , )

>> 
```

### Calculate ground speed

```
airplane.ground_speed( , )

>> 
```

### True air speed

```
airplane.true_air_speed( , )

>> 
```

### Calculate density altitute

```
airplane.density_altitude( , )

>> 
```

### Calculate fuel

Calculates the fuel consumed during a flight of x hours and minutes and eventually the remaining minutes left to fly with the fuel left.

```
airplane.fuel( , )

>> 
```

### Calculate consumption rate

```
airplane.fuel_consumption_rate( , )

>>
```


### Calculate ground gradient

```
airplane.ground_gradient( , )

>>
```

### Calculate obstacle clearance

```
airplane.calculate_obstacle_clearance( , )

>>
```


### Calculate distance to horizon

```
airplane.distance_to_horizon( , )

>>
```

### Calculate Needed fuel

```
airplane.needed_fuel( , )

>>
```

## Specific aircraft calculations

Considering that each new class you create using the `BaseAircraft` class (exactly like we did in the above examples), each newly created class will provide additional definitions that will take into consideration the specific characteristics of each aircraft.

### Safety factor

```
airplane.safety_factor( , )

>>
```

### Net performance

```
airplane.net_performance( , )

>>
```

### Gross performance

```
airplane.gross_performance( , )

>>
```

### Gradient of climb

```
airplane.gradient_of_climb( , )

>>
```

### Ground gradient

```
airplane.ground_gradient( , )

>>
```

### Maximum payload

```
airplane.maximum_payload( , )

>>
```

## Creating a new aircraft model

Creating a new model is very simple. Just subclass the `Airplane` class in order to create a new manufacturer for example.

```
from pyaviation.aircraft import Aircraft

class CustomManufacturer(Aircraft):
    manufacturer = "Custom"

class MyAircraft(CustomManufacturer):
    version = "eco-xxx"
    speed = {
        "cruise": 456,
        "max": 567
    }
    max_rang = 5678
    weight = {
        "taxi": 73900,
        "takeoff": 73500,
        "landing": 64500
    }
    fuel = {
        "max": 23859
    }
    passengers = 150
    ceiling = {
        "range": [39100, 41000]
    }

aircraft = MyAircraft()
```
