from bottle import request, HTTPResponse
import json
import random

EXTRAORDINARY_WOMEN = [
        {"id": 1, "name": "Boudica", "origin": "Iceni", "occupation": "Warrior"},
        {"id": 2, "name": "María La Judía", "origin": "Egypt", "occupation": "Alchemist"},
        {"id": 3, "name": "Hypatia", "origin": "Alexandria", "occupation": "Philosopher"},
        {"id": 4, "name": "Jeanne D'Arc", "origin": "France", "occupation": "Heroine"},
        {"id": 5, "name": "Isabel La Católica", "origin": "Castilla y Aragón", "occupation": "Queen"},
        {"id": 6, "name": "Francesca Caccini", "origin": "Italy", "occupation": "Singer"},
        {"id": 7, "name": "La Roldana", "origin": "Spain", "occupation": "Sculptor"},
        {"id": 8, "name": "Carolina Herschel", "origin": "Germany", "occupation": "Astronomer"},
        {"id": 9, "name": "Jane Austen", "origin": "England", "occupation": "Writer"},
        {"id": 10, "name": "Sophie Gremain", "origin": "France", "occupation": "Mathematician"},
        {"id": 11, "name": "Sacajawea", "origin": "Idaho", "occupation": "Explorer"},
        {"id": 12, "name": "Ada Lovelace", "origin": "English", "occupation": "Programmer"},
        {"id": 13, "name": "Florence Nightingale", "origin": "English", "occupation": "Nurse"},
        {"id": 14, "name": "Sarah Bernhardt", "origin": "France", "occupation": "Actress"},
        {"id": 15, "name": "Ginko Ogino", "origin": "Japan", "occupation": "Doctor"},
        {"id": 16, "name": "Calamity Jane", "origin": "United States", "occupation": "Cowgirl"},
        {"id": 17, "name": "Marie Curie", "origin": "Poland/France", "occupation": "Chemist"},
        {"id": 18, "name": "Hellen Keller", "origin": "United States", "occupation": "Political Activist"},
        {"id": 19, "name": "Clara Campoamor", "origin": "Spain", "occupation": "Politician"},
        {"id": 20, "name": "Amelia Earhart", "origin": "United States", "occupation": "Aviator"},
        {"id": 21, "name": "Josephine Baker", "origin": "United States", "occupation": "Dancer"},
        {"id": 22, "name": "Frida Kahlo", "origin": "Mexico", "occupation": "Painter"},
        {"id": 23, "name": "Irena Sendler", "origin": "Poland", "occupation": "Nurse"},
        {"id": 24, "name": "Teresa de Calcuta", "origin": "Macedonia", "occupation": "Missionary"},
        {"id": 25, "name": "Hedy Lamarr", "origin": "Austria", "occupation": "Actress/Inventor"},
        {"id": 26, "name": "Maria Callas", "origin": "United States", "occupation": "Opera Singer"},
        {"id": 27, "name": "Dian Fossey", "origin": "United States", "occupation": "Zoologist"},
        {"id": 28, "name": "Valentina Tereshkova", "origin": "Russia", "occupation": "Cosmonaut"},
        {"id": 29, "name": "Benazir Bhutto", "origin": "Pakistan", "occupation": "Prime Minister"},
        {"id": 30, "name": "Nadia Comaneci", "origin": "Romania", "occupation": "Gymnast"}
]



def list_women():
    return HTTPResponse(
            status=200,
            body=json.dumps({"extraordinary_women": EXTRAORDINARY_WOMEN}))


def add_woman():
    new_woman = {}
    try:
        max_id_woman = max(EXTRAORDINARY_WOMEN, key=lambda x:x['id'])
        max_id = max_id_woman['id'] + 1
        data = request.json
        new_woman = {
            "id": max_id,
            "name": data['name'],
            "origin": data['origin'],
            "occupation": data['occupation']
        }
        EXTRAORDINARY_WOMEN.append(new_woman)
        return HTTPResponse(
                status=200,
                body=json.dumps({"extraordinary_woman": new_woman}))
    except:
        return HTTPResponse(
                status=400,
                body=json.dumps({'error': 'error adding a woman'}))




def get_woman(woman_id):
    for woman in EXTRAORDINARY_WOMEN:
        if woman['id'] == int(woman_id):
            return HTTPResponse(
                status=200,
                body=json.dumps({'extraordinary_woman': woman}))
    else:
        return HTTPResponse(
            status=404,
            body=json.dumps({'error': 'id not found'}))


def delete_woman(woman_id):
    for woman in EXTRAORDINARY_WOMEN:
        if woman['id'] == int(woman_id):
            EXTRAORDINARY_WOMEN.remove(woman)
            return HTTPResponse(status=204)
    else:
        return HTTPResponse(
            status=204,
            body=json.dumps({'error': 'id not found'}))
