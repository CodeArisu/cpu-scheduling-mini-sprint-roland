
# CPU Scheduling Algorithm Simulation

A coding sprint for simulating CPU Time Scheduling Algorithms such as First Come First Serve (FCFS) Algorithm and Round Robin (RR) Algorithm. This repository visualized how different CPU Scheduling computes time schedules for each processes as inputs. Though
it can only print tables for each algorithms calculated scheduled reports.

## How to Run
* Using IDE (VSCode) run main.py
* Using terminal run:
<br/>

activate python Virtual Environment:
```bash
source .venv/bin/activate
```
run the source code:
```bash
python main.py
```
## Sample Outputs

Example data provided:

| PID | Arrival Time | Burst Time |
|:---:|:------------:|:----------:|
|P1   | 0            |7           |
|P2   | 2            |4           |
|P3   | 4            |1           |
|P4   | 5            |4           |
|P5   | 6            |3           | 

```python
Scheduling Results: FIRST COME FIRST SERVE
╒═════════╤════════════════╤══════════════╤═══════════════════╤═════════╤════════════════╤════════════════════╤═════════════════╕
│   PID   │  Arrival Time  │  Burst Time  │  Completion Time  │  Start  │  Waiting Time  │  Turn Around Time  │  Response Time  │
╞═════════╪════════════════╪══════════════╪═══════════════════╪═════════╪════════════════╪════════════════════╪═════════════════╡
│   P1    │       0        │      7       │         7         │    0    │       0        │         7          │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P2    │       2        │      4       │        11         │    7    │       5        │         9          │        5        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P3    │       4        │      1       │        12         │   11    │       7        │         8          │        7        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P4    │       5        │      4       │        16         │   12    │       7        │         11         │        7        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│   P5    │       6        │      3       │        19         │   16    │       10       │         13         │       10        │
├─────────┼────────────────┼──────────────┼───────────────────┼─────────┼────────────────┼────────────────────┼─────────────────┤
│ Average │                │              │                   │         │      5.8       │        9.6         │       5.8       │
╘═════════╧════════════════╧══════════════╧═══════════════════╧═════════╧════════════════╧════════════════════╧═════════════════╛
```

```python
Scheduling Results: ROUND ROBIN, Quantum = 2
╒═════════╤════════════════╤══════════════╤═══════════════════╤═══════════╤════════════════════╤════════════════╤═════════════════╕
│   PID   │  Arrival Time  │  Burst Time  │  Completion Time  │  Quantum  │  Turn Around Time  │  Waiting Time  │  Response Time  │
╞═════════╪════════════════╪══════════════╪═══════════════════╪═══════════╪════════════════════╪════════════════╪═════════════════╡
│   P1    │       0        │      7       │        19         │     2     │         19         │       12       │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼───────────┼────────────────────┼────────────────┼─────────────────┤
│   P2    │       2        │      4       │         9         │     2     │         7          │       3        │        0        │
├─────────┼────────────────┼──────────────┼───────────────────┼───────────┼────────────────────┼────────────────┼─────────────────┤
│   P3    │       4        │      1       │         7         │     2     │         3          │       2        │        2        │
├─────────┼────────────────┼──────────────┼───────────────────┼───────────┼────────────────────┼────────────────┼─────────────────┤
│   P4    │       5        │      4       │        17         │     2     │         12         │       8        │        4        │
├─────────┼────────────────┼──────────────┼───────────────────┼───────────┼────────────────────┼────────────────┼─────────────────┤
│   P5    │       6        │      3       │        18         │     2     │         12         │       9        │        5        │
├─────────┼────────────────┼──────────────┼───────────────────┼───────────┼────────────────────┼────────────────┼─────────────────┤
│ Average │                │              │                   │           │        10.6        │      6.8       │       2.2       │
╘═════════╧════════════════╧══════════════╧═══════════════════╧═══════════╧════════════════════╧════════════════╧═════════════════╛
```

## How it works

Given the predefined inputs the program automatically computes "Completion Time"-- time taken by the process to complete.

### For FSFC:
```
completion_time = previous_process_burst_time + next_process_burst_time 
```

### For RR:
```
if remaining_burst <= quantum
    completion_time = current_time + remaining_burst

else
    # subtracts until it is less than the input quantum
    remaining_burst = remaining_burst - quantum
    current_time = current_time + quantum
    then returns to the queue
```

After getting the completion time, calculate the "Start".
```
# compares values using maximum
start = max(prev_time, arrive_time)
```

Using the computations above:

```
finish = completion_time

turn_around = finish - arrive_time
waiting = turn_around - burst_time
response = start - arrive_time
```

## Notes:

This program only shows a direct table results using the predefined dataset

### For enhancements:
* Detailed visualization of the patterns and processes for in depth understanding. 
* Custom inputs for better analyzation.
* More available option for algorithms.
* Optimization for maximum accuracy of the proccesses time scheduling calculations.