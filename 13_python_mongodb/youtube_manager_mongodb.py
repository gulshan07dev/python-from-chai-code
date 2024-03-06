from pymongo import MongoClient
from bson import ObjectId

username = ""
password = ""
MONGO_URI = f"mongodb+srv://{username}:{password}@cluster0.rmacq3q.mongodb.net/"

# Not a good idea to include id and password in code files

client = None

try:
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client["ytmanager"]
    video_collection = db["videos"]
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {str(e)}")


def list_videos():
    videos = list(video_collection.find({}))
    print("\n")

    if not videos:
        print("No videos found!")
        return
    
    for video in videos:
        print(f"Id: {video['_id']}, name: {video['name']} and Duration: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({
        "name": name,
        "time": time
    })

def update_video(video_id, new_name, new_time):
    video = video_collection.find_one({"_id": ObjectId(video_id)})
    
    if not video:
        print("\n Invalid video id!")
    
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video = video_collection.find_one({"_id": ObjectId(video_id)})
    
    if not video:
        print("\n Invalid video id!")
    
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager with Mongodb | choose option")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. exit app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case "3":
                list_videos()
                video_id = input("Enter video id to update: ")
                new_name = input("Enter new video name: ")
                new_time = input("Enter new video time: ")
                update_video(video_id, new_name, new_time)
            case "4":
                video_id = input("Enter video id to delete: ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()
