class switchObject():
 def __init__(self, channel):
  import machine
  self.pin = machine.Pin(channel, machine.Pin.OUT)
  self.state = "1"
  self.switch()
 def switch(self):
  if bool(int(self.state)):
   print("Turning OFF")
   self.pin.on()
   self.state = "0"
   return self.state
  else:
   print("Turning ON")
   self.pin.off()
   self.state = "1"
   return self.state
