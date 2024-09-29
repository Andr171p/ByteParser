class StartMessage:
    MESSAGE = "Здравстуйте {username}, как я могу к вам обращаться?"


class UserNameMessage:
    MESSAGE = "Теперь я буду обращаться к вам {username}"


class ValueRateMessage:
    MESSAGE = ("Здравстуйте {username}, текущий курс доллара к рублю состовляет:\n"
               "{usd_rate}")