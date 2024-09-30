class StartMessage:
    MESSAGE = "Здравстуйте {username}, как я могу к вам обращаться?"


class UserNameMessage:
    REGISTER_MESSAGE = "Бот сохраняет ваше имя..."
    MESSAGE = "Приятно познакомиться, теперь я буду обращаться к вам <b>{username}</b>"


class ValueRateMessage:
    USD_MESSAGE = ("Здравстуйте {username}, текущий курс доллара к рублю состовляет:\n"
                   "<b>{usd_rate}</b>")
    EUR_MESSAGE = ("Здравстуйте {username}, текущий курс евро к рублю состовляет:\n"
                   "<b>{eur_rate}</b>")
    GBP_MESSAGE = ("Здравстуйте {username}, текущий курс фунтов стерлингов к рублю состовляет:\n"
                   "<b>{gbp_rate}</b>")
