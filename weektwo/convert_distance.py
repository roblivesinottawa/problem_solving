def convert_distance(miles):
    km = miles * 1.6
    return km

my_trip = 55

my_trip_in_km = convert_distance(my_trip)
print(f"the distance is kilometers is {str(my_trip_in_km)}")
# calculate the round trip
print(f"the round-trip in kilometers is {str(2.0 * my_trip_in_km)}")
