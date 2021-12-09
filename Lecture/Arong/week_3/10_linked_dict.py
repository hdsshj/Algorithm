class LinkedTuple:
    def __init__(self):
        self.items = list()
    
    # [("kadfkdf8", "test")]  ->  [("asfdsdf", "test33")]    
    def add(self, key, value):
        self.items.append((key, value))
    
    # 튜블 내에서 값을 찾기 위해선 key가 또 하나 필요하다.
    def get(self, key):
        for k, v in self.items:
            if key == k:
                