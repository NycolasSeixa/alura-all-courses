class Rating:
    def __init__(self, client, rate):
        self._client = client
        
        if (rate > 5):
            rate = 5
        elif rate < 0:
            rate = 0
        self._rate = rate