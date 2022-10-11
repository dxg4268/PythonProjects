"""
YouTube Video Downloader
"""
size = 0

import sys
from pytube import YouTube


def progress_func(chuck, file_handle, bytes_remaining):
    global size
    current = (size - bytes_remaining) / size
    percent = round(current * 100,1)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
     
    # print(round(percent,1),end="\r")


url = input("\n[*] Enter URL for Video => ")
print("\n\t\tAudio and Video both are available in 720p streams")
print("\t\tFor 1080p stream, audio & video are present separately...")
print("\n")
quality = input("[*] Enter quality (default - 360p; upto 720p) => ")

print("\n   Processing...")


def Youtube(url="",quality='360p'):
    try:
        global size
        yt  = YouTube(url, on_progress_callback=progress_func)
    
        streams = list(yt.streams.filter(progressive=True, file_extension='mp4')) 
        title = yt.title
        # print(streams[1])

        print("[+] Video Found !") 
        print(f"[-] Downloading : {title}")


        for stream in streams:
            if f'res="{quality}"' in str(stream):
                # print("\n",stream)
                stream_final = stream
                
        print(f"\tFile Size : ", str(round(((stream_final.filesize)/1024)/1024)), 'MB')
        print()
        size = stream_final.filesize

        # print("[+] Downloading Selected Stream ...")
        path = stream_final.download()
        print("\n\n[+] Video saved to => ", path)
        
        
    except Exception as e:
        print("[!] Error Downloading the video :(")
        
#Start Execution
Youtube(url,quality)        
        
        