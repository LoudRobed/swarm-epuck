
class Search():
    # Determines the course of action based on the sensory input.
    # Returns a boolean value as its first return value which says
    # if the layer should have precedence. temporary solution.
    THRESHOLD = 1000
    def determine_action(self, proximities):

        thresh_list = self.calculate_threshold_list(proximities, self.THRESHOLD)
        wheel_speeds = self.calculate_wheel_speed(thresh_list)
        return True,wheel_speeds

    # Calculates an array of boolean values that says if the input
    # of that sensor is above a threshold.
    def calculate_threshold_list(self,proximities,threshold):
        t_list = []
        for x in proximities:
            if x > threshold:
                t_list.append(True)
            else:
                t_list.append(False)
        return t_list

    def calculate_wheel_speed(self, thresh_list):
    #TODO: Do some real calculation based on the thresh_list
        speeds = []
        speeds.append(1.0)
        speeds.append(1.0)

        return speeds

SearchObject = Search()
args = SearchObject.determine_action([1,1,1,1,0])
if(args[0]):
   speeds = args[1]
   print speeds[0]
   print speeds[1]

