import serial
import time
from logger import *
#from flowsms4 import total_delay_timing
import eurotherm3500_v7
import flowsms7 as fl

tmp = eurotherm3500_v7.Eurotherm3500('COM4', 1)

# Function that stablishes serial communication with all the
# electronically actuated valves
ser1 = 0        
def serial_connection_valves():

  COMPORT = 'COM7'
  global ser1
  ser1 = serial.Serial()
  ser1.baudrate = 9600
  ser1.port = COMPORT #counter for port name starts at 0
  parity=serial.PARITY_NONE
  stopbits=serial.STOPBITS_ONE
  bytesize=serial.EIGHTBITS
  
  if (ser1.isOpen() == False):
    ser1.timeout = 1
    ser1.open()

  else:
    print ('The Port is closed: ' + ser1.portstr)


# Fuction that selects He as carrier gas for the mixing line


def carrier_mix(gas):
  serial_connection_valves()
  
  He = 'A'
  Ar = 'B'
  
  if gas == He:
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != He:
      ser1.write(b'5CW\r')
    else:
      print('Valve moved to position {} to feed He as carrier in mixing line'.format(byteData[-2]))

  elif gas == Ar:
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != Ar:
      ser1.write(b'5CC\r')
    else:
      print('Valve moved to position {} to feed Ar as carrier in mixing line'.format(byteData[-2]))
      
def carrier_pulses(gas):
  serial_connection_valves()
  
  He = 'B'
  Ar = 'A'
  
  if gas == He:
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != He:
      ser1.write(b'4CC\r')
    else:
      print('Valve moved to position {} to feed He as carrier in mixing line'.format(byteData[-2]))

  elif gas == Ar:
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != He:
      ser1.write(b'4CW\r')
    else:
      print('Valve moved to position {} to feed Ar as carrier in mixing line'.format(byteData[-2]))

  
# Fuction that selects 16O2 as oxygen gas source for the mixing line
def feed_16O2():
  serial_connection_valves()
  ser1.write(b'6CW\r')
  print('Feeding 16O2')
  

# Fuction that selects 18O2 as oxygen gas source for the mixing line
def feed_18O2():
  serial_connection_valves()
  ser1.write(b'6CC\r')
  print('Feeding 18O2')
  

# Fuction that selects 12CO2 as carbon dioxide gas source for the mixing line
def feed_12CO2():
  serial_connection_valves()
  ser1.write(b'9CW\r')
  print('Feeding 12CO2')
  

# Fuction that selects 13CO2 as carbon dioxide gas source for the mixing line
def feed_13CO2():
  serial_connection_valves()
  ser1.write(b'9CC\r')
  print('Feeding 13CO2')


# Fuction that selects H2 as hydrogen gas source for the mixing line  
def feed_H2():
  serial_connection_valves()
  ser1.write(b'7CW\r')
  print('Feeding H2')
  
# Fuction that selects D2 as deuterium gas source for the mixing line
def feed_D2():
  serial_connection_valves()
  ser1.write(b'7CC\r')
  print('Feeding D2')
  

# Fuction that selects 12CH4 as methane gas source for the mixing line
def feed_12CH4():
  serial_connection_valves()
  ser1.write(b'8CW\r')
  print('Feeding 12CH4')
  

# Fuction that selects 13CH4 as methane gas source for the mixing line
def feed_13CH4():
  serial_connection_valves()
  ser1.write(b'8CC\r')
  print('Feeding 13CH4')
  

# Fuction that selects the position of Valve 1 (Reaction mode selection module)
def valve1(position):
  serial_connection_valves()
  if position == 'off':
    ser1.write(b'1CW\r')
    print('Mixing line valve position: off (mix -> reactor)')
  elif position == 'on':
    ser1.write(b'1CC\r')
    print('Mixing line valve position: on (mix -> loop)')
    
    
# Fuction that selects the position of Valve 2 (Reaction mode selection module)
def valve2(position):
  serial_connection_valves()
  if position == 'off':
    ser1.write(b'2CW\r')
    print('Water vapor valve position: off (mix -> reactor)')
  elif position == 'on':
    ser1.write(b'2CC\r')
    print('Water vapor valve position: on (mix -> vapor -> reactor)')
    
    
# Fuction that selects the position of Valve 3 (Reaction mode selection module)
def valve3(position):
  serial_connection_valves()
  if position == 'off':
    ser1.write(b'3CW\r')
    print('Pulses line valve position: off (mix -> loop 1 -> waste / carrier -> loop 2 -> reactor)')
  elif position == 'on':
    ser1.write(b'3CC\r')
    print('Pulses line valve position: on (mix -> loop 2 -> waste/ carrier -> loop 1 -> reactor)')
 
 
