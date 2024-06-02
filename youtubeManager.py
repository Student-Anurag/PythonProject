import json

def load_data():
    try:
        with open('youtube.txt','r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_helper(videos):
    with open('youtube.txt','w') as f:
        json.dump(videos,f)
def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']} ")

def add_videos(videos):
    name = input("Enter video name: ")
    time =input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    idx = int(input("Enter the video number to update: "))
    if 1 <= idx <= len(videos):
        name = input("Enter the new video name ")
        time = input("Enter the new video time ")
        videos[idx-1] = {'name':name, 'time':time}
        save_helper(videos)
    else:
        print("Invalid index selected!!!")

def delete_videos(videos):
    list_all_videos(videos)
    idx = int(input("Enter the video number to be delted "))
    if 1<=idx<=len(videos):
        del videos[idx-1]
        save_helper(videos)
    else:
        print("Invalid video index selected!")

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")
        print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice!!!")
if __name__ == "__main__":
    main()