"""
Flight leg:
GLA -> ATL -> TOR

2 segments (GLA -> ATL, ATL -> TOR)
"""
from typing import List

class Segment:
  def __init__(self, departure, destination):
    self.departure = departure
    self.destination = destination

class Flight:
  def __init__(self, segments: List[Segment]):
    self.segments = segments
    
  def __repr__(self):
    stops = [self.segments[0].departure, self.segments[0].destination]
    for segment in self.segments[1:]:
      stops.append(segment.destination)
    return ' -> '.join(stops)

  @property
  def departure_point(self):
    return self.segments[0].departure
  
  @departure_point.setter
  def departure_point(self, val):
    dest = self.segments[0].departure
    self.segments[0] = Segment(departure= val, destination=dest)


flight = Flight([Segment('GLA', 'ATL')])
print(flight.departure_point)
print(flight)

flight.departure_point = 'EDI'
print(flight.departure_point)
print(flight)