import network
import socket
import time
import random
from machine import Pin


# Relay setup (assuming relay is controlled by GPIO pin 15)
relay = Pin(15, Pin.OUT)
relay.value(0)  # Initialize relay to OFF

# LED setup
led = Pin('LED', Pin.OUT)

# Wi-Fi credentials
ssid = 'hastins'
password = '876543210'


# HTML template (modified for relay control)
def webpage(random_value, relay_state):
    html = f"""
        <!DOCTYPE html>
        <html style="font-family: Helvetica;color: #ffffff; background-color: #284e62; display: inline-block; margin: 50px auto; text-align: center; ">
        <head>
            <title>Pico Web Server</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>Web Server</h1>
            <h2>Relay Control</h2>
            <form action="./relay_on">
                <input type="submit" value="Relay ON" style="background-color: #4CAF50; border-radius: 50px;" />
            </form>
            <br>
            <form action="./relay_off">
                <input type="submit" value="Relay OFF" style="background-color: #FFFF;border-radius: 50px; " />
            </form>
            <p>Relay state: {relay_state}</p>
            <h2> PIN</h2>
            <form action="./value">
                <input type="submit" value="Fetch value" />
            </form>
            <p>Fetched value: {random_value}</p>
        </body>
        </html>
        """
    return str(html)

# Connect to WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for Wi-Fi connection
connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() >= 3:
        break
    connection_timeout -= 1
    print('Waiting for Wi-Fi connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('Failed to establish a network connection')
else:
    print('Connection successful!')
    network_info = wlan.ifconfig()
    print('IP address:', network_info[0])

# Socket setup
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen()

print('Listening on', addr)

# Variables
relay_state = "OFF"
random_value = 0


# Main loop to listen for connections
while True:
    try:
        conn, addr = s.accept()
        print('Got a connection from', addr)
        
        # Receive and parse the request
        request = conn.recv(1024)
        request = str(request)
        print('Request content = %s' % request)

        try:
            request = request.split()[1]
            print('Request:', request)
        except IndexError:
            pass
        
        # Process the request and update variables
        if request == '/relay_on?':
            print("LED on")
            relay.value(1)  # Turn relay ON
            relay_state = "ON"
            led.value(1)
            state = "ON"
        elif request == '/relay_off?':
            relay.value(0)  # Turn relay OFF
            relay_state = 'OFF'
            led.value(0)
            state = 'OFF'
        elif request == '/value?':
            random_value = random.randint(0, 20000)


        response = webpage(random_value, relay_state)

        conn.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        conn.send(response)
        conn.close()

 
    except OSError as e:
        conn.close()
        print('Connection closed')
 
