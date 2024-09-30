class RedisValuesStructure:
    def __init__(
            self, usd: bytes | str, eur: bytes | str, gbp: bytes | str, timestamp: bytes | str
    ) -> None:
        self.__usd = usd.decode('utf-8')
        self.__eur = eur.decode('utf-8')
        self.__gbp = gbp.decode('utf-8')
        self.__timestamp = timestamp.decode('utf-8')

    def data(self) -> dict:
        return {
            'usd': self.__usd,
            'eur': self.__eur,
            'gbp': self.__gbp,
            'timestamp': self.__timestamp
        }


class RedisUserStructure:
    def __init__(self, username: bytes | str, timestamp: bytes | str) -> None:
        self.__username = username.decode('utf-8')
        self.__timestamp = timestamp.decode('utf-8')

    def data(self) -> dict:
        return {
            'username': self.__username,
            'timestamp': self.__timestamp
        }
