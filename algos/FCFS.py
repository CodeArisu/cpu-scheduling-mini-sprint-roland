from .Process import ProcessSim
from queue import Queue

"""
First-Come, First-Served (FCFS) Scheduling Algorithm Implementation
"""
class FCFS(ProcessSim):
    
    def __init__(self, pid, arrv_time, burst_time, start, comp_time, wait_time=0, turn_around_time=0, response_time=0):
        """
        Initialize a FCFS Scheduling instance of a Process Sim child.
        
        :param pid: Process ID
        :param arrv_time: Arrival Time of the process
        :param burst_time: Burst Time of the process
        :param wait_time: Waiting Time of the process
        :param turn_around_time: Turn Around Time of the process
        :param response_time: Response Time of the process
        """
        super().__init__(pid, arrv_time, burst_time, comp_time)
        self.wait_time = wait_time
        self.turn_around_time = turn_around_time
        self.response_time = response_time
        self.start = start
        
        
    def __repr__(self):
        return (f"FCFS(pid={self.pid}, arrv_time={self.arrv_time}, burst_time={self.burst_time}, start_time={self.start}, comp_time={self.comp_time}, "
                f"wait_time={self.wait_time}, turn_around_time={self.turn_around_time}, response_time={self.response_time})")
        
        
    def get_current_params(self):
        return (self.start, self.wait_time, self.turn_around_time, self.response_time)


    def get(self):
        return super().get() + self.get_current_params()
        # pid, arrv_time, burst_time, comp_time, start, wait_time, turn_around_time, response_time
        

    def get_turn_around(self):
        return self.turn_around_time
    
    
    def get_wait(self):
        return self.wait_time
    
    
    def get_response(self):
        return self.response_time

