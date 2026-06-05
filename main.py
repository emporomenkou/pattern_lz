from strategy import FilterSettings, PriceDecreaseFilter, PriceIncreaseFilter, NewFilter, OldFilter
from abstract_fabric import ModernFabric, VictorianFabric, client_request
from tolsty_legkoves import ChairCreator, Chair


def abstract_fabric_result():
    print("\nАбстрактная фабрика\n")
    client_request(ModernFabric)
    client_request(VictorianFabric)

def legkoves_result():
    print("\nЛегковес:\n")
    misha = []
    type_chair = ChairCreator.create_chair("chair", "korichnevi")
    type_armchair = ChairCreator.create_chair("armchair", "chorni")

    misha.append(Chair(228, 1337, type_chair))
    misha.append(Chair(67, 69, type_chair))
    misha.append(Chair(0, 1, type_chair))

    misha.append(Chair(2, 3, type_armchair))    
    misha.append(Chair(6767, 6969, type_armchair))
    misha.append(Chair(228228, 13371337, type_armchair))

    for chair in misha:
        chair.fly()       

def strategy_result():
    print("\nСтратегия:\n")
    my_settings = FilterSettings(PriceIncreaseFilter)
    my_settings.filtration()
    my_settings.set_filter(PriceDecreaseFilter)
    my_settings.filtration()
    my_settings.set_filter(NewFilter)
    my_settings.filtration()
    my_settings.set_filter(OldFilter)
    my_settings.filtration()    

def main():
    abstract_fabric_result()
    legkoves_result()
    strategy_result()

if __name__ == "__main__":
    main()