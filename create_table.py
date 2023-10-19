from estd_connection import estd_connection

cursor = estd_connection()

cursor.execute("DROP TABLE IF EXISTS DATAENTRY")

sql = """
CREATE TABLE DATAENTRY (
    TITLE CHAR(20),
    FIRSTNAME CHAR(20),
    LASTNAME CHAR(20),
    AGE INT,
    NATIONALITY CHAR(20),
    NUMBER_OF_COURSES INT,
    NUMBER_OF_SEMESTERS INT,
    REGISTRATION_STATUS CHAR(20)
    )  
"""

cursor.execute(sql)
print("Table Created Successfully !!")
