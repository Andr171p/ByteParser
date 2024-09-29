class RedisStructure:
    def __init__(self, usd, eur, gbp, timestamp) -> None:
        self.usd = usd.decode('utf-8')
        self.eur = eur.decode('utf-8')
        self.gbp = gbp.decode('utf-8')
        self.timestamp = timestamp.decode('utf-8')

    def data(self) -> dict:
        return {
            'usd': self.usd,
            'eur': self.eur,
            'gbp': self.gbp,
            'timestamp': self.timestamp
        }
