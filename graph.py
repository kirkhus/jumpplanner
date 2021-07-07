"""Generic map graph to overlay."""


import os
import json


def _load_starmap(file_):
    """Load the starmap from static data."""

    static = os.environ.get("STATIC_DATA", os.path.realpath(
        os.path.dirname(__file__)))

    jump_map = os.path.join(static, file_)

    if not os.path.isfile(jump_map):
        raise RuntimeError("missing data: {}".format(jump_map))

    with open(jump_map, "r") as open_jump_map:
        # JSON doesn't allow int keys
        return {int(k): v for k, v in json.load(open_jump_map).items()}


class Graph:
    """Created once during app init, this is the default universe."""

    _timestamp = None
    _starmap = None

    def __init__(self, file_):
        """Hold reference to the default starmap."""

        self._starmap = _load_starmap(file_)
        
    def neighbors(self, system):
        """Return a list of neighbors for a given system."""
        return self.get_system(system)['neighbors']

    def security(self, system):
        """Return the security level for a given system."""
        return self.get_system(system)['security']

    def get_system(self, system):
        """Return a dict with both neighbors and security for a system."""
        return self._starmap.get(system)

    def get_system_id(self, name):
        return [id for id, items in self._starmap.items() if items['name'].lower()== name.lower()][0]

    def name(self, system):
        return self.get_system(system)['name']

    def is_wormhole(self, system_id, neighbor):
        if not neighbor:
            return False

        system = self.get_system(system_id)
        if not "wormholes" in system:
            return False

        return neighbor in system["wormholes"]                                   

    def is_highsec(self, system_id):
        security = self.security(system_id)
        return security >= 0.5
    
    def names(self):
        return [item['name'] for id, item in self._starmap.items()]
