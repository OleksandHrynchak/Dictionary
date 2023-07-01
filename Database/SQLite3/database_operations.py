import sqlite3


def connect() -> sqlite3.Connection:
    """
    connect:
        Establishes a connection to the SQLite database and returns an `sqlite3.Connection` object.
    """
    try:
        connection = sqlite3.connect("Database/SQLite3/dictionary_data.sqlite")
        return connection
    except sqlite3.Error as error:
        print(f"Error connecting to SQLite database 'connect': {error}")


def add_theme(text_value: str):
    """
    add_theme:
        takes the theme name and writes it to the database in the themes table.
    """
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
    """
    themes_from_db:
        retrieves the themes names from the database and returns them as a list.
    """
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
    """
    id_theme:
        takes the name of the theme and outputs its id in the global variable `theme_id`.\n
        used on the `Theme` screen.
    """
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
    """
    output_notes:
        outputs the words and translation according to the theme id from the `Notes` table,
        using the 'theme_id' change.\n
        used on the `Theme` screen.
    """
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
    """
    id_settings_theme:
        takes the name of the theme and outputs its id in the global variable `settings_theme_id`.\n
        used on the `Settings` screen.
    """
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
    """
    output_settings_notes:
        outputs the words and translation according to the theme id from the `Notes` table,
        using the 'settings_theme_id' change.\n
        used on the `Settings` screen.
    """
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
    """
    save_word_and_translate:
        takes two values `word` and `translation` and stores them in the `Notes` table according to the selected theme.
    """
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
    """
    save_word_and_translate:
        takes `update` which new name of the selected theme using `theme_id` and renames it.
    """
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
    """
    delete_theme:
        removes the theme selected by `theme_id`.
    """
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
    """
    delete_theme:
        deletes all notes where id equals `theme_id`.
    """
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

    update_note:
        accepts new 'words' and 'translates' and old 'words' and 'translations' and replaces old ones with new ones.
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
    """
    delete_note:
        takes the word and translation and removes them from the selected `theme_id`.
    """
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


def change_save(settings: dict):
    """
    change_save:
        takes the dictionary with the selected settings and updates it in the `Settings` table.
    """
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
    """
    change_save:
        outputs a tuple with stored values from the `Settings` table.
    """
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
