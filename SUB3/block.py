from datetime import date
from trial import trial

class block():
    def __init__(self, patID=1234, date=str(date.today()), sess=1, blocknum=1):
        self.patID = patID
        self.date = date
        self.session = sess
        self.blocknum = blocknum
        self.trials = list()
    
    def obj_from_json(self, json):
        self.patID = json['info']['patID']
        self.date = json['info']['date']
        self.session = json['info']['session']
        self.blocknum = json['info']['blocknum']
        self.avg_success = json['results']['avgsuccess']
        self.trials = [trial().obj_from_json(t)
                       for t in list(json['trials'].values())]

        return self

    def compute_avg_success(self) -> None:
        if self.trials:
            return sum([trl.success for trl in self.trials]) / len(self.trials)

    def number_of_trials(self):
        return len(self.trials)

    def copy_block(self):
        return block(self.patID, self.date, self.session, self.blocknum + 1)
