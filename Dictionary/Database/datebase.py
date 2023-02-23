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

    print("seccessfully connected...")

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

            print("tabel created")

    finally:
        connection.close()


except Exception as ex:
    print("Conection refused...")
    print(ex)
