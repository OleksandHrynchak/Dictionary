import pymysql


def connect():
    """
    connect:
        Establishes a connection to a MySQL database and returns a connection object.
    """
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            port=3306,
            database="dictionary_db",
            cursorclass=pymysql.cursors.DictCursor,
        )
        return connection
    except pymysql.Error as error:
        print(f"Error executing INSERT query: {error}")


def add_theme(text_value: str):
    """
    add_theme:
        takes the theme name and writes it to the database in the themes table.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Themes (theme) VALUES ('{text_value}')")
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing INSERT query: {error}")
    finally:
        connection.close()


def themes_from_db() -> list:
    """
    themes_from_db:
        retrieves the themes names from the database and returns them as a list.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Themes")
            list_of_theme = [record.get("theme") for record in cursor.fetchall()]
            connection.commit()
        return list_of_theme
    except pymysql.Error as error:
        print(f"Error executing SELECT query: {error}")
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
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id FROM Themes WHERE theme ='{theme}'")
            global theme_id
            theme_id = cursor.fetchone().get("id")
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing SELECT query: {error}")
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
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT word, translate \
                    FROM Notes \
                    WHERE themes_id={theme_id}"
            )
            records = [
                (value.get("word"), value.get("translate"))
                for value in cursor.fetchall()
            ]
            notes = []
            [notes.extend(note) for note in records]
            connection.commit()
            return notes

    except pymysql.Error as error:
        print(f"Error executing SELECT query: {error}")
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
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT id FROM Themes WHERE theme ='{theme}'")
            global settings_theme_id
            settings_theme_id = cursor.fetchone().get("id")
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing SELECT query: {error}")
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
        with connection.cursor() as cursor:
            cursor.execute(
                f"SELECT word, translate \
                    FROM Notes \
                    WHERE themes_id={settings_theme_id}"
            )
            records = [
                (value.get("word"), value.get("translate"))
                for value in cursor.fetchall()
            ]
            notes = []
            [notes.extend(note) for note in records]
            connection.commit()
            return notes

    except pymysql.Error as error:
        print(f"Error executing SELECT query: {error}")
    finally:
        connection.close()


def save_word_and_translate(word: str, translate: str):
    """
    save_word_and_translate:
        takes two values `word` and `translation` and stores them in the `Notes` table according to the selected theme.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO Notes (word,translate,themes_id) \
                                VALUES ('{word}','{translate}','{theme_id}')"
            )
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing INSERT query: {error}")
    finally:
        connection.close()


def update_theme(update: str):
    """
    save_word_and_translate:
        takes `update` which new name of the selected theme using `theme_id` and renames it.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE Themes SET theme=('{update}') WHERE id=('{theme_id}')"
            )
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing UPDATE query: {error}")
    finally:
        connection.close()


def delete_theme():
    """
    delete_theme:
        removes the theme selected by `theme_id`.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Themes WHERE id=('{theme_id}')")
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing DELETE query: {error}")
    finally:
        connection.close()


def delete_notes():
    """
    delete_theme:
        deletes all notes where id equals `theme_id`.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Notes WHERE themes_id=('{theme_id}')")
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing DELETE query: {error}")
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
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE Notes SET word=('{up_word}'), translate=('{up_translate}') \
                WHERE themes_id=('{theme_id}')AND word=('{old_word}') AND translate=('{old_translate}') "
            )
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing UPDATE query: {error}")
    finally:
        connection.close()


def delete_note(word: str, translate: str):
    """
    delete_note:
        takes the word and translation and removes them from the selected `theme_id`.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"DELETE FROM Notes WHERE themes_id=('{theme_id}') AND\
                            word = ('{word}') AND translate = ('{translate}')"
            )
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing DELETE query: {error}")
    finally:
        connection.close()


def change_save(settings: dict):
    """
    change_save:
        takes the dictionary with the selected settings and updates it in the `Settings` table.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE Settings\
                SET theme=('{settings['theme']}'),\
                verify=({settings['verify']}),\
                repetition=({settings['repetition']}),\
                word=({settings['word']}),\
                translate=({settings['translate']}),\
                randomly=({settings['randomly']}),\
                successively=({settings['successively']}),\
                timer=({settings['timer']})"
            )
            connection.commit()
    except pymysql.Error as error:
        print(f"Error executing UPDATE query: {error}")
    finally:
        connection.close()


def call_settings() -> tuple:
    """
    change_save:
        outputs a tuple with stored values from the `Settings` table.
    """
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Settings")
            settings = tuple(cursor.fetchone().values())
            connection.commit()
            return settings
    except pymysql.Error as error:
        print(f"Error executing UPDATE query: {error}")
    finally:
        connection.close()
