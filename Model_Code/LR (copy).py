#To run this example use:
# ./bin/spark-submit --master "local[4]"  \
#                    --conf "spark.mongodb.input.uri=mongodb://127.0.0.1/PM.ModelRunHistory?readPreference=primaryPreferred" \
#                    --conf "spark.mongodb.output.uri=mongodb://127.0.0.1/PM.ModelRunHistory" \
#                    --packages org.mongodb.spark:mongo-spark-connector_2.11:2.0.0 \
#                    /home/lenovo/projects/PredictiveMaintainance/Model_Code/LR.py

from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.classification import LogisticRegression

def runModelLR():
	# Load training data
	training = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")
	lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

	# Fit the model
	lrModel = lr.fit(training)

	# Print the coefficients and intercept for logistic regression
	print("Coefficients: " + str(lrModel.coefficients))
	print("Intercept: " + str(lrModel.intercept))


if __name__ == "__main__":
	print("INside main:")
	#sparkConf = SparkConf().setMaster("local").setAppName("LR").set("spark.app.id", "LR").addResource(new Path("/usr/local/hadoop/etc/hadoop/yarn-site.xml"))
	sparkConf = SparkConf().setAppName("LR").set("spark.app.id", "LR")
	#Configuration conf = new Configuration();
	#conf.addResource(new Path("/etc/hbase/conf/hbase-site.xml"));


	sc = SparkContext(conf=sparkConf)
	sqlContext = SQLContext(sc)

	#logger = sc._jvm.org.apache.log4j
	#logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)

	# Load the data
	df = sqlContext.read.format("com.mongodb.spark.sql").load()
	print("Schema:")
	df.printSchema()
	print(df)

	# SQL
	df.registerTempTable("ModelRunHistory")
	models_data = sqlContext.sql("SELECT Model, Acurracy FROM ModelRunHistory")
	print("models_data:")
	models_data.show()

	#call the model and get the acurracy
	model_ac = runModelLR()
	modelRunRDD = sc.parallelize([(Model,  model_ac)])
	
	
	# Save some data
	#modelRunRDD = sc.parallelize([("XGB",  80)])
	modelRun = sqlContext.createDataFrame(modelRunRDD, ["Model", "Acurracy"])
	modelRun.write.format("com.mongodb.spark.sql").mode("append").save()

	models_data = sqlContext.sql("SELECT Model, Acurracy FROM ModelRunHistory")
	print("models_data:")
	models_data.show()

#sc.stop()
