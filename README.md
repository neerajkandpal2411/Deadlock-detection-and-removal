# Deadlock-detection-and-removal# 🚦 Deadlock Detection and Removal GUI

## ✨ Overview

The **Deadlock Detection and Removal GUI** is a Python-based desktop application designed to visualize and manage deadlocks in a system. Using PyQt5 for the graphical interface, it allows users to define process-resource relationships, observe the corresponding resource allocation and wait-for graphs, detect deadlocks through cycle detection, and even simulate the removal of deadlocks. This tool is ideal for students, educators, and anyone looking to gain a deeper understanding of operating system deadlock concepts.



---

## 🌟 Features

* **Interactive Process-Resource Table:** Easily input and modify which processes hold or request which resources.
* **Dynamic Graph Visualization:** Real-time generation and display of:
    * **Resource Allocation Graph:** Shows allocations (Resource -> Process) and requests (Process -> Resource).
    * **Wait-For Graph:** Simplifies the Resource Allocation Graph to show only process-to-process dependencies (Process P1 waits for Process P2).
* **Automatic Deadlock Detection:** Identifies deadlocks by detecting cycles within the Wait-For Graph.
* **Visual Deadlock Highlighting:** Deadlocked processes are visually highlighted in the graph for clear identification.
* **Simulated Deadlock Removal:** A dedicated button to simulate breaking a deadlock by removing one of the involved processes from the system.
* **User-Friendly Interface:** Intuitive design built with PyQt5 for ease of use.

---

## 🛠️ Technologies Used

* **Python 3.x**
* **PyQt5:** For building the graphical user interface.
* **NetworkX:** A powerful library for creating, manipulating, and studying the structure, dynamics, and functions of complex networks (graphs).
* **Matplotlib:** For rendering the graph visualizations within the GUI.
* **NumPy:** A dependency for Matplotlib and NetworkX for numerical operations.

---

## 🚀 Getting Started

Follow these steps to set up and run the application on your local machine.

### Prerequisites

* **Python 3.x** ([Download Python](https://www.python.org/downloads/))

---

## 💡 How to Use

1.  **Add Rows:** Click the "**Add Row**" button to add new entries to the "Process-Resource Allocation Table."
2.  **Define Allocations/Requests:**
    * **Process:** Enter the name of a process (e.g., `P1`, `P2`).
    * **Resource:** Enter the name of a resource (e.g., `R1`, `R2`).
    * **Allocated:** Type `yes` if the process **holds** the resource. Type `no` if the process **is waiting for** the resource.
    * As you type, the graph will update in real-time.
3.  **Detect Deadlock:** Click the "**Detect Deadlock**" button to explicitly check for deadlocks. Cycles in the Wait-For Graph (indicating a deadlock) will be highlighted in red. The "**Remove Deadlock**" button will become active if a deadlock is found.
4.  **Remove Deadlock:** If a deadlock is detected, click "**Remove Deadlock**." The application will simulate breaking the deadlock by removing one of the involved processes from the table and the graph, demonstrating a common strategy for deadlock resolution (process termination).

---

## 📞 Contact

Neeraj Kandpal <br>
LinkedIn : linkedin.com/in/neeraj-kandpal/ <br>
Email : neerajkandpal265@gmail.com
