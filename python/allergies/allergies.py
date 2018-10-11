import math

class Allergies(object):

    def __init__(self, score):
      allergens = {
        1: "eggs",
        2: "peanuts",
        4: "shellfish",
        8: "strawberries",
        16: "tomatoes",
        32: "chocolate",
        64: "pollen",
        128: "cats"
      }

      self._lst= []
      for key in allergens:
        if key & score:
          self._lst.append(allergens[key])

    def is_allergic_to(self, item):
      return item in self._lst

    @property
    def lst(self):
      return self._lst
