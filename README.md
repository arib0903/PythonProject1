# Python Project Servers
A server that shows 3 graphs
-----------------------------
-The application creates a server that gets Covid Vaccine data from the cdc website\
-Uses those datas to make certain graphs(barChart,pieGraph,lineGraph)

# barChart:
Gets the Locations(states) as the x value, and the Percent fully vaccinated as y value\
-Uses **AjaxGetRequest** to handle data being sent from python file to JavaScript file

 
# pieGraph:
Displays the Percent of Vaccine Manufacture Share. Based on (Pfizer,Moderna,Jannsen,Unknown)\
-Uses **AjaxGetRequest** to handle data being sent from python file to JavaScript file


# lineGraph:
Displays the percentage of people fully vaccinated based on the user input (of state)\
-Uses **AjaxPostRequest** to handle data being sent from JavaScript file to python file and then back to JavaScript file





