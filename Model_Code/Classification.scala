
-----------------------------------
//1. Get the data into the spark
-----------------------------------

// sed 1d train.tsv > train_noheader.tsv
// load raw data
val rawData = sc.textFile("hdfs://localhost:9000/user/hduser/train_noheader.tsv")
val records = rawData.map(line => line.split("\t"))
records.first
-----------------------------------
//2. Data preparation
-----------------------------------
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.linalg.Vectors
val data = records.map { r =>
	val trimmed = r.map(_.replaceAll("\"", ""))
	val label = trimmed(r.size - 1).toInt
	val features = trimmed.slice(4, r.size - 1).map(d => if (d == "?") 0.0 else d.toDouble)
	LabeledPoint(label, Vectors.dense(features))
}
data.cache
val numData = data.count

val nbData = records.map { r =>
	val trimmed = r.map(_.replaceAll("\"", ""))
	val label = trimmed(r.size - 1).toInt
	val features = trimmed.slice(4, r.size - 1).map(d => if (d == "?") 0.0 else d.toDouble).map(d => if (d < 0) 0.0 else d)
	LabeledPoint(label, Vectors.dense(features))
}

-----------------------------------
//3.create a model and calculate accurracy
//Logistic Regression Model
-----------------------------------
import org.apache.spark.mllib.classification.LogisticRegressionWithSGD
val numIterations = 10
val lrModel = gisticRegressionWithLBFGS.train(data, numIterations)
val dataPoint = data.first
val prediction = lrModel.predict(dataPoint.features)
val trueLabel = dataPoint.label
val predictions = lrModel.predict(data.map(lp => lp.features))
predictions.take(5)
val lrAccuracy = lrTotalCorrect / numData
--------------------------------------------------------------------------------------------------------------------------------------------

