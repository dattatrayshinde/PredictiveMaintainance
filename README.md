
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

![Lambda Architecture](https://github.com/dattatrayshinde/PredictiveMaintainance/blob/master/Lambda%20Architecture/Images/lambda.png)
Here I have created real time analytics plateform by using following softwares -

1. Hadoop – Storing raw data

2. Apache Spark – For real time and batch processing

3. MongoDB – to store processed and query it as per need

4. Flask – To create REST api and UI

Installations:
---
I have done all the setup on machine with Ubuntu 14.4 as operating system.

-1. Hadoop :
---

Download & Install in follwing order :

-Installing Java

```R
cd ~
Sudo apt-get update
sudo apt-get install default-jdk
java -version
```
-Add user
```R
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo
```

-Installing SSH
```
sudo apt-get install ssh
which ssh
which sshd
su hduser
ssh-keygen -t rsa -P ""
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
ssh localhost
```

-Install Hadoop
```
wget http://mirrors.sonic.net/apache/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz
tar xvzf hadoop-2.6.0.tar.gz

~/hadoop-2.6.0$ sudo mv * /usr/local/hadoop
~/hadoop-2.6.0$ sudo mv * /usr/local/hadoop 
~/hadoop-2.6.0$ sudo chown -R hduser:hadoop /usr/local/hadoop
```
-Setup Configuration Files
```
1. ~/.bashrc
2. /usr/local/hadoop/etc/hadoop/hadoop-env.sh
3. /usr/local/hadoop/etc/hadoop/core-site.xml
4. /usr/local/hadoop/etc/hadoop/mapred-site.xml.template
5. /usr/local/hadoop/etc/hadoop/hdfs-site.xml
```

-1. ~/.bashrc
```
hduser@laptop:~$ vi ~/.bashrc

#HADOOP VARIABLES START
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export HADOOP_INSTALL=/usr/local/hadoop
export PATH=$PATH:$HADOOP_INSTALL/bin
export PATH=$PATH:$HADOOP_INSTALL/sbin
export HADOOP_MAPRED_HOME=$HADOOP_INSTALL
export HADOOP_COMMON_HOME=$HADOOP_INSTALL
export HADOOP_HDFS_HOME=$HADOOP_INSTALL
export YARN_HOME=$HADOOP_INSTALL
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_INSTALL/lib/native
export HADOOP_OPTS="-Djava.library.path=$HADOOP_INSTALL/lib"
export HADOOP_CLASSPATH=$(find $HADOOP_HOME -name '*.jar' | xargs echo | tr ' ' ':')
```
-2. /usr/local/hadoop/etc/hadoop/hadoop-env.sh

```
$ sudo nano hadoop-env.sh
#The java implementation to use.
export JAVA_HOME="/usr/lib/jvm/java-7-openjdk-amd64"
```
-3. /usr/local/hadoop/etc/hadoop/core-site.xml

```
$ sudo nano core-site.xml
<configuration>
  <property>
      <name>fs.defaultFS</name>
      <value>hdfs://localhost:9000</value>
  </property>
</configuration>
```
-4. /usr/local/hadoop/etc/hadoop/mapred-site.xml.template

```
$ sudo cp mapred.site.xml.template mapred-site.xml
$ sudo nano mapred-site.xml
<configuration>
  <property>
      <name>mapreduce.framework.name</name>
      <value>yarn</value>
  </property>
</configuration>
```
-5. /usr/local/hadoop/etc/hadoop/hdfs-site.xml
```
$ sudo nano hdfs-site.xml
<configuration>
  <property>
      <name>dfs.replication</name>
      <value>1</value>
  </property>
  <property>
      <name>dfs.namenode.name.dir</name>
      <value>file:/usr/local/hadoop/hadoop_data/hdfs/namenode</value>
  </property>
  <property>
      <name>dfs.datanode.data.dir</name>
      <value>file:/usr/local/hadoop/hadoop_store/hdfs/datanode</value>
  </property>
</configuration>
```


Format the New Hadoop Filesystem
```
$hadoop namenode -format
$ cd $HADOOP_HOME/sbin/
$start-all.sh
```
-2. Apache Spark – For real time and batch processing
---

-3. MongoDB – to store processed and query it as per need
---
Install MongoDB
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```
-Add MongoDB to system Path
```
```
-Create MongoDB folders /Data/DB
```
```

-Start MongoDB Server
```
Mongod
```
-Start MongoDB Client
```
Mongo
```
-4. Flask – To create REST api and UI
---
```
sudo pip install flask
```
#Workflow :
---
---
