# from dotenv import load_dotenv
# import os
# import mysql.connector # pip install mysql-connector-python

# load_dotenv()

# mydb = mysql.connector.connect(
#     host= os.getenv("DB_HOST"),
#     user=os.getenv("DB_USERNAME"),
#     passwd= os.getenv("DB_PASSWORD"),
#     db= os.getenv("DB_NAME"),
#     autocommit = True
#     # ,ssl_mode = "VERIFY_IDENTITY",
#     # ssl      = {
#     #   "ca": "/etc/ssl/cert.pem"
#     # }
#     )

# def query(query:str, display:bool=False, num:int=0):
    
#     mycursor = mydb.cursor()

#     mycursor.execute(query)

#     if display == True:
#         myresult = mycursor.fetchall()

#         if num == 0:
#             for x in myresult:
#                 print(x)
#         elif num > 0:
#             c = 1
#             for x in myresult:
#                 c += 1
#                 if c <= num:
#                     print(x)
#                 elif c > num:
#                     break

# def create_municipios(drop_table: bool = False):

#     mycursor = mydb.cursor()

#     if drop_table == True: 
#         mycursor.execute("DROP TABLE IF EXISTS municipios;")

#     mycursor.execute("CREATE TABLE IF NOT EXISTS municipios (id_code INT PRIMARY KEY, municipio VARCHAR(255))")


# def create_estabelecimentos(drop_table: bool = False):
#     mycursor = mydb.cursor()

#     if drop_table == True: 
#         mycursor.execute("DROP TABLE IF EXISTS estabelecimentos;")

#     mycursor.execute("""
#                 CREATE TABLE IF NOT EXISTS estabelecimentos (
#                 CNPJ_BAS VARCHAR(255),
#                 CNPJ_ORDEM VARCHAR(255),
#                 CNPJ_DV VARCHAR(255),
#                 MATRIZ VARCHAR(255),
#                 NOME_F VARCHAR(255),
#                 SIT_CAD VARCHAR(255),
#                 DATA_SIT_CAD VARCHAR(255),
#                 MOT_SIT_CAD VARCHAR(255),
#                 NOME_CID_EXT VARCHAR(255),
#                 PAIS VARCHAR(255),
#                 DAcreate_all_TA_INICIO_ATV VARCHAR(255),
#                 CNAE_PRINC VARCHAR(255),
#                 CNAE_SEC VARCHAR(255),
#                 TIPO_LOGR VARCHAR(255),
#                 LOGRADOURO VARCHAR(255),
#                 NUM VARCHAR(255),
#                 COMPL VARCHAR(255),
#                 BAIRRO VARCHAR(255),
#                 CEP VARCHAR(255),
#                 UF VARCHAR(255),
#                 MUNIC VARCHAR(255),
#                 DDD_1 VARCHAR(255),
#                 TEL_1 VARCHAR(255),
#                 DDD_2 VARCHAR(255),
#                 TEL_2 VARCHAR(255),
#                 DDD_FAX VARCHAR(255),
#                 FAX1 VARCHAR(255),
#                 EMAIL VARCHAR(255),
#                 SIT_ESP VARCHAR(255),
#                 DATA_SIT_ESP VARCHAR(255),
#                 id INT AUTO_INCREMENT PRIMARY KEY
#                 )
#             """)

# def create_tables(drop_table: bool = False):
#     create_municipios(drop_table)
#     create_estabelecimentos(drop_table)


# mycursor = mydb.cursor()
# mycursor.execute(f"""
# COPY company.Municipios(id_code, municipio) FROM 'D:/Github/pb-dev-code-track/cnae-extractor/data/MUNICIPIOS.csv' WITH DELIMITER ';' QUOTE E'\042' ESCAPE E'\b';
# """)
    

# # mycursor.execute(f"""
# # mysqlimport --local -u {keys.db_user} -p --fields-terminated-by=';' --lines-terminated-by='\n' --ignore-lines=1 {keys.db_name} /data/MUNICIPIOS.csv
# # """)

# # mycursor.execute("""
# # SET GLOBAL local_infile = true;
# # """)

# # def teste():
# #     mycursor = mydb.cursor()

# #     mycursor.execute("""
# #   LOAD DATA INFILE 'D:/Github/pb-dev-code-track/cnae-extractor/data/MUNICIPIOS.csv'
# #   INTO TABLE municipios
# #   FIELDS TERMINATED BY ';'
# #   LINES TERMINATED BY '\n'
# #   (id_code, municipio);
# # """)

# # mycursor.execute("""
# # select * from municipios;
# # """)

# # myresult = mycursor.fetchall()

# # for x in myresult:
# #   print(x)

# mkdir -p $env:appdata\postgresql\; Invoke-WebRequest -Uri https://cockroachlabs.cloud/clusters/fb1c74f6-b23d-4bb3-83ca-ab1173f530fc/cert -OutFile $env:appdata\postgresql\root.crt

import os
from sqlalchemy import create_engine, text

engine = create_engine(os.getenv("DATABASE_URL"))
conn = engine.connect()

res = conn.execute(text("SELECT now()")).fetchall()
print(res)