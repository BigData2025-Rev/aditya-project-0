from abc import abstractmethod, ABC

class BaseView(ABC):

    @abstractmethod
    def print_menu(self):
        pass

    @abstractmethod
    def process_user_input(self):
        pass