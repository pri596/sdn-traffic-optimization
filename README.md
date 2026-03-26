# SDN Traffic Optimization using Machine Learning

##  Overview

Efficient traffic management is a critical challenge in Software Defined Networking (SDN), where dynamic network conditions can lead to congestion, latency, and suboptimal routing decisions.

This project implements a **locally hosted web-based system** that integrates **machine learning with SDN simulation** to enable intelligent traffic prediction and optimization. The system provides an interactive interface to simulate network behavior and analyze performance metrics.

---

##  Objective

The goal of this project is to:

* Predict network traffic patterns using machine learning
* Improve routing decisions through intelligent policy control
* Provide a user interface for monitoring and analysis
* Demonstrate integration of ML models within an SDN-like environment

---

##  System Architecture

The system is designed as an end-to-end pipeline:

```
User → Web Interface → SDN Simulator → ML Model → Traffic Prediction → QoS Policy → Output
```

---

##  System Components

###  Web Application (Django)

* Handles user interaction and routing
* Provides dashboards and report views
* Supports authentication and user management

###  SDN Simulator

* Simulates network traffic behavior
* Generates data for prediction
* Acts as a simplified SDN environment

###  Machine Learning Model

* Trained on network-related features
* Predicts traffic conditions
* Stored as a serialized model (`.pkl`)

###  QoS Policy Module

* Applies decision logic based on predictions
* Simulates traffic optimization strategies

---

##  Features

* Real-time traffic simulation interface
* Performance metrics visualization
* Basic reporting system
* Integration of ML predictions into network decision flow

---

##  Key Insight

This project demonstrates how machine learning can be integrated into SDN systems to enable **data-driven traffic management**, moving beyond static or rule-based approaches.

---

##  Limitations

* Simplified SDN simulation (not a full Mininet/OpenFlow setup)
* Local deployment only
* Limited dataset and model tuning

---

##  Future Improvements

* Integration with real SDN controllers (e.g., OpenDaylight, ONOS)
* Advanced traffic prediction models
* Deployment as a scalable web service
* Real-time streaming data integration

---

##  Tech Stack

* Python
* Django
* Machine Learning (Scikit-learn / model serialization)
* HTML, CSS
* SQLite (local database)

---

##  How to Run

```bash
pip install -r requirements.txt
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000/
```

---

##  Conclusion

This project showcases a system-level approach to combining **machine learning and networking concepts**, highlighting how predictive models can enhance decision-making in SDN environments.

It reflects not just model development, but the integration of ML into a **functional application workflow**.
alhost:8000/

