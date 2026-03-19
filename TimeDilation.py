import math

c = 299792458  # Speed of light in m/s

miles_to_meters = 1609.344
hours_to_seconds = 3600
time = int(input("How many hours did you travel?"))*hours_to_seconds 
+ int(input("How many minutes did you travel?"))*60
distance = int(input("How many miles did you travel?"))*miles_to_meters
meters_per_second = distance / time
v = meters_per_second
t = time

lorentz_factor = 1 / math.sqrt(1-((v**2)/(c**2)))
time_travel = (t * lorentz_factor) - t
print("You have traveled " + f"{time_travel:.20f}" + " seconds into the future.")