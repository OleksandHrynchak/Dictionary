import pymysql


try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        port=3306,
        database='dictionary_db',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            create_table_thems = "CREATE TABLE Thems (" \
                "id int(11) NOT NULL AUTO_INCREMENT," \
                "them varchar(50) NOT NULL," \
                "PRIMARY KEY (id)" \
                ");"

            create_table_notes = "CREATE TABLE Notes("\
                "id int(11) NOT NULL AUTO_INCREMENT,"\
                "word varchar(30) NOT NULL,"\
                "translate varchar(30) NOT NULL,"\
                "themsid int(11),"\
                "PRIMARY KEY (id),"\
                "FOREIGN KEY (themsid) REFERENCES Thems(id) "\
                ") ;"

            cursor.execute(create_table_thems, create_table_notes)

            connection.commit()

    finally:
        connection.close()


except pymysql.Error as e:
    print(f"Error executing INSERT query: {e}")
