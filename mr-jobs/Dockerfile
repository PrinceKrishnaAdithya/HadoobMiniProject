FROM python:3.11-slim

RUN apt-get update && apt-get install -y default-jdk curl && \
    curl -O https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz && \
    tar -xzf hadoop-3.3.6.tar.gz -C /opt && mv /opt/hadoop-3.3.6 /opt/hadoop && \
    rm hadoop-3.3.6.tar.gz

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
ENV HADOOP_USER_NAME=hadoop

COPY write_hadoop_conf.py /tmp/write_hadoop_conf.py
RUN python3 /tmp/write_hadoop_conf.py

COPY requirements.txt .
RUN pip install mrjob==0.7.4
COPY . /app
WORKDIR /app
CMD ["bash", "run_all_jobs.sh"]
