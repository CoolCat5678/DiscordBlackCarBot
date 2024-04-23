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
    
class Passenger:
    def __init__(self, data) -> None:
        self.JoinNumber = data['JoinNumber']
        self.JoinNumber = data['PlayerName']
        self.JoinNumber = data['DiscordID']