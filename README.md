# 🐘 Student Mark Analytics with Hadoop MapReduce

A specialized big data analytics platform that uses a **distributed Hadoop cluster** to process student academic performance records. Using **MapReduce**, the system aggregates 7+ key metrics across 200+ students and 4 departments, serving the results through a modern, premium dashboard.

![Hadoop Dash Preview](https://img.shields.io/badge/Hadoop-3.3.x-blue.svg?logo=apachehadoop&logoColor=white) 
![Architecture](https://img.shields.io/badge/Stack-Flask%20%7C%20Nginx%20%7C%20mrjob%20%7C%20Docker-green.svg)

---

## 🚀 Key Features

*   **Distributed Processing**: Uses Apache Hadoop (HDFS & YARN) for scalable data storage and processing.
*   **Analytical Power**: 6 custom MapReduce jobs implemented in Python using `mrjob`:
    *   🏷️ **Grade Distribution**: Automated classification into O, A+, A, B+, B, C, and F.
    *   📊 **Subject Averages**: Performance analysis across 6 subjects (Math, Physics, Chem, CS, etc.).
    *   🏢 **Departmental Analytics**: Performance comparison between CSE, ECE, MECH, and CIVIL.
    *   🏆 **Top Rankers**: High-speed sorting of toppers globally across the cohort.
    *   📈 **Score Histogram**: Frequency distribution for finding the "common" score bands.
*   **Premium Dashboard**: Real-time visualization using **Chart.js** and **Lucide Icons** on a sleek Nginx-served single-page app.
*   **HDFS Integration**: Automated HDFS setup, input splitting, and result persistence.

## 🏗️ Technical Architecture

```mermaid
graph LR
    subgraph "Storage [HDFS]"
        A[students.csv] --> B[HDFS Blocks]
    </div>
    subgraph "Processing [YARN]"
        B --> C[MapReduce Jobs]
        C --> D[Result Files]
    </div>
    subgraph "API & UI"
        D --> E[Flask Backend]
        E --> F[Nginx Proxy]
        F --> G[Dashboard]
    </div>
```

---

## ⚡ Quick Start

### 1. Prerequisites
*   Docker Desktop (Windows/Mac) or Docker CE (Linux)
*   At least 4GB of RAM allocated to Docker

### 2. Launch the Cluster
Run the following command in the project root:

```powershell
docker-compose up --build
```

### 3. Accessing the Dashboard
*   **Dashboard**: [http://localhost:3000](http://localhost:3000)
*   **Hadoop NameNode**: [http://localhost:9870](http://localhost:9870)
*   **YARN ResourceManager**: [http://localhost:8088](http://localhost:8088)

---

## 📂 Project Structure

*   📁 `dataset/`: Contains the base student records (CSV) and the generated results.
*   📁 `mr-jobs/`: Core MapReduce logic implemented in Python using the `mrjob` framework.
*   📁 `flask-api/`: High-performance Flask REST API that syncs HDFS results to the UI.
*   📁 `frontend/`: Premium dashboard (Nginx/HTML5/Vanilla CSS/Chart.js).
*   📄 `docker-compose.yml`: Multi-container orchestration (7 services total).

## 🛠️ Hadoop Daemons in this Project

1.  **NameNode**: The "brain" managing the HDFS metadata and namespace.
2.  **DataNode**: Stores actual data blocks and performs processing.
3.  **ResourceManager**: The YARN scheduler determining node allocation.
4.  **NodeManager**: Runs tasks on individual worker nodes.
5.  **HistoryServer**: Maintains historical logs of completed MapReduce jobs.

---

## 📝 Modifying Data
To test with your own data, simply replace `dataset/students.csv` with your own file follow the existing column structure:
`RollNo, Name, Dept, Math, Physics, Chemistry, CS, English, DS, Total, Percentage, Grade, Result`

## ⚖️ License
MIT License. Built for Big Data Student Projects and Learning Hadoop MapReduce.
