from app.util.json_util import read_json, write_json

FOOD_DATA = read_json("data/food_data.json")

class FoodRepository():
    def get_foods(self):
        return FOOD_DATA
    
    def search_food(self, name, category):
        result = []
        for data in FOOD_DATA:
            if name:
                if data["name"] == name:
                    result.append(data)
            if category:
                if data["category"] == category:
                    result.append(data)

        result = sorted(result, key= lambda x:x["name"])
        return result