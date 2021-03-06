from abc import ABC, abstractmethod


class GeneralModel(ABC):
    @abstractmethod
    def fit(self, dataset, sentiment_dicts):
        """
            Fit model
        :param dataset: list of data
        :param sentiment_dicts: list of ground truth dictionaries
        """
        pass

    @abstractmethod
    def predict(self, dataset, sentiment_dicts):
        """
            Predict values from dataset
        :param dataset: list of data
        :param sentiment_dicts: list of entity dictionaries
        :return: predicted sentiments (list of dictionaries)
        """
        return None

    def get_name(self):
        return self.__class__.__name__

    def print(self, *print_args):
        print('[%s]' % self.get_name(), end=' ')
        print(*print_args)
