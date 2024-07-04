import mysql.connector
from datetime import datetime

def update_database(txt1, txt2):
  user='staffwizardmysqladmin'
  pwd='b5&8$smb7$J9BMKK'
  host='azmysql-staff-wizard-prd-01.mysql.database.azure.com'
  db='mysql'
  
  cnx = mysql.connector.connect(user=user, 
                              password=pwd,
                              host=host,
                              database=db)
  
  cursor = cnx.cursor()
  date=str(datetime.now())
  query = f"INSERT INTO StaffwizzardLog(Date_Time, Assistant, User)\
  VALUES('{date}', '{txt1}', '{txt2}')"
  cursor.execute(query)
  cnx.commit()
  
  cursor.close()
  cnx.close()
