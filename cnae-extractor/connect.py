from dotenv import load_dotenv
import os
import mysql.connector # pip install mysql-connector-python

load_dotenv()

class Connect:
    
    def __init__(self) -> None:

        self.mydb = mysql.connector.connect(
            host= os.getenv("DB_HOST"),
            user=os.getenv("DB_USERNAME"),
            passwd= os.getenv("DB_PASSWORD"),
            db= os.getenv("DB_NAME"),
            autocommit = True
            # ,ssl_mode = "VERIFY_IDENTITY",
            # ssl      = {
            #   "ca": "/etc/ssl/cert.pem"
            # }
            )

    def create_municipios(self, drop_table: bool = False):

        mycursor = self.mydb.cursor()

        if drop_table == True: 
            mycursor.execute("DROP TABLE IF EXISTS municipios;")

        mycursor.execute("CREATE TABLE IF NOT EXISTS municipios (id_code INT PRIMARY KEY, municipio VARCHAR(255))")
        
        mycursor.execute("""
        select * from municipios;
        """)

        return print('Tabela criada')

    def create_estabelecimentos(self):
        mycursor = self.mydb.cursor()

        mycursor.execute("DROP TABLE IF EXISTS estabelecimentos;")

        mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS estabelecimentos (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  CNPJ_BAS VARCHAR(255),
                  CNPJ_ORDEM VARCHAR(255),
                  CNPJ_DV VARCHAR(255),
                  MATRIZ VARCHAR(255),
                  NOME_F VARCHAR(255),
                  SIT_CAD VARCHAR(255),
                  DATA_SIT_CAD VARCHAR(255),
                  MOT_SIT_CAD VARCHAR(255),
                  NOME_CID_EXT VARCHAR(255),
                  PAIS VARCHAR(255),
                  DATA_INICIO_ATV VARCHAR(255),
                  CNAE_PRINC VARCHAR(255),
                  CNAE_SEC VARCHAR(255),
                  TIPO_LOGR VARCHAR(255),
                  LOGRADOURO VARCHAR(255),
                  NUM VARCHAR(255),
                  COMPL VARCHAR(255),
                  BAIRRO VARCHAR(255),
                  CEP VARCHAR(255),
                  UF VARCHAR(255),
                  MUNIC VARCHAR(255),
                  DDD_1 VARCHAR(255),
                  TEL_1 VARCHAR(255),
                  DDD_2 VARCHAR(255),
                  TEL_2 VARCHAR(255),
                  DDD_FAX VARCHAR(255),
                  FAX1 VARCHAR(255),
                  EMAIL VARCHAR(255),
                  SIT_ESP VARCHAR(255),
                  DATA_SIT_ESP VARCHAR(255)
                 )
                 """)



# mycursor.execute(f"""
# mysqlimport --local -u {keys.db_user} -p --fields-terminated-by=';' --lines-terminated-by='\n' --ignore-lines=1 {keys.db_name} /data/MUNICIPIOS.csv
# """)

# mycursor.execute("""
# SET GLOBAL local_infile = true;
# """)


# mycursor.execute("""
#   LOAD DATA INFILE 'D:/Github/pb-dev-code-track/cnae-extractor/data/MUNICIPIOS.csv'
#   INTO TABLE municipios
#   FIELDS TERMINATED BY ';'
#   LINES TERMINATED BY '\n'
#   (id_code, municipio);
# """)

# mycursor.execute("""
# select * from municipios;
# """)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)