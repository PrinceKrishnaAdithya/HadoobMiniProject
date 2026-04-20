import os
conf = '/opt/hadoop/etc/hadoop'

open(conf+"/core-site.xml","w").write('<?xml version="1.0"?><configuration><property><name>fs.defaultFS</name><value>hdfs://namenode:8020</value></property></configuration>')
open(conf+"/mapred-site.xml","w").write('<?xml version="1.0"?><configuration><property><name>mapreduce.framework.name</name><value>yarn</value></property><property><name>yarn.app.mapreduce.am.env</name><value>HADOOP_MAPRED_HOME=/opt/hadoop</value></property><property><name>mapreduce.map.env</name><value>HADOOP_MAPRED_HOME=/opt/hadoop</value></property><property><name>mapreduce.reduce.env</name><value>HADOOP_MAPRED_HOME=/opt/hadoop</value></property></configuration>')
open(conf+"/yarn-site.xml","w").write('<?xml version="1.0"?><configuration><property><name>yarn.resourcemanager.hostname</name><value>resourcemanager</value></property><property><name>yarn.nodemanager.aux-services</name><value>mapreduce_shuffle</value></property><property><name>yarn.nodemanager.vmem-check-enabled</name><value>false</value></property></configuration>')
print("Hadoop config files written.")