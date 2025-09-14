
# CPU Scheduling Algorithm Simulation

A small coding project for simulating CPU Scheduling Algorithms such as First Come First Serve (FCFS) Algorithm and Round Robin (RR) Algorithm. This repository shows how different CPU Scheduling computes time schedules for each processes as inputs.

## How to Run
* Using IDE (VSCode) run main.py
* Using terminal run:
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
