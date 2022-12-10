from modules.bboard import getchart
from modules.youtube_search import search_video_id
from time import sleep

def main():
    source_id_list = []
    for song in getchart():
        source_id_list.append(search_video_id(song))
    print(source_id_list)

if __name__ == "__main__":
    main()

