//http://localhost:4040
val textFile = sc.textFile("hdfs://localhost:9000/user/hduser/test.txt")
val counts = textFile.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_ + _).count()
print(counts)
