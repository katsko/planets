from operator import itemgetter
import apium
from apium import af
from storage.data import PLANETS


class GetPlanet(apium.Method):
    name = af.Str(required=True)

    def validate_name(self, value):
        try:
            planet = PLANETS[self.name]
        except KeyError:
            raise ValueError('Planet not found')
        self.method_cache['planet'] = planet

    def execute(self):
        planet = self.method_cache['planet']
        return {
            'planet': {
                'name': self.name,
                'distance': planet['distance'],
                'planet_type': planet['planet_type'],
            }
        }
