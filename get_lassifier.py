def get_lassifier():
    #create object of the lassifier
    neigh = KNeighborsClassifier(n_neighbors=3)
    #Train the algorithm
    neigh.fit(data_train, target_train)
    # predict the response
    pred = neigh.predict(data_test)
    # evaluate accuracy
    print ("KNeighbors accuracy score : ",accuracy_score(target_test, pred))
get_lassifier()
