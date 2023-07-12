from pymavlink import mavutil

def send_body_ned_velocity(velocity_x, velocity_y, velocity_z, vehicle = None):
    
    if vehicle == None:
        print("Vehicle info unknown, please take over controls.")
    
# #    weird behaviers      
    vehicle._master.mav.set_position_target_local_ned_send(

        0,       # time_boot_ms (not used)

        0, 0,    # target system, target component

        mavutil.mavlink.MAV_FRAME_BODY_NED,

        0b0000001111000111, # type_mask

        0, 0, 0, # x, y, z positions (not used)

        velocity_x, velocity_y, velocity_z, # m/s

        0, 0, 0, # x, y, z acceleration

        0, 0)
    
