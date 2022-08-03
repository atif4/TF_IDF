def get_test_train():
    data_train, data_test, target_train, target_test = train_test_split(data  ,target , test_size = 0.30, random_state = 10)
    return data_train, data_test, target_train, target_test
data_train, data_test, target_train, target_test  = get_test_train()

    