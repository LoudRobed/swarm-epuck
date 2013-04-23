import random
class Search():
    # Determines the course of action based on the sensory input.
    # Returns a boolean value as its first return value which says
    # if the layer should have precedence. temporary solution.
    THRESHOLD = 500
    COUNTER = 0
    def determine_action(self, proximities):

        thresh_list = self.calculate_threshold_list(proximities, self.THRESHOLD)
        wheel_speeds = self.calculate_wheel_speed(thresh_list)
        return True,wheel_speeds

    # Calculates an array of boolean values that says if the input
    # of that sensor is below a threshold.
    def calculate_threshold_list(self,proximities,threshold):
        t_list = []
        for x in proximities:
            if x < threshold:
                t_list.append(True)
            else:
                t_list.append(False)
        return t_list

    def calculate_wheel_speed(self, ps):

        #TODO: Do something useful witht the sensoroutput.
        left = False
        right = False

        randorama = random.randint(0,2)

        if(randorama == 0):
            left = True
        if(randorama == 1):
            right = True
            
##        self.COUNTER = self.COUNTER+1
##        if(self.COUNTER >20):
##            self.COUNTER = 0
##            left = True    

        speeds = []

        
        
        if(left):
            speeds.append(0.5)
            speeds.append(1.0)
        else:
            speeds.append(1.0)
            speeds.append(1.0)

        if(right):
            speeds.append(1.0)
            speeds.append(0.5)
        else:
            speeds.append(1.0)
            speeds.append(1.0)

        return speeds

##SearchObject = Search()
##args = SearchObject.determine_action([1,1,1,1,0])
##if(args[0]):
##   speeds = args[1]
##   print speeds[0]
##   print speeds[1]
print random.randint(0,1)

