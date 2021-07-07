"""This can recreate the jumpmap.json should the universe ever change."""


import time
import json

import utility

u = utility.Utility()

all_systems = u.get_all_systems()

num_systems = len(all_systems)
complete = 0
systems = {}
print("Fount %s systems" % num_systems)
for id in all_systems:
    system = u.get_system_details(id) 

    systems[id] = system
    complete += 1
    print("{}/{} systems complete".format(complete, num_systems))

with open("universe.json", "w") as openjumpmap:
    openjumpmap.write(json.dumps(systems, indent=4, sort_keys=True))

print("updated universemap.json")


