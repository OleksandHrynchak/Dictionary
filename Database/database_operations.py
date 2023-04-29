import pymysql


def connect():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            port=3306,
            database='dictionary_db',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.Error as e:
        print(f"Error executing INSERT query: {e}")


def add_theme(text_value):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO Thems (them) VALUES ('{text_value}')")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing INSERT query: {e}")
    finally:
        connection.close()


def themes_from_db():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Thems")
            list_of_theme = [
                record.get("them") for record in cursor.fetchall()]
            connection.commit()
        return list_of_theme
    except pymysql.Error as e:
        print(f"Error executing SELECT query: {e}")
    finally:
        connection.close()


def id_theme(spinner, theme):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id FROM Thems WHERE them =(%s)", theme)
            global theme_id
            theme_id = cursor.fetchone().get("id")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing SELECT query: {e}")
    finally:
        connection.close()


def save_word_and_translate(word, translate):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO Notes (word,translate,themsid) \
                                VALUES ('{word}','{translate}','{theme_id}')")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing INSERT query: {e}")
    finally:
        connection.close()


def output_notes():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT word, translate \
                                    FROM Notes \
                                    WHERE themsid={theme_id}")
            records = [
                (value.get('word'), value.get('translate'))
                for value in cursor.fetchall()
            ]
            notes = []
            [notes.extend(note) for note in records]
            connection.commit()
            return notes

    except pymysql.Error as e:
        print(f"Error executing SELECT query: {e}")
    finally:
        connection.close()


def update_theme(update):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE Thems SET them=('{update}') WHERE id=('{theme_id}')")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing UPDATE query: {e}")
    finally:
        connection.close()


def delete_theme():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Thems WHERE id=('{theme_id}')")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing UPDATE query: {e}")
    finally:
        connection.close()


def delete_notes():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Notes WHERE themsid=('{theme_id}')")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing UPDATE query: {e}")
    finally:
        connection.close()


def update_note(up_word, up_translate, old_word, old_translate):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"UPDATE Notes SET word=('{up_word}'), translate=('{up_translate}') \
                WHERE themsid=('{theme_id}')AND word=('{old_word}') AND translate=('{old_translate}') ")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing UPDATE query: {e}")
    finally:
        connection.close()


def delete_note(word, translate):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM Notes WHERE themsid=('{theme_id}') AND\
                            word = ('{word}') AND translate = ('{translate}')")
            connection.commit()
    except pymysql.Error as e:
        print(f"Error executing UPDATE query: {e}")
    finally:
        connection.close()
