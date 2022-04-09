from tkinter import *
import requests
import json

root=Tk()
root.overrideredirect(True)
root.title("Country City App")
root.geometry("450x700")

root.configure(background="purple")
#Setting labels
city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="yellow")
city_name_label.place(relx=0.40,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.28,rely=0.30,anchor=CENTER)

weather_info_label = Label(root,text="Country: ", bg="cyan", font=("bold", 10))
weather_info_label.place(relx=0.23,rely=0.5,anchor=CENTER) 

humidity_info_label = Label(root,text="Region: ", bg="cyan", font=( "bold",10)) 
humidity_info_label.place(relx=0.22,rely=0.6,anchor=CENTER) 

language_info_label = Label(root,text="Language: ", bg="cyan", font=( "bold",10)) 
language_info_label.place(relx=0.3,rely=0.7,anchor=CENTER) 

population_info_label = Label(root,text="Population: ", bg="cyan", font=( "bold",10)) 
population_info_label.place(relx=0.22,rely=0.8,anchor=CENTER) 

area_info_label = Label(root,text="Area: ", bg="cyan", font=( "bold",10)) 
area_info_label.place(relx=0.22,rely=0.9,anchor=CENTER) 



def city_name():
   
    api_request = requests.get("https://restcountries.com/v2/capital/" + city_entry.get())
    
    api_output_json = json.loads(api_request.content)
    
    weather_info = api_output_json[0]["name"]
    print(weather_info)
    
    humidity = api_output_json[0]["region"]
    print(str(humidity))
    
    language = api_output_json[0]["languages"]
    print(str(language))
    
    population = api_output_json[0]["population"]
    print(str(population))
    
    area = api_output_json[0]["area"]
    print(str(area))
    
    
    
    weather_info_label["text"] = "Country : " + str(weather_info)
    humidity_info_label["text"] = "Region : " + str(humidity)
    language_info_label["text"] = "Language : " + str(language)
    population_info_label["text"] = "Population : " + str(population)
    area_info_label["text"] = "Area : " + str(area)
    
    city_name_label["text"] = city_entry.get()
    city_entry.destroy()
    search_btn.destroy()
    
search_btn = Button(root, text = "Search Info" ,bg ="green", command = city_name, relief = FLAT)
search_btn.place(relx = 0.5, rely = 0.40, anchor = CENTER)
    
    
    
    
root.mainloop()
