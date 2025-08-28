import db


def save_task(task):
    # save task to database
    db.tasks.insert_one(task)
    # return response
    return True

def delete_task(id):
    # delete task from database
    db.tasks.delete_one({"_id": id})
    return True

def get_tasks():
    # get all tasks from database
    all_tasks = db.tasks.find()
    # return response
    return all_tasks

def update_task(id, update):
    # update task in database
    db.tasks.update_one({"_id": id}, {"$set": update})
    return True

