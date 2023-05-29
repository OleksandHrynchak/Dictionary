import pymysql


try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="dictionary_db",
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with connection.cursor() as cursor:
            create_table_themes = (
                "CREATE TABLE Themes ("
                "id INT(11) NOT NULL AUTO_INCREMENT,"
                "theme VARCHAR(50) NOT NULL,"
                "PRIMARY KEY (id)"
                ");"
            )
        cursor.execute(create_table_themes)
        with connection.cursor() as cursor:
            create_table_notes = (
                "CREATE TABLE Notes("
                "id INT(11) NOT NULL AUTO_INCREMENT,"
                "word VARCHAR(30) NOT NULL,"
                "translate VARCHAR(30) NOT NULL,"
                "themesid INT(11),"
                "PRIMARY KEY (id),"
                "FOREIGN KEY (themesid) REFERENCES Themes(id) "
                ");"
            )
        cursor.execute(create_table_notes)
        with connection.cursor() as cursor:
            create_table_save_settings = (
                "CREATE TABLE Settings ("
                "id INT(11) NOT NULL AUTO_INCREMENT,"
                "theme VARCHAR(50),"
                "verify BOOLEAN,"
                "repetition BOOLEAN,"
                "word BOOLEAN,"
                "translate BOOLEAN,"
                "randomly BOOLEAN,"
                "successively BOOLEAN,"
                "timer INT,"
                "PRIMARY KEY (id)"
                ");"
            )
        cursor.execute(create_table_save_settings)
        with connection.cursor() as cursor:
            main_save = (
                "INSERT INTO Settings ("
                "theme, "
                "verify,"
                "repetition,"
                "word,"
                "translate,"
                "randomly,"
                "successively,"
                "timer)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )
            values = ("List of themes", True, False, True, False, True, False, 5)
            cursor.execute(main_save, values)
            connection.commit()
            connection.commit()

    finally:
        connection.close()

except pymysql.Error as error:
    print(f"Error executing CREATE query: {error}")
