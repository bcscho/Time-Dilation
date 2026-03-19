import math

c = 299792458  # speed of light (m/s)

miles_to_meters = 1609.344
hours_to_seconds = 3600

hours = float(input("How many hours did you travel?"))
minutes = float(input("How many minutes did you travel?"))
miles = float(input("How many miles did you travel?"))

travel_time = hours * hours_to_seconds + minutes * 60
distance = miles * miles_to_meters

v = distance / travel_time

if v >= c:
    print("Error: velocity must be less than the speed of light.")
    exit()

lorentz_factor = 1 / math.sqrt(1 - (v**2 / c**2))
time_dilation = travel_time - (travel_time / lorentz_factor)

print()
print(f"Average speed: {v:.3f} m/s")
print(f"Time dilation: {time_dilation:.20f} seconds")
print()
print(
    f"Relative to a stationary observer, you have advanced "
    f"{time_dilation:.20f} seconds into the future.")
