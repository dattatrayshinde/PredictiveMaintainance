
# Capstone Project - Predictive Maintainance using Real Time Data Analytics 

Synopsis :

This is the project about creation of real time data analytics platform for predictive maintaince. I have just followed lambda architecture but as I am using Apache spark there is no need of the most of the components in 3 different layers of the lambada architecure which are batch layer, speed layer and serving layer. With the help of Hadoop, Apche spark , MongoDB, Apache Kafka, I have created this architecture.Using Flask architecture of python to create REST based API’s which will just predict the values for given feature set.

Lambda architecture:
---
![Lambda Architecture](https://github.com/dattatrayshinde/PredictiveMaintainance/blob/master/Lambda%20Architecture/Images/la-overview_small.png)

Using a combination of batch and real time processing systems in parallel is an approach which businesses are increasingly exploring now. While the batch layer ensures scalability and fault resilience for the system, the real time layer takes care of processing metrics required on the go. Nathan Marz coined the term Lambda Architecture (LA) to describe a generic, scalable and fault-tolerant data processing architecture.
Data that enters the system is dispatched to the batch and the speed layers for simultaneous processing. The batch layer serves two functions:
Managing the master dataset (an immutable,append-only set of raw data) Pre-computing the batch views.The serving layer indexes the batch views so that they can be queried in a low-latency and ad-hoc manner.The speed layer compensates for the high latency of updates to the serving layer and deals only with recent data.Any incoming query can be answered by merging the results from both batch and real-time views.
I have added a separate folder here which will give more details about need oF LA and different ways to implement LA.

Tools / Softwares requirement :
---
Following fig gives an idea that what tools / softwares one can use to create real time analytics platform.

![Lambda Architecture](https://github.com/dattatrayshinde/PredictiveMaintainance/blob/master/Lambda%20Architecture/Images/la-overview_small.png)
Here I have created real time analytics plateform by using following softwares -

1. Hadoop – Storing raw data

2. Apache Spark – For real time and batch processing

3. MongoDB – to store processed and query it as per need

4. Flask – To create REST api and UI

Installations:
---
1. Hadoop :

2. Apache Spark – For real time and batch processing

3. MongoDB – to store processed and query it as per need

4. Flask – To create REST api and UI

Workflow :
---
