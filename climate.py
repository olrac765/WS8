import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("climate.db")

cursor = connection.cursor()
cursor.execute("SELECT Year from ClimateData")
years = cursor.fetchall()

cursor = connection.cursor()
cursor.execute("SELECT Co2 from ClimateData")
co2 = cursor.fetchall()

cursor = connection.cursor()
cursor.execute("SELECT Temperature from ClimateData")
temp = cursor.fetchall()


years = years
co2 = co2
temp = temp



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 
plt.show()