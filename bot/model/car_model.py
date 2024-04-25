from typing import Dict

class Passenger:
    def __init__(self, data) -> None:
        self.JoinNumber = data['JoinNumber']
        self.PlayerName = data['PlayerName']
        self.DiscordID = data['DiscordID']
        
    def __repr__(self) -> str:
        result = "\n"
        result += f"JoinNumber : {self.JoinNumber}\n"
        result += f"PlayerName : {self.PlayerName}\n"
        result += f"DiscordID : {self.DiscordID}\n"
        return result

class Car:
    def __init__(self, data) -> None:
        self.__passengers: Dict[int, Passenger] = {}
        self.CarName: str = data['CarName']
        self.Month: int = int(data['Month'])
        self.Finished = data['Finished']
        self.PlannedDate: str = data['PlannedDate']
        self.DiscordID = data['DiscordID']
        self.FightTime: int = int(data['FightTime'])
    
    def join_passenger(self, passenger: Passenger):
        self.__passengers[passenger.JoinNumber] = passenger
    
    def __repr__(self) -> str:
        result = "\n"
        result += f"CarName : {self.CarName}\n"
        result += f"Month : {self.Month}\n"
        result += f"Finished : {self.Finished}\n"
        result += f"PlannedDate : {self.PlannedDate}\n"
        result += f"DiscordID : {self.DiscordID}\n"
        result += f"FightTime : {self.FightTime}\n"
        num_list = []
        for i in self.__passengers.values():
            num_list.append(i.JoinNumber)
        result += f"PlayerList : {str(num_list)}\n"
        return result
    
    def __iter__(self):
        self._passenger_iter = iter(self.__passengers.values())
        return self
    
    def __next__(self):
        return next(self._passenger_iter)
    
    def __getitem__(self, key) -> Passenger:
        return self.__passengers[key]
    
    def __len__(self):
        return len(self.__passengers)
    

class CarList:
    def __init__(self) -> None:
        self.__cars: Dict[str, Car] = {}
            
    def __repr__(self) -> str:
        result = "\n"
        for key, value in self.__cars.items():
            result += f"{key}:{len(value)}人 預計:{value.PlannedDate}\n"
        return result
    
    def __iter__(self):
        self._passenger_iter = iter(self.__cars.values())
        return self

    def __next__(self):
        return next(self._passenger_iter)
    
    def __getitem__(self, key) -> Car:
        return self.__cars[key]
    
    def _create_list(self, datas):
        for data in datas:
            if data['CarName'] not in self.__cars:
                self.__cars[data['CarName']] = Car(data)
            self.__cars[data['CarName']].join_passenger(Passenger(data))