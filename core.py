from os.path import exists
from os import mkdir
from pytube import Playlist, YouTube
from re import sub
from wget import download as download_url


def complete(stream, file_path):
    print()


def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining
    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % ('█' * int(size * 20 / contentSize),
          ' ' * (20 - int(size * 20 / contentSize)), float(size / contentSize * 100)), end='')


def download(argv=None):
    if argv[0] == "playlist":
        global video
        # Init
        list = Playlist(f'{argv[1]}')
        channel = sub(r'[\/?:*"><|]', "", list.owner)
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
                download_url(
                    thumbnail, f'./{channel}/{target}/image/{img_name}.jpg')
            except:
                print(f'\n{yt.title} download failed!', end='\n')
            else:
                print(f'\n{yt.title} download complete.', end='\n')

    elif argv[0] == "video":
        # Init
        target = "UnknowCategory"
        url = argv[1]
        yt = YouTube(
            url,
            on_progress_callback=progress,
            # on_complete_callback=complete,
        )
        channel = sub(r'[\/?:*"><|]', "", yt.author)
        video = yt.streams.get_highest_resolution()
        thumbnail = yt.thumbnail_url
        img_name = sub(r'[\/?:*"><|]', "", yt.title)

        # file_size
        file_size = video.filesize

        # Download
        try:
            print(f"Downloading {yt.title}...", end='\n')
            video.download(f'./{target}/{channel}/video')
            print("")
            if not exists(f'{target}/{channel}/image'):
                mkdir(f'{target}/{channel}/image')
            download_url(
                thumbnail, f'./{target}/{channel}/image/{img_name}.jpg')
        except Exception as e:
            print(e)
            print(f'\n{yt.title} download failed!', end='\n')
        else:
            print(f'\n{yt.title} download complete.', end='\n')


def download_cli():
    arg1= input("MODE:")
    arg2= input("URL:")
    if arg1 == "playlist":
        global video
        # Init
        list = Playlist(f'{arg2}')
        channel = sub(r'[\/?:*"><|]', "", list.owner)
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
                download_url(
                    thumbnail, f'./{channel}/{target}/image/{img_name}.jpg')
            except:
                print(f'\n{yt.title} download failed!', end='\n')
            else:
                print(f'\n{yt.title} download complete.', end='\n')

    elif arg1 == "video":
        # Init
        target = "UnknowCategory"
        url = arg2
        yt = YouTube(
            url,
            on_progress_callback=progress,
            # on_complete_callback=complete,
        )
        channel = sub(r'[\/?:*"><|]', "", yt.author)
        video = yt.streams.get_highest_resolution()
        thumbnail = yt.thumbnail_url
        img_name = sub(r'[\/?:*"><|]', "", yt.title)

        # file_size
        file_size = video.filesize

        # Download
        try:
            print(f"Downloading {yt.title}...", end='\n')
            video.download(f'./{target}/{channel}/video')
            print("")
            if not exists(f'{target}/{channel}/image'):
                mkdir(f'{target}/{channel}/image')
            download_url(
                thumbnail, f'./{target}/{channel}/image/{img_name}.jpg')
        except Exception as e:
            print(e)
            print(f'\n{yt.title} download failed!', end='\n')
        else:
            print(f'\n{yt.title} download complete.', end='\n')

#download_cli()