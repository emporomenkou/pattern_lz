from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def filter():
        pass

class PriceIncreaseFilter(Filter):
    def filter():
        print("Отсортировано по возрастанию цены")
class PriceDecreaseFilter(Filter):
    def filter():
        print("Отсортировано по убыванию цены")
class NewFilter(Filter):
    def filter():
        print("Отсортировано по новизне(сначала новые)")
class OldFilter(Filter):
    def filter():
        print("Отсортировано по новизне(сначала старые)")        

class FilterSettings():
    def __init__(self, selected_filter : Filter):
        self.filter_type = selected_filter
    def set_filter(self, selected_filter : Filter):
        self.filter_type = selected_filter
    def filtration(self):
        self.filter_type.filter() 
