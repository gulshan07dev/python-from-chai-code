import sqlite3

conn = sqlite3.connect("youtube_videos.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()

    if(len(rows) == 0):
        print("\n Empty videos \n")
        return
    
    print("\n")
    print("*" * 80)

    for row in rows:
        print(row)

    print("*" * 80)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))

def main():
    while True:
        print("\n Youtube Manager with Db")
        print("1. List videos")
        print("2. Add video")
        print("3. update video")
        print("4. delete video")
        print("5. exit app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == "3":
            list_videos()
            video_id = input("Enter video id to update: ")
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video time: ")
            update_video(video_id, new_name, new_time)
        elif choice == "4":
            list_videos()
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice")
    
    conn.close()

if __name__ == "__main__":
    main()
