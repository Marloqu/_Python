from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time(hours = 51))

def variable_length(*args):
    print(args)

variable_length()

variable_length("one", "two")

variable_length(None)

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(28, 32, 54, 67))

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)
{'tanks': 1, 'day': 'Wednesday', 'pilots': 3}

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for xtitle, name in kwargs.items():
        print(f"{xtitle}: {name}")
    print(type(kwargs))

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

type(crew_members)

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}: {value}")

fuel_report(main = 50, external = 100, emergency = 60)

    
    


