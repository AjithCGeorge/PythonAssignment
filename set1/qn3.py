        # Qn-3

class String:
  def __init__(self):
    pass
    self.inpString()

  def inpString(self):
    self.stRing=input('enter the string to be turned to uppercase :')
    self.upperString()
  def  upperString(self):
      self.stRing=self.stRing.upper()
      print(self.stRing)

s=String()