import math
import os
import sys

from api import Api
from graph import Graph

import dijkstra

class Utility:
    
    THERA = 31000005

    _universe_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "universe.json")
    _stats = {}
    
    def __init__(self):
        self._api = Api()
        self._graph = Graph(self._universe_file)        
        
    def get_route(self, start, end):
        route = dijkstra.dijkstra(self._graph, start, end)
        
        return self.get_jump_types(route)

    def get_graph(self):
        return self._graph

    def get_jump_types(self, route):
        return_route = []
        for i, system in enumerate(route):
            
            name = self.get_system_name(system)
            type_ = ""
            neighbor = lambda i, route: route[i+1] if i < len(route) - 1 else None

            if name == "Thera" or self._graph.is_wormhole(int(system), neighbor(i, route)):
                type_ = "Wormhole"

            return_route.append({'name': name, 'type': type_})

        return return_route
    
    def get_system_id(self, name):
        try:
            return self._graph.get_system_id(name)
        except:
            pass
        print("Invalid name: ", name)
        return None
        
    def get_system_name(self, id):
        try:
            return self._graph.name(id)
        except:
            pass

        print("Invalid ID: ", id)
        return None

    def get_system_details(self, id):
        """Get details for a single system."""

        system_details = self._api.op("get_universe_systems_system_id", **{'system_id': id})
        
        this_system = {
            "id": id,
            "neighbors": [],
            "security": system_details["security_status"],
            "name": system_details["name"],
            "region": self.get_region_name(id),
            "position": system_details["position"] 
            }

        for gate in system_details.get("stargates", []):
            gate_details = self._api.op('get_universe_stargates_stargate_id', **{'stargate_id':gate})

            this_system["neighbors"].append(
                gate_details["destination"]["system_id"]
                )

        return this_system


    def get_region_name(self, system_id):
        system_details = self._api.op("get_universe_systems_system_id", **{'system_id': system_id})
        constellation_id = system_details['constellation_id']
        constellation_details = self._api.op("get_universe_constellations_constellation_id", **{"constellation_id": constellation_id})
        
        region_id = constellation_details['region_id']       
        region_details = self._api.op("get_universe_regions_region_id", **{"region_id": region_id})

        return region_details['name']

    def get_all_systems(self):
        return self._api.op('get_universe_systems')

    def get_all_systems_startswith(self, text):
        return [system for system in self._graph.names() if system.lower().startswith(text.lower())]
        
    def get_statistics(self):
        return self._stats

    def get_neighbours(self, system_id):
        return self._graph.get_system(system_id)["neighbors"]
    
    def get_best_entry_system(self, from_id, to_id, avoid=[]):
        route = self._api.op('get_route_origin_destination', **{'origin': from_id, 'destination': to_id, 'flag': 'insecure', 'avoid': avoid})
        route.reverse()
        
        return self._get_first_jumpable_system(route)

    def _get_first_jumpable_system(self, route):

        for r in route:
            if not self._graph.is_highsec(r):
                return r

    def get_ly_distance(self, from_id, to_id):
        from_ = self._graph.get_system(from_id)
        to = self._graph.get_system(to_id)

        x1 = from_["position"]["x"]
        y1 = from_["position"]["y"]
        z1 = from_["position"]["z"]

        x2 = to["position"]["x"]
        y2 = to["position"]["y"]
        z2 = to["position"]["z"]

        distance = (math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2))/9.4605284e1)/100000000000000
        
        return round(distance, 3)
        

    def get_jump_route(self, from_id, to_id):

        max_range = 10
        route = []
        distance = sys.maxsize
        
        from_ = self._graph.get_system(from_id)
        to = self._graph.get_system(to_id)

        print("From: ", from_)

        while distance > max_range:
            #distance = self.get_ly_distance(from_
            pass

        """
        calculateRoute: function(start, destination, maxRange) {
            if (! start || ! destination || destination.security >= 0.5) {
                return [];
            }

            var route = [];
            var sysA = start;
            var sysB = destination;
            var distance = Number.MAX_SAFE_INTEGER;

            while (distance > maxRange) {
                distance = calculateDistance(sysA, sysB);

                if (distance <= maxRange) {
                    route.push({
                        from: { name: sysA.name, security: sysA.security },
                        to: { name: sysB.name, security: sysB.security },
                        distance: distance
                    });
                    sysA = sysB;
                    if (sysB !== destination) {
                        sysB = destination;
                        distance = Number.MAX_SAFE_INTEGER;
                    }
                } else {
                    sysB = findCloserSystem(sysA, sysB, maxRange);
                    if (sysB === null) {
                        return [];
                    }
                }
            }
            """

        return route;
