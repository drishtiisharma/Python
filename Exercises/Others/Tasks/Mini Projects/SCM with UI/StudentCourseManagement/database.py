import mysql.connector

try:
    def get_connection():
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "scm_ui",
            use_pure = True
        )

        return connection

    connection = get_connection()

    print("Database connected successfully!")

    connection.close()
    
except mysql.connector.Error as e:
    print("connection could not be successfully established")
    print("error:", e)
