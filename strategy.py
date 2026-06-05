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

def main():
    print("\nСтратегия:\n")
    my_settings = FilterSettings(PriceIncreaseFilter)
    my_settings.filtration()
    my_settings.set_filter(PriceDecreaseFilter)
    my_settings.filtration()
    my_settings.set_filter(NewFilter)
    my_settings.filtration()
    my_settings.set_filter(OldFilter)
    my_settings.filtration()    

if __name__ == "__main__":
    main()