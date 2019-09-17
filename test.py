import trees
import treePlotter
myData, labels = trees.createDataSet()
#print(trees.chooseBestFeatureToSplit(myData))
#print(trees.splitDataSet(myData, 0, 1))
#print(trees.splitDataSet(myData, 0, 0))
#print(myData)
#classList = [3, 4, 5, 2, 2, 4, 4]
#print(trees.majorityCnt(classList))
#print(trees.calcShannonEnt(myData))
#myTree = trees.createTree(myData, labels)

#treePlotter.createPlot()
myTree = treePlotter.retrieveTree(0)
myTree['no surfacing'][3] = 'maybe'
print(myTree)
treePlotter.createPlot(myTree)