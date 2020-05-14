# -*- coding: utf-8 -*-
"""
This code will try to send commands to the Arduino using the WiFi
allowing for controlled testing of the drive systems.
"""

import time
# This library will allow you to communicate with the Arduino
import socket

# This is the IP address of the Arduino
TCP_IP = '192.168.0.201'
# This is the port the Arduino will reply
TCP_PORT = 25000
# Not very important but needs to be larger than the message you want to send
BUFFER_SIZE = 24

# Create the socket object. The parameters AF_INET and SOCK_STREAM are the ones
# you need to use
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the arduino IP and port
# Feedback to the user via the console to notify connection has been made
s.connect((TCP_IP, TCP_PORT))
print ('Connected to Arduino')

# How many seconds to wait after a button has been pressed.
button_delay = 0.2
 
#Create a loop to continually ask for an input command.
#Hold previous command until the new command is input and overwrite
#Feedback to the user of how the Ball-Bot should react
#Encode the keyboard input into a decimal number
#Send the decimal number to simulink over wifi
# Wait for a bit before you read for a button again
a=1
while (a==1):
 DriveDirection = input("Input Start Command (w=forward, a=left, a=reverse, d=right, p=pause): ")   
 Drive = DriveDirection.encode()
 s.send(Drive)
 print ('Data Sent to Simulink')
 time.sleep(button_delay)
 
# Close the connection to the Arduino
s.close()
# Print a message to the screen
print ('Demonstration Complete')
# Exit the program
exit(0)