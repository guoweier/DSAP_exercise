# Class Flower

class Flower:
  """A custom flower classification"""

  def __init__(self, name="Rose", petal=5, price=10):
    """Creat a new flower
    name: flower name
    petal: the number of petals of the flower
    price: flower price
    """
    self._name = name
    self._petal = petal
    self._price = price

  def get_name(self):
    """Return the flower name"""
    return self._name
  def get_petal(self):
    """Return petal number"""
    return self._petal
  def get_price(self):
    """Return flower price"""
    return self._price

if __name__ in "__main__":
  lily = Flower("Lily",6,7)
  print('Flower Name =', lily.get_name())
  print('Flower Petal =', lily.get_petal())
  print('Flower Price =', lily.get_price())