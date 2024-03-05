import json

file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            print(data)
            return data
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(file_name, "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    if len(videos) == 0:
        print("\n Not any videos exist!")
        return
    
    print("\n")
    print("*" * 70)
    
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video["name"]}, Duration: {video["time"]}")

    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        print(videos)
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid video number selected!")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
    else:
        print("Invalid video number selected")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()