# Fuction that fix the position of the valves in the reaction mode selection
# module to the continuous mode (dry) mode
def cont_mode_dry():
  serial_connection_valves()
  ser1.write(b'1CW\r')
  ser1.write(b'2CW\r')
  ser1.write(b'3CW\r')
  print('Valves operation mode: continuous mode (dry)')
  print('mix -> reactor ... pulses line carrier -> loops -> waste')
  

# Fuction that fix the position of the valves in the reaction mode selection
# module to the continuous mode (wet) mode
def cont_mode_wet():
  serial_connection_valves()
  ser1.write(b'1CC\r')
  ser1.write(b'2CW\r')
  ser1.write(b'3CW\r')
  print('Valves operation mode: continuous mode (wet)')
  print('mix -> vapor -> reactor ... pulses line carrier -> loops -> waste')
 

# Fuction that fix the position of the valves in the reaction mode selection
# module to the pulses mode 
def pulses_mode():
  serial_connection_valves()
  ser1.write(b'1CC\r')
  ser1.write(b'2CW\r')
  ser1.write(b'3CW\r')
  print('Valves operation mode: pulses')
  print('pulses line carrier -> loop 2 -> reactor ... mix -> loop 1 -> waste')

  
# Fuction that executes a program that injects gas pulses from the loops installed in the
# reaction mode selection module to the reactor.
# Two variables are requested as arguments for the number of pulses to be injected (pulses)
# and the delay time in between pulses (time_bp)
#total_time = []
def send_pulses_loop(pulses,time_bp):
  #total_time_loop = float(pulses) * float(time_bp)
  #total_time.append(total_time_loop)
  # tmp.pulse_ON()
  tmp.pulse_OFF()
  serial_connection_valves()
  ser1.write(b'1CC\r')
  int_pulses = int(pulses)
  float_time = float(time_bp)
  print('Valves operation mode: pulses (dual loop alternation)')
  print('Number of pulses (loop): {}\nTime in between pulses (s): {}'.format(pulses,time_bp))
  print('Valve Position Off: pulses line carrier -> loop 2 -> reactor /// mixing line -> loop 1 -> waste')
  print('Valve Position On: pulses line carrier -> loop 1 -> reactor /// mixing line -> loop 2 -> waste')
  for pulse in range(0, int_pulses):
    tmp.pulse_ON()
    ser1.write(b'3TO\r') # Comand that executes the pulses valve actuation
    print('Sending pulse number {} of {}'.format(pulse+1,int_pulses), end = "\r") # Pulse status message for terminal window
    time.sleep(float_time) # Conversion of seconds to miliseconds
    tmp.pulse_OFF()
  print('Pulses have finished') # End of the pulses message

def send_pulses_loop_IR(pulses):
  #total_time_loop = float(pulses) * float(time_bp)
  #total_time.append(total_time_loop)
  serial_connection_valves()
  ser1.write(b'1CC\r')
  int_pulses = int(pulses)
  print('Valves operation mode: pulses (dual loop alternation)')
  print('Number of pulses (loop): {}'.format(pulses))
  print('Valve Position Off: pulses line carrier -> loop 2 -> reactor /// mixing line -> loop 1 -> waste')
  print('Valve Position On: pulses line carrier -> loop 1 -> reactor /// mixing line -> loop 2 -> waste')
  tmp.IR_STATUS()
  for pulse in range(0, int_pulses):
    ser1.write(b'3TO\r') # Comand that executes the pulses valve actuation
    tmp.IR_ON()
    print('Sending pulse number {} of {}'.format(pulse+1,int_pulses), end = "\r") # Pulse status message for terminal window
    tmp.IR_STATUS()
  print('Pulses have finished') # End of the pulses message
  
