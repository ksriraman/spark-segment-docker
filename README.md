# Segment Server side integration using Docker example application 

## **Pre-requisites**:

#### **Install docker**: 
[Docker Installation](https://docs.docker.com/installation/)

#### **Download WordCount.py example with Segment server side integration (Update Write key to your account)**: 
[WordCount.py](https://github.com/ksriraman/spark_segment_docker/blob/master/WordCount.py)

#### **Pull Docker image**:
```docker pull karthicks/apache_spark_segment```

## **Execution**:

### **Run image in background and mount WordCount.py**:
As needed, replace _/root_ below with folder containing WordCount.py

```docker run -td -v /root/WordCount.py:/WordCount.py karthicks/apache_spark_segment:latest```

#### **Enter docker bash shell (Replace CONTAINERID from above output)**:
```docker exec -i -t CONTAINERID bash -l```

#### **Run WordCount application**:
```python WordCount.py```

####**Verify Segment Data in Debugger tab**:
https://segment.com/_username_/_project_/debugger

-----------------------------------------------------------------------------------------------------------

##### _This example uses the [cdh-spark image](https://registry.hub.docker.com/u/ypandit/cdh-spark/) contributed by [ypandit ](https://hub.docker.com/u/ypandit/)_
