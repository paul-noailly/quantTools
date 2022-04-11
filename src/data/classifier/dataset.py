from data.classifier.contract import Contract
from data.classifier.topic import Topic


class Dataset():
    def __init__(self, contract:Contract, topic:Topic) -> None:
        self.contract = contract
        self.topic = topic
    
    # data
    
    def _get_key(self):
        return f"d_[{self.contract._get_key()}][{self.topic._get_key()}]"
    
    def _asdict(self):
        return {
            'contract': self.contract._asdict(),
            'topic': self.topic._asdict(),
        }
    
    # get function
    
    def get_between_date_range(self, start_date, end_date, output='df'):
        pass
    
    def get_from_startdate(self, start_date, output='df'):
        pass
    
    def get_between_time_range(self, start_time, end_time, output='df'):
        pass
    
    def get_from_starttime(self, start_time, output='df'):
        pass
    
    