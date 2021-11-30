class Dataset:
    def __init__(self,):
        self.path = config.path
        self.data = self.read_data(self,self.path)
    def read_data(self,path):
        """
        :param path: data path
        :return: self.data
        """
        pass