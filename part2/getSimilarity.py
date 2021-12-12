from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.functions import *
from pyspark.sql.types import *
import os
import subprocess

# Calculate the Jaccard similarity between the two sets.
def getJaccardDist(set1, set2):
    intersection = set1.intersection(set2)
    return float(len(intersection)) / float(len(set1) + len(set2) - len(intersection))

sc = SparkContext()
sqlContext = SQLContext(sc)
spark = SparkSession.builder.appName("getSimilarity").getOrCreate()

# Create an empty output table.
schema = StructType([
    StructField('fileName', StringType(), True),
    StructField('similarity', FloatType(), True)
])
result = spark.createDataFrame(spark.sparkContext.emptyRDD(), schema)

# Retrieve all file names in the project_data folder.
cmd = 'hdfs dfs -ls /user/CS-GY-6513/project_data/'
files = subprocess.check_output(cmd, shell=True).decode("utf-8").strip().split('\n')

# Read the names of the columns in the reference file (assigned dataset).
refFileName = '/user/CS-GY-6513/project_data/data-cityofnewyork-us.ic3t-wcy2.csv'
refFile = sc.textFile(refFileName)
refColNames = refFile.take(1)[0]
refColNames = set(refColNames.split(','))

fileNames = []
for path in files:
    fileNames.append(path.split(' ')[-1])


for fileName in fileNames:
    if fileName == refFileName or not fileName.endswith('.csv'):
         continue
    # Read the column names of the target csv file.
    tarFile = sc.textFile(fileName)
    tarColNames = tarFile.take(1)[0]
    tarColNames = set(tarColNames.split(','))
    # Calculate the Jaccard similarity between the reference csv and the target csv.
    score = getJaccardDist(refColNames, tarColNames)
    # Append the score to the result table.
    shortFileName = fileName.split('/')[-1]
    newRow = spark.createDataFrame([(shortFileName, score)], schema)
    result = result.union(newRow)
# Export the top 50 dataset that have highest similarity to the assigned dataset.
result = result.sort('similarity', ascending=False).limit(50).write.save("similarityRank.out", format="csv")
