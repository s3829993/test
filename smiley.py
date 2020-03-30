class Smiley:
  def __init__(self, pattern):
    self.pattern = pattern
    #self.colour = colour
    
  def setPattern(self, pattern):
    self.pattern = pattern

  def setColour(self, new_colour):
    B = [0, 0, 0]
    for n, i in enumerate(self.pattern):
      if i != B:
        self.pattern[n] = new_colour  