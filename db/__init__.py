import json
file = open("db/data.json") 
data = json.load(file)
file.close()

def add_data(new_data):
    global data
        
    data.append(new_data)
    
    with open('db/data.json','w',encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
    
    with open('db/data.json','r',encoding="utf-8") as file:
        data = json.load(file)
        
def delete_data(id: int):
        global data
        
        movies = [movie for movie in data if movie['id'] != id]
        
        with open('db/data.json','w',encoding="utf-8") as file:
            json.dump(movies,file,indent=4,ensure_ascii=False)
        
        with open('db/data.json','r',encoding="utf-8") as file:
            data = json.load(file)
        
def update_data(id: int, new_data: dict):
    global data
    
    movie_index = next((index for index,movie in enumerate(data) if movie['id'] == id), None)
    
    if movie_index is not None:
        data[movie_index].update(new_data)
    
    with open('db/data.json','w',encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
        
    with open('db/data.json','r',encoding="utf-8") as file:
        data = json.load(file)