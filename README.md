# Smart Factory Simulator

A Python-based manufacturing equipment simulator designed to model machine operations, production metrics, alarms, and factory analytics.

The long-term goal of this project is to evolve into a lightweight digital twin platform capable of simulating manufacturing equipment, collecting production data, visualizing KPIs, and eventually supporting industrial communication protocols such as SECS/GEM.

---

## Project Goals

This project is intended to demonstrate:

- Object-Oriented Design
- Manufacturing Systems Engineering
- Production Analytics
- OEE (Overall Equipment Effectiveness)
- Event-Driven Architecture
- Industrial Software Development
- Dashboard Development
- Industrial Protocol Integration (Future)

---

## Current Features

### Machine State Simulation

The simulator models equipment operating states:

- STAND BY
- READY
- RUN
- ERROR

State transitions are managed through a finite state machine.

---

### Production Tracking

The simulator tracks:

- Units Processed
- Good Units
- Bad Units
- Production Lots

Example:

```text
Machine-01
Units Processed: 100
Good Units: 95
Bad Units: 5
```

---

### Alarm Simulation

Randomized alarm generation simulates real manufacturing failures.

Examples:

- Conveyor Jam
- Sensor Misalignment
- Vision Inspection Failure
- Emergency Stop

---

### OEE Calculation

Current implementation supports:

- Availability
- Performance
- Quality

Combined into:

```text
OEE = Availability × Performance × Quality
```

Used to evaluate machine effectiveness during runtime.

---

## Current Architecture

```text
smart_factory_simulator
│
├── simulator
│   ├── machine.py
│   ├── states.py
│   ├── alarms.py
│   ├── production.py
│   └── metrics.py
│
├── communication
│
├── dashboard
│
└── main.py
```

---

## Roadmap

### Sprint 1 (Completed)

- Machine State Model
- Production Lots
- Alarm System
- OEE Metrics
- Main Simulation Loop

---

### Sprint 2 (Planned)

Event-Driven Architecture

Planned features:

- Event Bus
- State Change Events
- Production Events
- Alarm Events
- OEE Update Events

Goal:

```text
Machine Simulator
        ↓
      Events
        ↓
Dashboard / Database / SECS-GEM
```

---

### Sprint 3 (Planned)

Production Analytics

- Cycle Time Tracking
- Throughput Metrics
- Yield History
- Downtime History

---

### Sprint 4 (Planned)

Multi-Machine Manufacturing Line

Examples:

```text
Machine-01
    ↓
Machine-02
    ↓
Machine-03
```

Features:

- Line Throughput
- Machine Utilization
- Inter-machine Dependencies

---

### Sprint 5 (Planned)

Bottleneck Detection

Automatically identify:

- Throughput Constraints
- Capacity Loss
- Production Bottlenecks

---

### Sprint 6 (Planned)

Web Dashboard

Planned technologies:

- Dash
- Plotly

Dashboard features:

- Live Machine Status
- OEE Monitoring
- Production Trends
- Alarm Monitoring

---

### Sprint 7 (Planned)

Data Persistence

Potential technologies:

- SQLite
- PostgreSQL

Stored data:

- Production History
- Alarm Logs
- OEE Metrics
- Shift Reports

---

### Sprint 8 (Future)

Industrial Communication Layer

Research and implementation of:

- SECS/GEM
- HSMS Communication
- Equipment Event Reporting

Goal:

Enable communication between the simulator and external Manufacturing Execution Systems (MES).

---

## Technical Stack

Current:

- Python
- Object-Oriented Programming

Planned:

- Dash
- Plotly
- SQLite
- PostgreSQL
- SECS/GEM Concepts
- Event-Driven Architecture

---

## Future Vision

The long-term objective is to evolve this project from a standalone simulator into a manufacturing digital twin platform capable of:

- Simulating production equipment
- Tracking factory KPIs
- Performing bottleneck analysis
- Monitoring OEE in real time
- Visualizing manufacturing performance
- Supporting industrial communication standards

---

## Author

Orlando Adams

Manufacturing Engineering • Industrial Automation • Software Development