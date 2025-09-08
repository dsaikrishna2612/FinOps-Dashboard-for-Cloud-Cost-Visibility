# FinOps-Dashboard-for-Cloud-Cost-Visibility

## 📌 Overview
This project provides a dashboard to monitor cloud usage and detect when services exceed free-tier limits using AWS Cost Explorer and Grafana.

## 🚀 Features
- Daily cost tracking via AWS API
- SQLite database for historical data
- Grafana dashboard for visualization
- Alert logic for free-tier breaches

## 🛠️ Setup Instructions
1. Configure AWS credentials
2. Initialize database:
   ```bash
   python db_init.py
3. Fetch cost data:
   python fetch_aws_costs.py
4. Run alert logic:
   python alert_logic.py
5. Import dashboard.json into Grafana


📂 Folder Structure
scripts/: Python scripts for data collection and alerts

grafana/: Dashboard configuration

dashboard_screenshots/: Visual proof of dashboard
