from dataclasses import dataclass
from sqlite3 import Connection, Cursor

from core.subscribes import Subscribe


@dataclass
class SubscribesDataBase:
    con: Connection
    cur: Cursor

    def add_subscribe(self, subscribe_type: str, subscribe_price: float, subscribe_trial: int):
        self.cur.execute("INSERT INTO SUBSCRIBE (SUBSCRIBE_TYPE, SUBSCRIBE_PRICE, TRIAL_DAY) VALUES (?,?,?)",
                         [subscribe_type, subscribe_price, subscribe_trial])
        self.con.commit()

    def get_subscribe_by_id(self, subscribe_id: int) -> Subscribe:
        subscribe = self.cur.execute("SELECT * FROM SUBSCRIBE WHERE ID = ?", [subscribe_id]).fetchone()
        if subscribe is not None:
            return Subscribe(subscribe[0], subscribe[1], subscribe[2], subscribe[3])

    def get_subscribes(self) -> list[Subscribe]:
        subscribes = self.cur.execute("SELECT * FROM SUBSCRIBE")
        subs = []
        for sub_id, sub_type, sub_price, trial_day in subscribes:
            subs.append(Subscribe(sub_id, sub_type, sub_price, trial_day))
        return subs

    def add_subscribe_to_user(self, subscribe_id: int, user_id: int):
        subscribe = self.get_subscribe_by_id(subscribe_id)
        self.cur.execute(
            "UPDATE USERS "
            "SET SUBSCRIBE_ID = ?,"
            " START_SUBSCRIBE_DATE = CURRENT_DATE,"
            " END_SUBSCRIBE_DATE = DATE(CURRENT_DATE, ?)"
            "WHERE ID = ?", [subscribe_id, f'{subscribe.subscribe_trial} days', user_id])
        self.con.commit()
