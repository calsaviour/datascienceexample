def dispatcher():
    train_path = "../data/train.csv"
    train = pd.read_csv(train_path)
    test_path = "../data/test.csv"
    test = pd.read_csv(test_path)
    
def load_ipython_extension(ipython, *args):
    ipython.register_magic_function(dispatcher, 'line', magic_name="load")
