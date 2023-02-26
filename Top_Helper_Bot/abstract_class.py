from abc import abstractmethod, ABC


class ShowRecords(ABC):
    @abstractmethod
    def show_one_record(self, name):
        pass

    @abstractmethod
    def show_all_records(self):
        pass
