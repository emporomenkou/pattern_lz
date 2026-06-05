from abc import ABC, abstractmethod as abm

class Chair(ABC):
    @abm
    def sit(self):
        pass
    @abm
    def broken(self):
        pass
    
class Sofa(ABC):
    @abm
    def lie(self):
        pass
    @abm
    def broken(self):
        pass

class Table(ABC):
    @abm
    def put_cup(self):
        pass
    @abm
    def broken(self):
        pass

class ModernChair(Chair):
    def sit(self):
        return "Вы сидите на стуле стиля модерн"
    def broken(self):
        return "Вы сломали стул стиля модерн"  
    
class VictorianChair(Chair):
    def sit(self):
        return "Вы сидите на стуле стиля викториан"
    def broken(self):
        return "Вы сломали стул стиля викториан" 
    
class ModernSofa(Sofa):
    def lie(self):
        return "Вы лежите на диване стиля модерн"
    def broken(self):
        return "Вы сломали диван стиля модерн"

class VictorianSofa(Sofa):
    def lie(self):
        return "Вы лежите на диване стиля викториан"
    def broken(self):
        return "Вы сломали диван стиля викториан"  
    
class ModernTable(Table):
    def put_cup(self):
        return "Вы поставили кружку на стол стиля модерн"
    def broken(self):
        return "Вы сломали стол стиля модерн"  
    
class VictorianTable(Table):
    def put_cup(self):
        return "Вы поставили кружку на стол стиля викториан"
    def broken(self):
        return "Вы сломали стол стиля викториан" 

class FurnitureFabric(ABC):
    @abm
    def create_chair(self):
        pass
    @abm
    def create_sofa(self):
        pass
    @abm
    def create_table(self):
        pass

class ModernFabric(FurnitureFabric):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self):
        return ModernSofa()    
    def create_table(self):
        return ModernTable()
    
class VictorianFabric(FurnitureFabric):
    def create_chair(self):
        return VictorianChair()
    def create_sofa(self):
        return VictorianSofa()    
    def create_table(self):
        return VictorianTable()
    
def client_request(fabric: FurnitureFabric):
    client_fabric = fabric()
    chair = client_fabric.create_chair()
    sofa = client_fabric.create_sofa()
    table = client_fabric.create_table()
    print(f"{chair.sit()} и {chair.broken()}")
    print(f"{sofa.lie()} и {sofa.broken()}")
    print(f"{table.put_cup()} и {table.broken()}")

def main():
    client_request(ModernFabric)
    client_request(VictorianFabric)

if __name__ == "__main__":
    main()

    