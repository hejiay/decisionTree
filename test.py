import trees
myData, labels = trees.createDataSet()
print(trees.chooseBestFeatureToSplit(myData))
#print(trees.splitDataSet(myData, 0, 1))
#print(trees.splitDataSet(myData, 0, 0))
print(myData)
#print(trees.calcShannonEnt(myData))