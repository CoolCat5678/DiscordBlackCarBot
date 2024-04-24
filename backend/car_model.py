class Passenger:
    def __init__(self, data) -> None:
        self.JoinNumber = data['JoinNumber']
        self.PlayerName = data['PlayerName']
        self.DiscordID = data['DiscordID']
        
    def __repr__(self) -> str:
        return(f'JoinNumber:{self.JoinNumber}, PlayerName:{self.PlayerName}, DiscordID:{self.DiscordID}')

class Car:
    def __init__(self, data) -> None:
        self._passengers = {}
        self.CarName: str = data['CarName']
        self.Month: int = int(data['Month'])
        self.Finished = data['Finished']
        self.PlannedDate: str = data['PlannedDate']
        self.DiscordID = data['DiscordID']
        self.FightTime: int = int(data['FightTime'])
    
    def join_passenger(self, passenger: Passenger):
        self._passengers[passenger.JoinNumber] = passenger
    
    def __repr__(self) -> str:
        result = ""
        for key, value in self._passengers.items():
            result += f"{key}: {value}\n"
        return result
    
    def __iter__(self):
        self._passenger_iter = iter(self._passengers.values())
        return self
    
    def __next__(self):
        return next(self._passenger_iter)
    
    def __getitem__(self, key) -> Passenger:
        return self._passengers[key]
    
    def __len__(self):
        return len(self._passengers)
    

class CarList:
    def __init__(self, datas) -> None:
        self._cars = {}
        self.create_list(datas)
            
    def create_list(self, datas):
        for data in datas:
            if data['CarName'] not in self._cars:
                self._cars[data['CarName']] = Car(data)
            self._cars[data['CarName']].join_passenger(Passenger(data))
            
    def __repr__(self) -> str:
        result = ""
        for key, value in self._cars.items():
            result += f"{key}: {len(value)}人\n"
        return result
    
    def __iter__(self):
        self._passenger_iter = iter(self._cars.values())
        return self

    def __next__(self):
        return next(self._passenger_iter)
    
    def __getitem__(self, key) -> Car:
        return self._cars[key]