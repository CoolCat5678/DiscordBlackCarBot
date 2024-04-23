class Car:
    def __init__(self, conn, data) -> None:
        self.conn = conn
        self.passenger = {}
        self.CarName = data['CarName']
        self.Month = data['Month']
        self.Finished = data['Finished']
        self.PlannedDate = data['PlannedDate']
        self.DiscordID = data['DiscordID']
        self.FightTime = data['FightTime']
        self.join_passenger(data)
    
    def join_passenger(self, data):
        self.passenger[data['JoinNumber']] = Passenger(data)
        
    def get_all_passenger(self):
        for k, v in self.passenger.items():
            print(k, v)
    
    def __repr__(self) -> str:
        return(f'車名:{self.CarName}, 人數{len(self.passenger)}')
            
class Passenger:
    def __init__(self, data) -> None:
        self.JoinNumber = data['JoinNumber']
        self.PlayerName = data['PlayerName']
        self.DiscordID = data['DiscordID']
        
    def __repr__(self) -> str:
        return(f'JoinNumber:{self.JoinNumber}, PlayerName:{self.PlayerName}, DiscordID:{self.DiscordID}')