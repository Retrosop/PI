
import sqlite3

class SocialNetworkProfile:
    def __init__(self, database='social_network.db'):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.create_table()

        try:
            self.conn = sqlite3.connect(database)
            self.cursor = self.conn.cursor()
            self.create_table()
        except sqlite3.DatabaseError as e:
            print(f"Ошибка подключения к базе данных: {e}")
            raise

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS social_network_profiles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            platform TEXT NOT NULL,
            followers INTEGER DEFAULT 0
        )
        ''')
        self.conn.commit()

    def insert_profile(self, username, platform, followers):
        self.cursor.execute('''
        INSERT INTO social_network_profiles (username, platform, followers)
        VALUES (?, ?, ?)
        ''', (username, platform, followers))
        self.conn.commit()

    def update_profile(self, username, followers):
        self.cursor.execute('''
        UPDATE social_network_profiles
        SET followers = ?
        WHERE username = ?
        ''', (followers, username))
        self.conn.commit()

    def delete_profile(self, username):
        self.cursor.execute('''
        DELETE FROM social_network_profiles
        WHERE username = ?
        ''', (username,))
        self.conn.commit()

    def search_profile(self, username):
        self.cursor.execute('''
        SELECT * FROM social_network_profiles
        WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone()

    def close_connection(self):
        self.conn.close()

# Automatic Tests
if __name__ == "__main__":
    profile_db = SocialNetworkProfile()

    # Test 1: Insert Profile
    print("Testing Insert...")
    profile_db.insert_profile("test_user", "Instagram", 100)
    result = profile_db.search_profile("test_user")
    assert result is not None, "Insert Test Failed"

    # Test 2: Update Profile
    print("Testing Update...")
    profile_db.update_profile("test_user", 200)
    result = profile_db.search_profile("test_user")
    assert result[3] == 200, "Update Test Failed"

    # Test 3: Delete Profile
    print("Testing Delete...")
    profile_db.delete_profile("test_user")
    result = profile_db.search_profile("test_user")
    assert result is None, "Delete Test Failed"

    print("All tests passed!")

    profile_db.close_connection()