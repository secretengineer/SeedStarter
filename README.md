# SeedStarter
Environmental controller for seed-starting rack using Raspberry Pi


This code is designed to automate the operation of a seedling heat mat and greenhouse lighting system. It reads data from a light sensor, a temperature sensor, and the weather API. The script then turns on the heat mat and lighting based on the collected data.

Here is a step-by-step breakdown of the code:

Import necessary libraries.
Define pin numbers for the light sensor, seedling heat mat, and greenhouse light.
Set up the GPIO pins using the RPi.GPIO library.
Define temperature and light thresholds.
Set the URL for the weather API.
Next, the script defines two functions: is_dark() and check_temperature().

is_dark() uses the weather API to determine if it is dark outside. It fetches the sunset time and compares it with the current time. If the current time is later than the sunset time, the function returns True, indicating that it is dark outside.
check_temperature() uses the Raspberry Pi IP address to get temperature data from a web service. It compares the received temperature with the temperature threshold. If the temperature is above the threshold, the function returns True.
The monitor() function continuously checks the temperature, light level, and whether it is dark outside. Based on these checks, it turns on the seedling heat mat and greenhouse lighting system.

The monitor() function runs in an infinite loop, with each iteration sleeping for 10 seconds. This delay helps reduce the CPU load.

To start the script, the monitor() function is called at the end of the script.