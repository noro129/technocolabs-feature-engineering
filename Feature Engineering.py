#Feature Engineering
##Creating Features

#1
X_1["LivLotRatio"] = X.GrLivArea/X.LotArea
X_1["Spaciousness"] = (X.FirstFlrSF + X.SecondFlrSF)/X.TotRmsAbvGrd
X_1["TotalOutsideSF"]=X.WoodDeckSF+X.OpenPorchSF+X.EnclosedPorch+X.Threeseasonporch+X.ScreenPorch

#2
X_2 = pd.get_dummies(df.BldgType, prefix="Bldg")
X_2 = X_2.mul(df.GrLivArea, axis=0)

#3
X_3["PorchTypes"]=X[['WoodDeckSF','OpenPorchSF','EnclosedPorch','Threeseasonporch','ScreenPorch']].gt(0).sum(axis=1)

#4
X_4["MSClass"] = df.MSSubClass.str.split("_", n=1, expand=True)[0]

#5
X_5["MedNhbdArea"] = X.groupby('Neighborhood').GrLivArea.transform('median')

##Clustering With K-Means

#2
features = ['LotArea','TotalBsmtSF','FirstFlrSF','SecondFlrSF','GrLivArea']

kmeans = KMeans(n_clusters=10,n_init=10, random_state=0)
X_scaled = kmeans.fit_predict(X_scaled)
X["Cluster"]=X_scaled

#3
X_cd = kmeans.fit_transform(X_scaled)

##Principal Component Analysis

#2
X=X.join(X_pca)

##Target Encoding

#2
encoder=MEstimateEncoder(cols=['Neighborhood','SaleType','Exterior1st','Exterior2nd'],m=2)

encoder.fit(X_encode,y_encode)

