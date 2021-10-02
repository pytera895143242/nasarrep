import sqlite3


class DateBase:
    def __init__(self, date_base_file):
        self.connection = sqlite3.connect(date_base_file)
        self.cursor = self.connection.cursor()

    def records_of_all_users(self, username, user_id):
        """Записывает всех пользователей, в таблицу all_users"""
        with self.connection:
            return self.cursor.execute("INSERT INTO all_users('username', 'user_id') VALUES(?, ?)",
                                       (username, user_id))

    def records_of_mailing_users(self, username, user_id):
        """Записывает всех пользователей, в таблицу all_users"""
        with self.connection:
            return self.cursor.execute("INSERT INTO mailing_users('username', 'user_id') VALUES(?, ?)",
                                       (username, user_id))

    def count_string(self):
        with self.connection:
            self.cursor.execute("SELECT Count(*) FROM all_users")
            return self.cursor.fetchone()[0]

    def mailing_user_id(self):
        with self.connection:
            self.cursor.execute("SELECT * FROM mailing_users")
            self.users_id = self.cursor.fetchall()
            return self.users_id

    def delete_user(self, user_id):
        with self.connection:
            return self.cursor.execute(f"DELETE FROM mailing_users WHERE user_id = {user_id}")

    def count_string2(self):
        with self.connection:
            self.cursor.execute("SELECT Count(*) FROM mailing_users")
            return self.cursor.fetchone()[0]