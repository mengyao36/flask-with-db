import sqlite3

# Connecting to sqlite
# connection object
connect = sqlite3.connect('patients')
 
# db object
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL,
            gender CHAR(25) NOT NULL,
            admissionday CHAR(25) NOT NULL,
            dischargeday CHAR(25) NOT NULL,
            insurance CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() 

## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, admissionday, dischargeday, insurance) values('12345', 'John', 'Smith', '01/01/2000', 'male', '01/01/2022', '01/02/2022', 'Medicare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, admissionday, dischargeday, insurance) values('23456', 'Jane', 'Doe', '02/02/2001', 'fmale', '02/01/2022', '02/02/2022', 'Medicare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, admissionday, dischargeday, insurance) values('34567', 'Mary', 'Smith', '03/03/2002', 'fmale', '03/01/2022', '03/02/2022', 'Medicaid')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, admissionday, dischargeday, insurance) values('45678', 'Bob', 'Smith', '04/04/2003', 'male', '04/01/2022', '04/02/2022', 'Medicare')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob, gender, admissionday, dischargeday, insurance) values('56789', 'Jane', 'Doe', '05/05/2004', 'fmale', '05/01/2022', '05/02/2022', 'Private')")

connect.commit()


# close the connection
connect.close()