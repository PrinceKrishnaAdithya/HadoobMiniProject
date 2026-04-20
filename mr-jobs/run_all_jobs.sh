#!/bin/bash
set -e

NAMENODE=namenode:8020

# Updated HDFS paths for SALES project
HDFS_INPUT=hdfs://$NAMENODE/user/hadoop/sales/input
HDFS_OUTPUT=hdfs://$NAMENODE/user/hadoop/sales/output

echo "Waiting for NameNode to leave safe mode..."
until hdfs dfsadmin -safemode get 2>/dev/null | grep -q "Safe mode is OFF"; do
    echo "  Still in safe mode, waiting..."
    sleep 5
done
echo "NameNode is ready."

echo "Setting up HDFS directories..."
hdfs dfs -mkdir -p $HDFS_INPUT

# Upload sales dataset
echo "Uploading dataset to HDFS..."
hdfs dfs -put -f /data/sales.csv $HDFS_INPUT/

echo "Copying input locally for mrjob local mode..."
mkdir -p /tmp/mrjob_input
hdfs dfs -get $HDFS_INPUT/sales.csv /tmp/mrjob_input/sales.csv

echo "Running MapReduce jobs (local mode)..."
mkdir -p /data/results

# SALES ANALYSIS JOBS
for JOB in sales_by_category total_revenue top_products order_count; do
    echo "  -> Running $JOB"
    python $JOB.py -r local /tmp/mrjob_input/sales.csv > /data/results/$JOB.txt
done

echo "Uploading results to HDFS..."
for JOB in sales_by_category total_revenue top_products order_count; do
    hdfs dfs -mkdir -p $HDFS_OUTPUT/$JOB
    hdfs dfs -put -f /data/results/$JOB.txt $HDFS_OUTPUT/$JOB/part-00000
done

echo "All results ready in HDFS!"