import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="online_exam",
        use_pure = True
    )

def ensure_schema_updates():
    """Apply small backwards-compatible schema updates required by the app."""
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = DATABASE()
              AND TABLE_NAME = 'results'
              AND COLUMN_NAME = 'is_published'
            """
        )
        exists = cursor.fetchone()[0]
        if not exists:
            cursor.execute(
                "ALTER TABLE results ADD COLUMN is_published BOOLEAN NOT NULL DEFAULT FALSE"
            )
            connection.commit()
    finally:
        cursor.close()
        connection.close()
