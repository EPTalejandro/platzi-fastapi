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
        
# def update_data(id: int, new_data: dict):
#     global data
#     
#     movie = [movie for movie in data if movie['id'] == id]
#     
#     movie[0] = {
#     "title": new_data['title'],
#     "overview": new_data['overview'],
#     "year": new_data['year'],
#     "rating": new_data['rating'],
#     "category": new_data['category']  
#                 }
#     
#     data[0]['id'].update(new_data)
#     
#     with open('db/data.json','w',encoding="utf-8") as file:
#             json.dump(data,file,indent=4,ensure_ascii=False)
#         
#     with open('db/data.json','r',encoding="utf-8") as file:
#         data = json.load(file)