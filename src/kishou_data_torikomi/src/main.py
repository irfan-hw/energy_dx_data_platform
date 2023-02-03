# import pandas as pd
from lib.db_store import DBStore
from lib.db_func import DBFunction
from lib.logger import Logger
from lib.weather_import_control import WeatherImportControl
import schedule,time

def measured_data_import_schedule(controller:WeatherImportControl):
    controller.measured_data_import_control()

def forecasted_data_import_schedule(controller:WeatherImportControl):
    controller.forecasted_data_import_control()


def main():
    # Scheduling service
    for id in weather_import_control_id_list:
        
        weather_import_control = WeatherImportControl(weather_import_id=id)
        init_success = weather_import_control.get_init_success()

        if(init_success):
            # Immediately run for the first time
            measured_data_import_schedule(controller=weather_import_control)
            forecasted_data_import_schedule(controller=weather_import_control)

            # Schedule measured data import
            measured_import_interval = weather_import_control.get_interval_import_measured_data()
            schedule.every(measured_import_interval).minutes.do(
                    measured_data_import_schedule, 
                    controller=weather_import_control
                )
            # Schedule forecast data import
            # forecasted_data_import_interval = weather_import_control.get_interval_import_forecasted_data()
            # schedule.every(forecasted_data_import_interval).minutes.do(
            #         forecasted_data_import_schedule, 
            #         controller=weather_import_control
            #     )

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    logger = Logger(__name__)
    
    weather_import_control_id_list = [1]
    main()
