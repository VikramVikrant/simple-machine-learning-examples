from sklearn.neighbors.nearest_centroid import NearestCentroid

clf = NearestCentroid()

# height , weight, shoesize of 11 persons
X=[[180,70,8],[160,45,5],[120,60,5],[190,90,10],[200,85,11],[100,60,5],[250,150,12],[120,55,6],[140,60,7],\
   [150,70,9],[90,55,3]]

# Gender of 11 persons of respective height,weight & shoesize
Y=['male','female','female','male','male','female','male','female','male','male','female'] 

clf = clf.fit(X,Y)

prediction = clf.predict([[250,150,12]])

print(prediction)
