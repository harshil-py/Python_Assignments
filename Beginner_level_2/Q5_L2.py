"""
5. You are developing a program that analyzes weather data. 
Write a Python function that takes a list of temperature readings for a specific location and
determines the average temperature, highest temperature, and lowest temperature. 
Input: temperature_readings = [25, 28, 21, 24, 27] 
Output: Average Temperature: 25.0 
Highest Temperature: 28 
Lowest Temperature: 21
"""
temprature_readings = [25, 28, 21, 24, 27] 
def weather_analysis(temprature_readings):
    avg = sum(temprature_readings)/len(temprature_readings) 
    maximum = max(temprature_readings)
    minimum = min(temprature_readings)
    return f"Average Temperature: {avg} \nHighest Temperature: {maximum} \nLowest Temperature: {minimum}"

print(weather_analysis(temprature_readings))