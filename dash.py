import eel
import obd
from obd import OBDStatus
from datetime import datetime
# Set web files folder
eel.init('web')

@eel.expose
def vehicle_data():
    vehicle_dict = {}
    # Try to make a connection via ELM327 OBD-II interface
    try:
        connection = obd.OBD(fast=False) # auto-connects to USB or RF port

        vehicle_dict['vehicle_speed'] = connection.query(obd.commands.SPEED).value.to("mph") # send the command, and parse the response
        vehicle_dict['vehicle_rpm'] = connection.query(obd.commands.RPM).value
        vehicle_dict['vehicle_fuel'] = connection.query(obd.commands.FUEL_LEVEL).value
        vehicle_dict['vehicle_codes'] = connection.query(obd.commands.DTC_count).value
        vehicle_dict['vehicle_voltage'] = connection.query(obd.commands.ELM_VOLTAGE).value
        vehicle_dict['vehicle_coolant'] = connection.query(obd.commands.COOLANT_TEMP).value

    # Use default values if failed
    except:
        vehicle_dict['vehicle_speed'] = 0
        vehicle_dict['vehicle_rpm'] = 800
        vehicle_dict['vehicle_fuel'] = 100
        vehicle_dict['vehicle_codes'] = 0
        vehicle_dict['vehicle_voltage'] = 12.8
        vehicle_dict['vehicle_coolant'] = 200

        print('Connection failed...')

    return vehicle_dict

# Start Eel application on the splashscreen
eel.start('templates/splash.html',
        size=(800, 600),
        jinja_templates='templates')  # Point to templates folder for Jinja templating
