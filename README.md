# SDN-Based Traffic Routing Optimization using Machine Learning

##  Overview

Efficient traffic routing is a fundamental challenge in Software Defined Networking (SDN), where dynamic network conditions can lead to congestion, latency, and inefficient resource utilization.

This project implements a **locally hosted web-based system** that integrates **machine learning with an SDN-inspired traffic simulation environment** to enable **intelligent routing decisions and traffic optimization**.

The system moves beyond static routing by using predictive insights to guide **adaptive Quality of Service (QoS) policies**, improving overall network efficiency.

---

##  Objective

The primary goal of this project is to:

* Enable **intelligent traffic routing** using machine learning
* Simulate SDN-like network conditions
* Optimize traffic flow using QoS-based decision policies
* Provide an interactive interface for monitoring and analysis

---

##  System Architecture

The system follows an end-to-end decision pipeline:

```text id="3pmd8o"
User → Web Interface → SDN Simulator → ML Model → Traffic Prediction → QoS Policy → Optimized Routing Output
```

---

##  Project Structure

```text id="hkthec"
sdn-traffic-optimization/
│
├── user_management/        # Django project configuration
├── users/                  # Core application logic
│   ├── sdn_simulator.py    # Network simulation logic
│   ├── qos_policy.py       # Routing & QoS decision module
│   ├── network_model.pkl   # Trained ML model
│
├── media/                  # Static assets
├── templates/              # UI interface
├── manage.py
├── requirements.txt
```

---

##  Core Components

### 🔹 SDN Simulator

* Simulates network traffic conditions and flow behavior
* Generates input features for the ML model
* Represents a simplified SDN environment

---

### 🔹 Machine Learning Model

* Predicts traffic conditions and congestion patterns
* Provides insights used for routing decisions
* Enables data-driven optimization

---

### 🔹 QoS Policy Module

* Translates predictions into routing decisions
* Simulates adaptive traffic control strategies
* Acts as a simplified SDN controller logic

---

### 🔹 Web Application (Django)

* Provides user interface for interaction
* Displays traffic metrics and results
* Integrates all system components into a workflow

---

##  Key Features

* Intelligent traffic routing based on ML predictions
* Simulation of network conditions
* QoS-driven optimization strategies
* Interactive web interface for monitoring

---

##  Key Insight

Traditional SDN systems rely on predefined rules for routing.
This project demonstrates how **machine learning can enhance SDN by enabling adaptive, data-driven routing decisions**, improving network efficiency under dynamic conditions.

---

##  Limitations

* Simplified SDN environment (no real controller like ONOS/OpenFlow)
* Local deployment only
* Limited dataset and model tuning

---

##  Future Improvements

* Integration with real SDN controllers (e.g., ONOS, OpenDaylight)
* Advanced routing strategies using reinforcement learning
* Real-time network data streaming
* Scalable deployment for production environments

---

## 🛠️Tech Stack

* Python
* Django
* Scikit-learn
* HTML, CSS
* SQLite

---

##  How to Run

```bash id="eq5xqj"
pip install -r requirements.txt
python manage.py runserver
```

Open:

```text id="27y37h"
http://127.0.0.1:8000/
```

---

##  Conclusion

This project demonstrates a system-level approach to **intelligent traffic routing in SDN environments**, combining simulation, machine learning, and policy-based decision-making.

It highlights how predictive models can be integrated into network systems to enable **adaptive and efficient routing strategies**, moving beyond static configurations.