# Fuction that executes a program that injects gas pulses produced during the alternation between continuous and
# pulses mode.
# Three variables are requested as arguments for the number of pulses to be injected (pulses), the time the switching valve will
# remain open(time_vo), and the delay time in between pulses (time_bp).
def send_pulses_valve(pulses,time_vo,time_bp):
  #total_time_loop = (float(pulses) * float(time_bp)) + (float(pulses) * float(time_vo))
  #total_time.append(total_time_loop)
  serial_connection_valves()
  valve_actuation_time = 0.145
  ser1.write(b'1CC\r')
  int_pulses = int(pulses) # Preparing the integer input for the loop range
  float_time_vo = float(time_vo) # Preparing the float input for the sleep function vo
  float_time_bp = float(time_bp) # Preparing the float input for the sleep function bp
  print('Valves operation mode: pulses (valve)')
  print('Number of pulses (valve): {}\nTime valve open (s): {}\nTime in between pulses (s): {}'.format(pulses,time_vo,time_bp))
  print('Valve Position Off: mixing line -> reactor /// pulses line carrier -> loop 2 -> loop 1 -> waste')
  print('Valve Position On: pulses line carrier -> reactor /// mixing line -> loop 2 -> loop 1 -> waste')
  for pulse in range(0, int_pulses):
    ser1.write(b'1CW\r') # Comand that executes the pulses valve actuation
    time.sleep(float_time_vo + valve_actuation_time) # Conversion of seconds to miliseconds
    ser1.write(b'1CC\r') # Comand that executes the pulses valve actuation
    print('Sending pulse number {} of {}'.format(pulse+1,int_pulses), end = "\r") # Pulse status message for terminal window
    time.sleep(float_time_bp) # Conversion of seconds to miliseconds
  print('Pulses have finished') # End of the pulses message
  
  
def send_pulses_valve_IR(pulses,time_vo):
  #total_time_loop = (float(pulses) * float(time_bp)) + (float(pulses) * float(time_vo))
  #total_time.append(total_time_loop)
  serial_connection_valves()
  valve_actuation_time = 0.145
  ser1.write(b'1CC\r')
  int_pulses = int(pulses) # Preparing the integer input for the loop range
  float_time_vo = float(time_vo) # Preparing the float input for the sleep function vo
  print('Valves operation mode: pulses (valve)')
  print('Number of pulses (valve): {}\nTime valve open (s): {}\n'.format(pulses,time_vo))
  print('Valve Position Off: mixing line -> reactor /// pulses line carrier -> loop 2 -> loop 1 -> waste')
  print('Valve Position On: pulses line carrier -> reactor /// mixing line -> loop 2 -> loop 1 -> waste')
  tmp.IR_STATUS()
  for pulse in range(0, int_pulses):
    ser1.flush()
    ser1.write(b'1CW\r') # Comand that executes the pulses valve actuation
    tmp.IR_ON()
    time.sleep(float_time_vo + valve_actuation_time) # Conversion of seconds to miliseconds
    ser1.write(b'1CC\r') # Comand that executes the pulses valve actuation
    tmp.IR_STATUS()
    print('Sending pulse number {} of {}'.format(pulse+1,int_pulses), end = "\r") # Pulse status message for terminal window

  print('Pulses have finished') # End of the pulses message
  
  
def send_pulses_valve_ME_IR(pulses,period,gas,flow1,flow2):
  #total_time_loop = (float(pulses) * float(time_bp)) + (float(pulses) * float(time_vo))
  #total_time.append(total_time_loop)
  serial_connection_valves()
  valve_actuation_time = 0.145
  ser1.write(b'1CC\r')
  int_pulses = int(pulses) # Preparing the integer input for the loop range
  float_period = float(period) # Preparing the float input for the sleep function vo
  float_flow1 = float(flow1)
  float_flow2 = float(flow2)
  print('Valves operation mode: pulses (valve)')
  print('Number of pulses (valve): {}\nTime valve open (s): {}\n'.format(pulses,time_vo))
  print('Valve Position Off: mixing line -> reactor /// pulses line carrier -> loop 2 -> loop 1 -> waste')
  print('Valve Position On: pulses line carrier -> reactor /// mixing line -> loop 2 -> loop 1 -> waste')
  tmp.IR_STATUS()
  for pulse in range(0, int_pulses):
    ser1.flush()
    ser1.write(b'1CW\r') # Comand that executes the pulses valve actuation
    tmp.IR_ON()
    time.sleep(float_time_vo + valve_actuation_time) # Conversion of seconds to miliseconds
    ser1.write(b'1CC\r') # Comand that executes the pulses valve actuation
    tmp.IR_STATUS()
    print('Sending pulse number {} of {}'.format(pulse+1,int_pulses), end = "\r") # Pulse status message for terminal window

  print('Pulses have finished') # End of the pulses message


# Fuction that add the experiment time gathered from all the items added in the experiment
#def experiment_time():
  #total_time_sum = (sum(total_time) + total_delay_timing)/60
  #print('Total experiment time in pulses: {} minutes'.format(total_time_sum))