from pymavlink import mavutil

def send_body_ned_velocity(vehicle = None):
    
    if vehicle == None:
        print("Vehicle info unknown, please take over controls.")
    
    #weird behaviers            
    # vehicle._master.mav.set_position_target_local_ned_send(#ned is currently abandoned

    #     0,       # time_boot_ms (not used)

    #     0, 0,    # target system, target component

    #     mavutil.mavlink.MAV_FRAME_BODY_NED,

    #     0b0000111111000111, # type_mask

    #     0, 0, 0, # x, y, z positions (not used)

    #     velocity_x, velocity_y, velocity_z, # m/s

    #     0, 0, 0, # x, y, z acceleration

    #     0, 0)
    
    
    #doesn't move
    # print("banking right")
    # vehicle._master.mav.command_long_send(
    #     1, 1,
    #     mavutil.mavlink.MAV_CMD_NAV_ATTITUDE_TIME,
    #     0,  # confirmation
    #     10,  # roll angle (degrees)
    #     20,  # pitch angle (degrees)
    #     30,  # yaw angle (degrees)
    #     0.5, # thrust (0-1)
    #     0, 0, 0)

        vehicle._master.mav.set_attitude_target_send(
            0,
            0, 0,
            0b11000111, # type_mask
            
        )
