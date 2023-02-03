import traceback
from lib.mysql_conn import MySQLConnection
from lib.logger import Logger

class DBStore:
    def __init__(self):
        self.logger = Logger(__name__)
    
    """
    ##############################################

    General Insert Section

    ##############################################
    """

    # Insert new data into area table
    def create_area(self ,area_name, latitude, longitude, prec_no, bloc_no, note='NULL'):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0

        if note is not "NULL":
            note = "'"+note+"'"
        try:
            query = '''
            INSERT INTO area (area_id, area_name, latitude, longitude, prec_no, bloc_no, note, deleted) 
            VALUES (NULL,'%s',%s,%s,%s,%s,%s, 0);
            '''  % (area_name,latitude,longitude,prec_no,bloc_no,note)
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    # Insert new data into weather_set table
    def create_weatherset(self ,weather_type_id, URL_forecasted_data, URL_measured_data):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO weather_set(weather_set_id, weather_type_id, URL_forecasted_data, URL_measured_data) 
            VALUES (NULL,%s,'%s','%s');
            '''% (weather_type_id, URL_forecasted_data, URL_measured_data)
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    # Insert new data into weather_type table
    def create_weathertype(self ,weather_type_name, unit, decimal_places,time_gain):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0

        try:
            query = '''
            INSERT INTO weather_type (weather_type_id, weather_type_name, unit, decimal_places, time_gain) 
            VALUES (NULL,'%s','%s',%s,'%s');
            ''' % (weather_type_name, unit, decimal_places,time_gain)
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    """
    ##############################################

    Update Weather Import Control

    ##############################################
    """
    def update_forecasted_weatherimportcontrol(self, id, next_exec_datetime, last_exec_datetime):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            UPDATE weather_import_control
            SET next_exec_import_forecasted_datetime = '%s', 
            last_exec_import_forecasted_datetime = '%s' 
            WHERE weather_import_control.weather_import_id = %s
            ''' % (next_exec_datetime, last_exec_datetime, id)
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    def update_measured_weatherimportcontrol(self, id, next_exec_datetime, last_exec_datetime):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            UPDATE weather_import_control
            SET next_exec_import_measured_datetime = '%s', 
            last_exec_import_measured_datetime = '%s' 
            WHERE weather_import_control.weather_import_id = %s
            ''' % (next_exec_datetime, last_exec_datetime, id)
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success


    """
    ##############################################

    Weather Forecasted Insert Section

    ##############################################
    """

  #Insert multiple new data in to weather_forecasted_5min table
    def insertblock_weatherforecasted5min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_forecasted_5min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {} ON DUPLICATE KEY UPDATE value = VALUES(value);
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    #Insert multiple new data in to weather_forecasted_10min table
    def insertblock_weatherforecasted10min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_forecasted_10min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {} ON DUPLICATE KEY UPDATE value = VALUES(value);
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success
    
    #Insert multiple new data in to weather_forecasted_15min table
    def insertblock_weatherforecasted15min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_forecasted_15min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {} ON DUPLICATE KEY UPDATE value = VALUES(value);
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success
    
    #Insert multiple new data in to weather_forecasted_30min table
    def insertblock_weatherforecasted30min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_forecasted_30min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {} ON DUPLICATE KEY UPDATE value = VALUES(value);
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success
    
    #Insert multiple new data in to weather_forecasted_60min table
    def insertblock_weatherforecasted60min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_forecasted_60min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {} ON DUPLICATE KEY UPDATE value = VALUES(value);
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    """
    ##############################################

    Weather Measured Insert Section

    ##############################################
    """

    #Insert multiple new data in to weather_measured_5min table
    def insertblock_weathermeasured5min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_measured_5min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {};
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success

    
    #Insert multiple new data in to weather_measured_10min table
    def insertblock_weathermeasured10min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_measured_10min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {};
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success


    #Insert multiple new data in to weather_measured_15min table
    def insertblock_weathermeasured15min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_measured_15min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {};
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success
    
    #Insert multiple new data in to weather_measured_30min table
    def insertblock_weathermeasured30min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_measured_30min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {};
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success
    
    #Insert multiple new data in to weather_measured_60min table
    def insertblock_weathermeasured60min(self, rows):
        conn = MySQLConnection()
        conn.create_db_connection()
        success = 0
        
        try:
            query = '''
            INSERT INTO  weather_measured_60min (area_id, weather_set_id, weather_type_id, datetime, value) 
            VALUES {};
            '''.format(', '.join(map(str, rows)))
            conn.insert_sql(query)
            self.logger.debug(query)
            success = 1
        except Exception as e:
            print(e)
            self.logger.error(traceback.format_exc())
        finally:
            conn.close()
            return success