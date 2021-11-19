# import ffmpeg
from os.path import basename, dirname, exists
from os import mkdir
from pytube import Playlist, YouTube
from re import sub
from sys import argv
from wget import download


def complete(stream, file_path):
    print()


def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining
    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size * 20 / contentSize), ' ' * (20 - int(size * 20 / contentSize)), float(size / contentSize * 100)), end='')


if __name__ == "__main__":
    if argv[1] == "playlist":
        # Init
        list = Playlist(f'{argv[2]}')
        channel = list.owner
        if not exists(f'./{channel}'):
            mkdir(channel)
        target = list.title
        for movies in list.video_urls:
            url = movies
            yt = YouTube(
                url,
                on_progress_callback=progress,
                # on_complete_callback=complete,
            )
            video = yt.streams.get_highest_resolution()
            thumbnail = yt.thumbnail_url
            img_name = sub(r'[\/?:*"><|]', "", yt.title)

            # file_size
            file_size = video.filesize

            # Download
            try:
                print(f"Downloading {yt.title}...", end='\n')
                video.download(f'./{channel}/{target}/video')
                print("")
                if not exists(f'{channel}/{target}/image'):
                    mkdir(f'{channel}/{target}/image')
                download(thumbnail, f'./{channel}/{target}/image/{img_name}.jpg')
            except:
                print(f'\n{yt.title} download failed!', end='\n')
            else:
                print(f'\n{yt.title} download complete.', end='\n')

    elif argv[1] == "video":
        # Init
        target = "UnknowCategory"
        url = argv[2]
        yt = YouTube(
            url,
            on_progress_callback=progress,
            # on_complete_callback=complete,
        )
        video = yt.streams.get_highest_resolution()
        thumbnail = yt.thumbnail_url
        img_name = sub(r'[\/?:*"><|]', "", yt.title)

        # file_size
        file_size = video.filesize

        # Download
        try:
            print(f"Downloading {yt.title}...", end='\n')
            video.download(f'./{target}/video')
            print("")
            if not exists(f'{target}/image'):
                mkdir(f'{target}/image')
            download(thumbnail, f'./{target}/image/{img_name}.jpg')
        except:
            print(f'\n{yt.title} download failed!', end='\n')
        else:
            print(f'\n{yt.title} download complete.', end='\n')
