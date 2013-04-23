# File:          swarm_controller.py
# Date:          23.04.2013
# Author:        Andreas,Odd

import epuck_basic as epb
from search import Search
from retrieval import Retrieval
from stagnation import Stagnation

class swarm_controller (epb.EpuckBasic):
  def __init__(self):
    super(swarm_controller, self).__init__()
    self.basic_setup()
  # User defined function for initializing and running
  # the swarm_controller class
  def run(self):
    
       
    # Main loop
    while True:
      # Perform a simulation step of 64 milliseconds
      # and leave the loop when the simulation is over
      if self.step(64) == -1:
        break
      
      self.forward()
      # Read the sensors:
           
      # Process sensor data here.

      output1 = Retrieval.determine_action(True)
      Search.determine_action(True)
      Stagnation.determine_action(True)
      
      # Enter here functions to send actuator commands, like:
      print output1

controller = swarm_controller()
controller.run()
