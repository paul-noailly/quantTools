from typing import List, Dict


def generate_source_from_dict(dic:Dict):
    assert 'broker' in dic, "dic parameter must contain a broker:str item"
    assert 'account_type' in dic, "dic parameter must contain a account_type:str item"
    assert 'tags' in dic, "dic parameter must contain a tag:List[str] item"
    return Source(
        broker=dic['broker'],
        account_type=dic['account_type'],
        tags=dic['tags']
    )

class Source():
    def __init__(self, broker:str, account_type:str='default', tags:List[str]=[]) -> None:
        self.broker = broker
        self.account_type = account_type
        self.tags = tags
        
    def _asdict(self) -> Dict:
        return {
            'broker': self.broker,
            'account_type': self.account_type,
            'tags': self.tags
        }
        
    def _get_key(self):
        return f"s_{self.broker}|{self.account_type}"
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f"Source[ {self.broker} - {self.account_type} ]"