from pyspark import SparkContext
import analytics

analytics.write_key = 'vYMEyDSwgdCuIpakFZBa4gbYkM6z1vuA'

inputFile = "file:/wordcount/input/Had*"
sc = SparkContext("local", "Simple App")
inputData = sc.textFile(inputFile).cache()

counts = inputData.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)

analytics.identify('019mr8mf4r', {
    'email': 'karthick@example.com',
    'name': 'Karthick Sriraman',
    'context': 'Ran Word Count on Spark',	
})

counts.saveAsTextFile("file:/wordcount/output/counts")
