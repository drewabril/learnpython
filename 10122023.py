from win11toast import toast

print("Hello World!")

#echo = input("I am a Parrot\n")

#toast("🐍")


buttons = [
    {'activationType': 'protocol', 'arguments': 'C:\Windows\Media\Alarm01.wav', 'content': 'Play'},
    {'activationType': 'protocol', 'arguments': 'file:///C:/Windows/Media', 'content': 'Open Folder'}
]

toast('Music Player', 'Download Finished', buttons=buttons)