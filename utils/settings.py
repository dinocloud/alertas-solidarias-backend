import os
class DBSettings:
    DB_ENGINE = "mysql+pymysql"
    DB_HOST = os.getenv("RDS_HOSTNAME", "alertas-solidarias.cilz5xnmiidq.sa-east-1.rds.amazonaws.com")
    DB_PORT = os.getenv("RDS_PORT", "3306")
    DB_NAME = os.getenv("RDS_DB_NAME", "alertas_solidarias")
    DB_USER = os.getenv("RDS_USERNAME", "root")
    DB_PASSWORD = os.getenv("RDS_PASSWORD", "dinocloud")
    SQLALCHEMY_DATABASE_URI = "{0}://{1}:{2}@{3}/{4}".format(DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)