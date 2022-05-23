from VideoStore import VideoStore

# demo
if __name__ =="__main__":
    video_store = VideoStore("resources/video_store.xml")
    print('#'*20, 'show all data', '#'*20)
    video_store.print_all_genres()
    print('#'*20, ' adding', '#'*20)
    video_store.add_film(2, 3, "hollywood", 23, "tarantino")
    video_store.add_genre(3, "comedy")
    video_store.print_all_genres()
    print('#' * 20, ' search', '#' * 20)
    video_store.print_genre(1)
    print("-----------films by duration 20-85 minutes -----------")
    video_store.print_films_by_range(20, 85)
    print('#' * 20, ' change', '#' * 20)
    video_store.change_film(4, "once in Hollywood", 27, "tarantino")
    print('#' * 20, ' deleting', '#' * 20)
    video_store.remove_film(3)
    video_store.remove_genre(3)
    video_store.print_all_genres()


