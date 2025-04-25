# Raspberry-Pi-Pico-W-Web-Server-with-Relay-Control
This is a well-structured MicroPython script for a web server on a Raspberry Pi Pico W that controls a relay and displays a random value!
This project demonstrates a simple web server running on a Raspberry Pi Pico W that allows users to control a relay and fetch a random numerical value through a web browser.

## Overview

This repository contains the MicroPython code for an embedded web server on the Raspberry Pi Pico W. The server provides a basic HTML interface with the following functionalities:

* **Relay Control:** Buttons to turn a connected relay ON and OFF. The current state of the relay is displayed on the webpage.
* **Random Value Fetch:** A button to generate and display a random integer between 0 and 20000.

## Hardware Requirements

* Raspberry Pi Pico W
* Relay module (compatible with 3.3V logic)
* LED (optional, for visual indication)
* Jumper wires for connections

## Software Requirements

* MicroPython firmware flashed onto the Raspberry Pi Pico W.
* Necessary libraries (`network`, `socket`, `time`, `random`, `machine`) are part of the standard MicroPython distribution for the Pico W.

## Wiring

Connect the relay control pin to GPIO pin 15 on the Raspberry Pi Pico W. If you are using an LED, connect it to the onboard 'LED' pin. Ensure your relay module is properly powered and isolated.

**Important:** Exercise caution when working with electrical circuits and relays. Ensure proper wiring and voltage levels.

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone [repository URL]
    cd [repository name]
    ```
    (Replace `[repository URL]` and `[repository name]` with your repository details.)

2.  **Connect to Wi-Fi:**
    Modify the `ssid` and `password` variables in the `main.py` file with your Wi-Fi network credentials.

    ```python
    ssid = 'YOUR_WIFI_SSID'
    password = 'YOUR_WIFI_PASSWORD'
    ```

3.  **Upload the Code:**
    Use a tool like `rshell` or Thonny to upload the `main.py` file to your Raspberry Pi Pico W.

## Usage

1.  **Power up the Raspberry Pi Pico W.**
2.  **Wait for the Pico W to connect to your Wi-Fi network.** The script will print the IP address of the Pico W to the serial console once the connection is successful.
3.  **Open a web browser on a device connected to the same Wi-Fi network.**
4.  **Enter the IP address of your Raspberry Pi Pico W in the browser's address bar.**
5.  You will see the web interface with buttons to control the relay and fetch a random value.

## Code Explanation

* **`network`:** Used for establishing a Wi-Fi connection.
* **`socket`:** Used for creating and managing the web server socket.
* **`time`:** Used for introducing delays during the Wi-Fi connection process.
* **`random`:** Used for generating the random numerical value.
* **`machine.Pin`:** Used for configuring and controlling the GPIO pin connected to the relay and the onboard LED.
* **`webpage(random_value, relay_state)`:** This function generates the HTML content for the web page, dynamically including the current relay state and the fetched random value.
* The main loop listens for incoming web requests. It parses the requested URL to determine the action (relay ON, relay OFF, or fetch value) and updates the relay state and the random value accordingly. It then sends an HTTP response containing the updated webpage.

## Contributing

Contributions to this project are welcome. Feel free to fork the repository and submit pull requests with improvements or bug fixes.

## License
MIT License

Copyright (c) [2025] [Hastings Mumo ]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

