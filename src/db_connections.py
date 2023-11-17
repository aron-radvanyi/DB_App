# database.py

import configparser
import mysql.connector

def get_db_connection():
    configuration = configparser.ConfigParser()
    configuration.read("settings/config.ini")

    connection = mysql.connector.connect(
        host=configuration["Database"]["host"],
        port=configuration["Database"]["port"],
        user=configuration["Database"]["user"],
        password=configuration["Database"]["password"],
        database=configuration["Database"]["database"]
    )

    return connection
