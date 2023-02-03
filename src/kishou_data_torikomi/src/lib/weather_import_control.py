
from lib.db_store import DBStore
from lib.db_func import DBFunction
from lib.logger import Logger
from lib.web_scraping import jma_scraping_10min_a1,jma_scraping_hourly_a1,jma_scraping_10min_s1,jma_scraping_hourly_s1
import config.kccs_config as APIConfig
from datetime import datetime, date, timedelta
import ssl, traceback, requests

ssl._create_default_https_context = ssl._create_unverified_context

class WeatherImportControl:
    '''
        weather_import
        [0] id
        [1] area_id 
        [2] weather_set_id
        [3] interval_import_measured_data	
        [4] interval_import_forecasted_data	
        [5] next_exec_import_measured_datetime
        [6] next_exec_import_forecasted_datetime
        [7] last_exec_import_measured_datetime
        [8] last_exec_import_forecasted_datetime
        [9] active
        [10] deleted
    '''

    def __init__(self,weather_import_id):
        self.logger = Logger(__name__)
        db_func = DBFunction()
        self.init_success=0

        # Find weather import
        self.weather_import, weather_import_success = db_func.find_weatherimportcontrol(weather_import_id)

        if(weather_import_success):
            self.area, area_success = db_func.find_area(self.weather_import[1])
            self.weather_set, weather_set_success = db_func.find_weatherset(self.weather_import[2])
            
            if(weather_set_success):
                self.weather_type, weather_type_success = db_func.find_weatherset_weathertypelist(self.weather_import[2])

        if(not weather_import_success or not weather_set_success or not area_success or not weather_type_success):
            print("%s Weather Import Control id=%s initialization failed"%(datetime.today().strftime('%Y-%m-%d %H:%M') ,weather_import_id))
            self.logger.error("---------------- Weather Import Control id=%s initialization failed"%(weather_import_id))
        else:
            self.init_success=1
            self.logger.info("---------------- Weather Import Control id=%s initialization success"%(weather_import_id))

    '''
        ##############################################

        Get Function

        ##############################################
    '''
    def get_id(self):
        return self.weather_import[0]

    def get_interval_import_measured_data(self):
        return self.weather_import[3]
    
    def get_interval_import_forecasted_data(self):
        return self.weather_import[4]
    
    def get_next_exec_import_measured_datetime(self):
        return self.weather_import[5]
    
    def get_next_exec_import_forecasted_datetime(self):
        return self.weather_import[6]
    
    def get_last_exec_import_measured_datetime(self):
        return self.weather_import[7]
    
    def get_last_exec_import_forecasted_datetime(self):
        return self.weather_import[8]

    def get_init_success(self):
        return self.init_success

    '''
        ##############################################

        Update Class Variable Function

        ##############################################
    '''

    def update_self_variable(self):
        db_func = DBFunction()
        temp, weather_import_success = db_func.find_weatherimportcontrol(self.get_id())
        if (weather_import_success):
            self.weather_import = temp
        else:
            self.logger.error('update_weather_import_variable id=%s failed.'%self.get_id())

    '''
        ##############################################

        Scheduling Function

        ##############################################
    '''
    def measured_data_import_control(self):
        curr_time =datetime.now()
        success=0

        if(curr_time > self.get_next_exec_import_measured_datetime()):
            self.logger.info("---------------- measured_data_import id=%s task running." % self.get_id())

            retry_attempt = 0
            while(retry_attempt<3 and not success):
                try:
                    success = self.import_block_measured_data(
                        date_time= date.today()-timedelta(days=1)
                    )
                except:
                    self.logger.error(traceback.format_exc())
                retry_attempt += 1

            if(success):                
                print("%s Import Measured Task id=%s completed" % (datetime.today().strftime('%Y-%m-%d %H:%M'),self.get_id()))
                self.logger.info("---------------- measured_data_import id=%s task completed." % self.get_id())
            else:
                print("%s Import Measured Task id=%s failed" % (datetime.today().strftime('%Y-%m-%d %H:%M'),self.get_id()))  
                self.logger.info("---------------- measured_data_import id=%s task failed." % self.get_id())
            
            db_store = DBStore() 
            db_store.update_measured_weatherimportcontrol(
                id = self.get_id(), 
                next_exec_datetime = (curr_time+timedelta(minutes=self.get_interval_import_measured_data())), 
                last_exec_datetime = datetime.now()
            )
            self.update_self_variable()


    def forecasted_data_import_control(self):
        curr_time =datetime.now()
        success=0

        if(curr_time > self.get_next_exec_import_forecasted_datetime()):
            self.logger.info("---------------- forecasted_data_import id=%s task running." % self.get_id())

            retry_attempt = 0
            while(retry_attempt<3 and not success):
                try:
                    success = self.import_block_forecasted_data()
                except:
                    self.logger.error(traceback.format_exc())
                retry_attempt += 1

            if(success):                
                print("%s Import Forecasted Task id=%s completed" % (datetime.today().strftime('%Y-%m-%d %H:%M'),self.get_id()))
                self.logger.info("---------------- forecasted_data_import id=%s task completed." % self.get_id())
            else:
                print("%s Import Forecasted Task id=%s failed" % (datetime.today().strftime('%Y-%m-%d %H:%M'),self.get_id()))  
                self.logger.info("---------------- forecasted_data_import id=%s task failed." % self.get_id())
            
            db_store = DBStore() 
            db_store.update_forecasted_weatherimportcontrol(
                id = self.get_id(), 
                next_exec_datetime = (curr_time+timedelta(minutes=self.get_interval_import_forecasted_data())), 
                last_exec_datetime = datetime.now()
            )
            self.update_self_variable()

    '''
        ##############################################

        Import Function

        ##############################################
    '''
    def import_block_forecasted_data(self):
        success = 0
        db_store = DBStore()

        request_parameter_code = {
            '気温':'temperature',
            '湿度':'humidity',
            '降水量':'apcp_surface',
            '風速':'wind_velocity',
            '風向':'wind_direction',
            '日射量':'solar_radiation'
        }
        json_response_code = {
            '気温':'temperature',
            '湿度':'humidity',
            '降水量':'apcp_surface',
            '風速':'wind_velocity',
            '風向':'wind_direction_angle',
            '日射量':'solar_radiation'
            
        }

        forecasts_target = []
        for weather_type_elm in self.weather_type:
            forecasts_target.append(request_parameter_code[weather_type_elm[1]])

        # send request
        url = '%s?place=%s' % (self.weather_set[1], self.area[2])
        url += '&forecasts={}'.format(','.join(map(str, forecasts_target)))

        response = requests.get(url, auth=(APIConfig.ACCESS_KEY_ID, APIConfig.SECRET_ACCESS_KEY))
        
        # get response
        result = response.json()

        if(response.status_code == 200):
            # parse and input to database
            data = []
            for item in result['forecasts']:
                for weather_type_elm in self.weather_type:
                    data.append((
                        self.area[0],
                        self.weather_set[0],
                        weather_type_elm[0], 
                        item['time'],
                        item[json_response_code[weather_type_elm[1]]]
                    ))

            time_gain = self.weather_set[3]
            
            if(time_gain=="5min"):
                success=db_store.insertblock_weatherforecasted5min(data)
            elif(time_gain=="10min"):
                success=db_store.insertblock_weatherforecasted10min(data)
            elif(time_gain=="15min"):
                success=db_store.insertblock_weatherforecasted15min(data)
            elif(time_gain=="30min"):
                success=db_store.insertblock_weatherforecasted30min(data)
            elif(time_gain=="60min"):
                success=db_store.insertblock_weatherforecasted60min(data)
        else:
            self.logger.error('%s %s - %s'%(response.status_code,response.reason,response.reason))
            
        return success

    def datetime_join(self, date:datetime, time):
        if(time=='24:00'):
            tomorrow = date +timedelta(days=1)
            return datetime(
                tomorrow.year,
                tomorrow.month,
                tomorrow.day,
                0,
                0
            ).strftime("%Y/%m/%d %H:%M")
        else:
            return datetime(
                date.year,
                date.month,
                date.day,
                int(time.split(':')[0]),
                int(time.split(':')[1])
            ).strftime("%Y/%m/%d %H:%M")
    
    # area : 場所の名前
    # weather_set : URL アクセス
    # weather_type : （例 気温、湿度
    # datetime : 年月日 　（注意：時間がいらない)
    def import_block_measured_data(self, date_time:datetime):
        success = 0
        db_store = DBStore()
        year = date_time.strftime("%Y")
        month = date_time.strftime("%m")
        day = date_time.strftime("%d")

        url = " %s?prec_no=%s&block_no=%s&year=%s&month=%s&day=%s" % \
            (self.weather_set[2],self.area[3],self.area[4],year,month,day)
        
        webpage_type = self.weather_set[2].split('/')[-1].split('.')[0]
        
        if(webpage_type == '10min_a1'):
            result = jma_scraping_10min_a1(url)
            weather_type_dict = {
                '気温':2,
                '湿度':3,
                '降水量':1,
                '風速':4,
                '風向':5,
                '日射量':8
            }
        elif(webpage_type == 'hourly_a1'):
            result = jma_scraping_hourly_a1(url)
            weather_type_dict = {
                '気温':2,
                '湿度':5,
                '降水量':1,
                '風速':6,
                '風向':7,
                '日射量':8
            }
        elif(webpage_type == '10min_s1'):
            result = jma_scraping_10min_s1(url)
            weather_type_dict = {
                '気温':4,
                '湿度':5,
                '降水量':3,
                '風速':6,
                '風向':7,
                '日射量':10
            }
        elif(webpage_type == 'hourly_s1'):
            result = jma_scraping_hourly_s1(url)
            weather_type_dict = {
                '気温':4,
                '湿度':7,
                '降水量':3,
                '風速':8,
                '風向':9,
                '日射量':11
            }
        else:
            self.logger.error("Invalid webpage")
            print("Invalid webpage")
            return success
        
        data = []
        for item in result:
            for weather_type_elm in self.weather_type:
                data.append((
                    self.area[0],
                    self.weather_set[0],
                    weather_type_elm[0], 
                    self.datetime_join(date_time,item[0]),
                    item[weather_type_dict[weather_type_elm[1]]]
                ))

        time_gain = self.weather_set[3]
        
        if(time_gain=="5min"):
            success=db_store.insertblock_weathermeasured5min(data)
        elif(time_gain=="10min"):
            success=db_store.insertblock_weathermeasured10min(data)
        elif(time_gain=="15min"):
            success=db_store.insertblock_weathermeasured15min(data)
        elif(time_gain=="30min"):
            success=db_store.insertblock_weathermeasured30min(data)
        elif(time_gain=="60min"):
            success=db_store.insertblock_weathermeasured60min(data)
          
        return success
