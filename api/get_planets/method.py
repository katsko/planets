from operator import itemgetter
import apium
from apium import af
from storage.data import PLANETS


class GetPlanets(apium.Method):
    distance = af.Int()
    order = af.Str(default='distance')

    def validate_order(self, value):
        if value not in ['distance', 'name']:
            raise ValueError('Value must be "distance" or "name"')

    def execute(self):
        data = [
            {
                'name': name,
                'distance': properties['distance'],
            }
            for name, properties in PLANETS.items()
        ]
        data = sorted(data, key=itemgetter(self.order))
        if distance := self.distance:
            data = [item for item in data if item['distance'] >= distance]
        return {'planets': data}
