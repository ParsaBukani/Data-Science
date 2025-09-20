
# Real-Time Data Pipeline

_Data Science — University of Tehran_

This project implements a **real-time payment data pipeline** using **Apache Kafka**, **Apache Spark (PySpark)**, and **MongoDB**.  
The system simulates financial transactions, validates them, detects fraud, calculates commissions, and produces both **batch** and **real-time insights**.

## Overview

- **Scenario**  
  We act as *Darooghe*, a payment service provider. The pipeline handles events from multiple channels (online, POS, mobile, NFC), ensuring reliable ingestion, processing, and analysis.

- **Data Ingestion**  
  Kafka-based consumers validate transactions against business rules (amount consistency, timestamp checks, device checks). Invalid records are redirected to error logs.

- **Batch Processing**  
  PySpark jobs analyze **commission efficiency**, discover **transaction patterns**, and create **aggregated reports** for merchants and customers.

- **Real-Time Processing**  
  Spark Streaming processes live Kafka data to:  
  - Detect fraud (velocity checks, geographic impossibility, anomalous amounts).  
  - Monitor real-time commissions and high-performing merchants.  
  - Write results back into Kafka topics for live dashboards.

- **Storage & Visualization**  
  Data is stored in **MongoDB** with partitioning strategies for scalability.  
  Visualizations (transaction volume, merchant rankings, user activity trends) communicate both real-time and historical insights.

- **Bonus Features**  
  Includes advanced fraud detection, **dynamic pricing simulation** for commissions, and **pipeline optimization** with monitoring tools.

## Acknowledgements

Developed under the supervision of:  
**Dr. Bahrak** and **Dr. Yaghoobzadeh**  
Teaching Assistants: Javad Razi, Mohammad Reza Nemati,  
Shahriar Attar, Mohammad Amin Yousefi

