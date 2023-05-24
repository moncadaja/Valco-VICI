import serial
import time

#from logger import *
#from flowsms4 import total_delay_timing
#import eurotherm3500_v7
#import flowsms7 as fl

#tmp = eurotherm3500_v7.Eurotherm3500('COM4', 1)

# Function that stablishes serial communication with all the
# electronically actuated valves
ser1 = 0        
def serial_connection_valves():

  COMPORT = 'COM6'
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

#Function that displays available commands list
def commands_list():
  serial_connection_valves()
  commands = ser1.write(b'?\r')
  
  # Define a buffer to store the data
  buffer = []

  # Read data from the serial port until you receive a complete set of lines
  while True:
    data = ser1.readline().decode().strip()  # Read a line of data and decode it
    if not data:  # If no data is received, break the loop
      break
    buffer.append(data)  # Add the received line to the buffer  
  
  # Split each item at '\r' character to create separate lines
  lines = [item.split('\r') for item in buffer]
  print(lines)

  # Flatten the list of lines into a single list
  lines = [line for sublist in lines for line in sublist]
  print(lines)

  # Combine the lines with newline character '\n'
  output = '\n'.join(lines)

  # Print the output
  print(output)
  
#Function that displays the current position
def valve_current_position():
  serial_connection_valves()
  current_position = ser1.write(b'CP\r')
  byteData = ser1.readline().decode()
  print('Valve current position: {}'.format(byteData[-2]))
  
#Function that displays the number of positions of the selector valve
def valve_total_positions():
  serial_connection_valves()
  total_positions = ser1.write(b'NP\r')
  byteData = ser1.readline().decode()
  print('Valve total available positions: {}'.format(byteData[-2]))

#Function that selects the port position of a 6 port selector valve
def valve_set_port_number(direction,number):  
  serial_connection_valves()
  int_number = int(number)
  str_direction = str(direction)
  
  if int_number == 1 and str_direction == 'clockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CC01\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
  elif int_number == 1 and str_direction == 'anticlockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CW01\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
    
  if int_number == 2 and str_direction == 'clockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CC02\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
  elif int_number == 2 and str_direction == 'anticlockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CW02\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))

  if int_number == 3 and str_direction == 'clockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CC03\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
  elif int_number == 3 and str_direction == 'anticlockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CW03\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))

  if int_number == 4 and str_direction == 'clockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CC04\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
  elif int_number == 4 and str_direction == 'anticlockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CW04\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))

  if int_number == 5 and str_direction == 'clockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CC05\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
  elif int_number == 5 and str_direction == 'anticlockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CW05\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))

  if int_number == 6 and str_direction == 'clockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CC06\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))
  elif int_number == 6 and str_direction == 'anticlockwise':
    position = ser1.write(b'CP\r')
    byteData = ser1.readline().decode()
    if int(byteData[-2]) != int_number:
      ser1.write(b'CW06\r')
    else:
      print('Valve moved to position {} in {} direction'.format(byteData[-2],str_direction))

def send_pulses_valve(pulses,time_vo,time_bp):
  serial_connection_valves()
  #valve_actuation_time = 0.145
  ser1.write(b'1CC02\r')
  int_pulses = int(pulses) # Preparing the integer input for the loop range
  float_time_vo = float(time_vo) # Preparing the float input for the sleep function vo
  float_time_bp = float(time_bp) # Preparing the float input for the sleep function bp
  print('Valves operation mode: pulses (valve)')
  print('Number of pulses (valve): {}\nTime valve open (s): {}\nTime in between pulses (s): {}'.format(pulses,time_vo,time_bp))
  print('Valve Position Off: mixing line -> reactor /// pulses line carrier -> loop 2 -> loop 1 -> waste')
  print('Valve Position On: pulses line carrier -> reactor /// mixing line -> loop 2 -> loop 1 -> waste')
  for pulse in range(0, int_pulses):
    ser1.write(b'1CW\r') # Comand that executes the pulses valve actuation
    time.sleep(float_time_vo) # Conversion of seconds to miliseconds
    ser1.write(b'1CC\r') # Comand that executes the pulses valve actuation
    print('Sending pulse number {} of {}'.format(pulse+1,int_pulses), end = "\r") # Pulse status message for terminal window
    time.sleep(float_time_bp) # Conversion of seconds to miliseconds
  print('Pulses have finished') # End of the pulses message
