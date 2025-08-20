# Taxi Management System

**Networking Project**  
Umm Al-Qura University – Software Engineering Dept.  
Completed: 6 February 2024   

---

## Project Description
The **Taxi Management System (TMS)** is a client-server application built using **TCP sockets** in Python.  
It simplifies operations for managers, supports customers with ride requests, and ensures effective communication between drivers, managers, and customers.

The system was implemented with:
- **Threading** → for concurrent client handling.  
- **Multiprocessing** → for calculating profits & maintenance more efficiently.  
- **TCP protocol** → for reliable communication.  
- **Google Maps API (via Python client)** → for geolocation and nearby places.  

---

## Main Features
- **Ride Requests** – customers can request a taxi via TCP client.  
- **Driver Rating** – users can submit driver ratings (handled on separate port).  
- **Manager Chatroom** – TCP-based chat for management communication.  
- **Profit Calculation** – multiprocessing for dividing profits among managers, drivers, and cars.  

---

## Tech Stack
- **Language:** Python  
- **Libraries:** `socket`, `threading`, `multiprocessing`, `requests`, `googlemaps`  
- **Protocol:** TCP  

---

## Contributors
- Layan Alsayed   
- Aya Babkoor   
- Rema Alghamdi   

