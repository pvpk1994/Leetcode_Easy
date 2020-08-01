class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Keys: messages and values: Counters
        self.dict_active_list = {}
        
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # If message in dictionary of active messages
        if message in self.dict_active_list.keys():
            if self.dict_active_list[message] > timestamp:
                return False
            elif self.dict_active_list[message] <= timestamp:
                # time to reset the message
                self.dict_active_list[message]= timestamp+10
                return True
        
        # If message not in dictionary 
        else:
            # self.dict_active_list.add(message, timestamp)
            self.dict_active_list[message] = timestamp +10
            return True
            
       
