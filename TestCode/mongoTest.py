# mongoTest.py
#python "/home/lenovo/projects/PredictiveMaintainance/TestCode/mongoTest.py"

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.PM
    return db
    
def get_model_data(db):
    return db.ModelRunHistory.find()

def insert_data(db,model_name,model_accuracy):
    db.ModelRunHistory.insert({"Model" : model_name, "Acurracy" : model_accuracy})

if __name__ == "__main__":
    db = get_db() 
    insert_data(db,"DT",60)
    print get_model_data(db)
