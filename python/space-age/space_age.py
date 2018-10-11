conversion_rates = {
        'earth': 1.0,
        'mercury': .2408467,
        'venus': .61519726,
        'mars': 1.88087158,
        'jupiter': 11.862615,
        'saturn': 29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
      }

class SpaceAge(object):

  def convert_time(self, planet):
    def convert():
      year = self.seconds/conversion_rates[planet]/self.earth_year_seconds
      return round(year,2)
    return convert

  def __init__(self, seconds):
    self.seconds = seconds
    self.earth_year_seconds = 31557600
    for planet in conversion_rates:
      setattr(self,'on_'+planet, self.convert_time(planet))
