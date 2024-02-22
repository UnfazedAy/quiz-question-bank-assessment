import logging.config
import MySQLdb as mysql
import os
from config import settings

logger = logging.getLogger(__name__)

def db_is_alive():
    """
    A simple function to check if the database is alive and running
    """
    try:
        # Connect to the database
        conn = mysql.connect(
            host=os.getenv("DB_HOST") or settings.DB_HOST,
            port=int(os.getenv("DB_PORT") or settings.DB_PORT),
            database=os.getenv("DB_NAME") or settings.DB_NAME,
            user=os.getenv("DB_USER") or settings.DB_USER,
            password=os.getenv("DB_PASSWORD") or settings.DB_PASSWORD
        )
        conn.ping(True)
        logger.info("Database is alive and running")
        logger.info(f"Database connected to {os.getenv('DB_NAME') or settings.DB_NAME}")
        conn.close()

    except Exception as e:
        logger.error(f"Error checking database status: {str(e)}")
