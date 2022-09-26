import eel
import obd
from obd import OBDStatus
from datetime import datetime
# Set web files folder
eel.init('web')

@eel.expose
def vehicle_data():
    # Try to make a connection via ELM327 OBD-II interface
    try:
        connection = obd.OBD(fast=False) # auto-connects to USB or RF port

        vehicle_speed = connection.query(obd.commands.SPEED).value.to("mph") # send the command, and parse the response
        vehicle_rpm = connection.query(obd.commands.RPM).value
        vehicle_fuel = connection.query(obd.commands.FUEL_LEVEL).value

        vehicle_codes = connection.query(obd.commands.DTC_count).value

    # Use default values if failed
    except:
        vehicle_speed = 0
        vehicle_rpm = 0
        vehicle_fuel = 0
        vehicle_codes = 0

        print('Connection failed...')

    return vehicle_speed, vehicle_rpm, vehicle_fuel, vehicle_codes

# Start Eel application on the splashscreen
eel.start('templates/splash.html',
        size=(800, 600),
        jinja_templates='templates')  # Start
