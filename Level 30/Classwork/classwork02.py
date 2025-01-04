def number(bus_stops):
    people_in_the_bus = 0
    for stop in bus_stops:
        people_in_the_bus += stop[0]
        people_in_the_bus -= stop[1] 
    return people_in_the_bus