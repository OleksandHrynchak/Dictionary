import sqlite3


def connect():
    try:
        connection = sqlite3.connect("Database/SQLite3/dictionary_data.sqlite")
        return connection
    except sqlite3.Error as error:
        print(f"Error connecting to SQLite database 'connect': {error}")


def add_theme(text_value: str):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO Themes (theme) VALUES (?)", (text_value,))
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing INSERT query 'add_theme': {error}")
    finally:
        connection.close()


def themes_from_db() -> list:
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT theme FROM Themes")
        list_of_theme = [record[0] for record in cursor.fetchall()]
        connection.commit()
        return list_of_theme
    except sqlite3.Error as error:
        print(f"Error executing SELECT query 'themes_from_db': {error}")
    finally:
        connection.close()


def id_theme(spinner, theme: str):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Themes WHERE theme = ?", (theme,))
        global theme_id
        theme_id = cursor.fetchone()[0]
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing SELECT query 'id_theme': {error}")
    finally:
        connection.close()


def output_notes() -> list:
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT word, translate FROM Notes WHERE themes_id = ?", (theme_id,)
        )
        records = cursor.fetchall()
        notes = [note for record in records for note in record]
        connection.commit()
        return notes
    except sqlite3.Error as error:
        print(f"Error executing SELECT query 'output_notes': {error}")
    finally:
        connection.close()


def id_settings_theme(spinner, theme: str):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM Themes WHERE theme = ?", (theme,))
        global settings_theme_id
        settings_theme_id = cursor.fetchone()[0]
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing SELECT query 'id_settings_theme': {error}")
    finally:
        connection.close()


def output_settings_notes() -> list:
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT word, translate FROM Notes WHERE themes_id=?", (settings_theme_id,)
        )
        records = cursor.fetchall()
        notes = [note for record in records for note in record]
        connection.commit()
        return notes
    except sqlite3.Error as error:
        print(f"Error executing SELECT query 'output_settings_notes': {error}")
    finally:
        connection.close()


def save_word_and_translate(word: str, translate: str):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO Notes (word, translate, themes_id) VALUES (?, ?, ?)",
            (word, translate, theme_id),
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing INSERT query 'save_word_and_translate': {error}")
    finally:
        connection.close()


def update_theme(update: str):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Themes SET theme=? WHERE id=?",
            (
                update,
                theme_id,
            ),
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing UPDATE query 'update_theme': {error}")
    finally:
        connection.close()


def delete_theme():
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Themes WHERE id=?", (theme_id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing DELETE query 'delete_theme': {error}")
    finally:
        connection.close()


def delete_notes():
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Notes WHERE themes_id=?", (theme_id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing DELETE query 'delete_notes': {error}")
    finally:
        connection.close()


def update_note(up_word: str, up_translate: str, old_word: str, old_translate: str):
    """
    `up_word` -> `update_word`\n
    `up_translate` -> `update_translate`\n
    """
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Notes SET word=?, translate=? WHERE themes_id=? AND word=? AND translate=?",
            (up_word, up_translate, theme_id, old_word, old_translate),
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing UPDATE query 'update_note': {error}")
    finally:
        connection.close()


def delete_note(word: str, translate: str):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM Notes WHERE themes_id=? AND word=? AND translate=?",
            (theme_id, word, translate),
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing DELETE query 'delete_note': {error}")
    finally:
        connection.close()


def change_save(settings):
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Settings SET theme=?, verify=?, repetition=?, word=?, translate=?, randomly=?, successively=?, timer=?",
            (
                settings["theme"],
                settings["verify"],
                settings["repetition"],
                settings["word"],
                settings["translate"],
                settings["randomly"],
                settings["successively"],
                settings["timer"],
            ),
        )
        connection.commit()
    except sqlite3.Error as error:
        print(f"Error executing UPDATE query 'change_save': {error}")
    finally:
        connection.close()


def call_settings() -> tuple:
    connection = connect()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Settings")
        settings = cursor.fetchone()
        connection.commit()
        return settings
    except sqlite3.Error as error:
        print(f"Error executing SELECT query 'call_settings': {error}")
    finally:
        connection.close()
