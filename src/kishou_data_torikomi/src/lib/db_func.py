import traceback
from lib.mysql_conn import MySQLConnection
from lib.logger import Logger

class DBFunction:
    def __init__(self):
        self.logger = Logger(__name__)

    def find_weatherset(self, weather_set_id):
        conn = MySQLConnection()
        conn.create_db_connection()
        records = []
        success=0
        
        try:
            query = '''
            SELECT * FROM weather_set WHERE weather_set_id=%s;
            ''' % (weather_set_id)
            records = conn.get_sql(query)
            if len(records)>0:
                records = records[0]
                success=1
        except:
            print('weather_set Data id=%s not found' %  weather_set_id)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return records, success
    
    def find_area(self, area_id):
        conn = MySQLConnection()
        conn.create_db_connection()
        records = []
        success=0

        try:
            query = '''
                SELECT * FROM area WHERE area_id=%s;
                ''' % (area_id)
            records = conn.get_sql(query)
            if len(records)>0:
                records = records[0]
                success=1
        except:
            print('area Data id=%s not found' % area_id)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return records, success

    def find_weathertype(self, weather_type_id):
        conn = MySQLConnection()
        conn.create_db_connection()
        records = []
        success=0

        try:
            query = '''
                SELECT * FROM weather_type WHERE weather_type_id=%s;
                ''' % (weather_type_id)
            records = conn.get_sql(query)
            if len(records)>0:
                records = records[0]
                success=1
        except:
            print('weather_type Data id=%s not found' % weather_type_id)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return records, success
        
    def find_weatherimportcontrol(self, weather_import_id):
        conn = MySQLConnection()
        conn.create_db_connection()
        records = []
        success=0
        
        try:
            query = '''
                SELECT * FROM weather_import_control WHERE weather_import_id=%s;
                ''' % (weather_import_id)
            records = conn.get_sql(query)
            if len(records)>0:
                records = records[0]
                success=1
        except:
            print('weather_import Data id=%s not found' % weather_import_id)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return records, success

    def find_weatherset_weathertypelist(self, weather_set_id):
        conn = MySQLConnection()
        conn.create_db_connection()
        records = []
        success=0
        
        try:
            query = '''
                SELECT 
                weather_type.weather_type_id, 
                weather_type.weather_type_name, 
                weather_type.unit, 
                weather_type.decimal_places
                FROM weather_set_pivot RIGHT JOIN weather_type 
                ON weather_set_pivot.weather_type_id=weather_type.weather_type_id 
                WHERE weather_set_id=%s;
                ''' % (weather_set_id)
            records = conn.get_sql(query)
            if len(records)>0:
                success=1
        except:
            print('weatherset_weathertypelist Data id=%s not found' % weather_set_id)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return records, success

        