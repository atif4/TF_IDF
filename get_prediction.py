def get_prediction():
    #train the algorithm on training data and predict using the testing data
    pred = gnb.fit(data_train, target_train).predict(data_test)
    #print('Prediction',pred.tolist())
    print ('the accuracy score of the model')
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
get_prediction()
    
        