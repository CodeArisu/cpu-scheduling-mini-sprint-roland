class ProcessSim:
    
    def __init__(self, pid, arrv_time, burst_time, comp_time):
        """
        Initialize a Process Simulation instance.
        
        :param pid: Process ID
        :param arrv_time: Arrival Time of the process
        :param burst_time: Burst Time of the process
        :param comp_time: Completion Time of the process
        """
        self.pid = pid  # Process ID
        self.arrv_time = arrv_time    # Arrival Time
        self.burst_time = burst_time  # Burst Time
        self.comp_time = comp_time    # Completion Time

    def __repr__(self):
        return f"Process(pid={self.pid}, arrv_time={self.arrv_time}, burst_time={self.burst_time}, comp_time={self.comp_time})"


    def get(self):
        return self.pid, self.arrv_time, self.burst_time, self.comp_time

    
    