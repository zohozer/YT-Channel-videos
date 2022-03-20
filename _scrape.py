import scrapetube
import sys

path = '_list.txt'

print('**********************\n')
print("The result will be saved in '_list.txt' file.")
print("Enter Channel ID:")

# Prints the output in the console and into the '_list.txt' file.
class Logger:
 
    def __init__(self, filename):
        self.console = sys.stdout
        self.file = open(filename, 'w')
 
    def write(self, message):
        self.console.write(message)
        self.file.write(message)
 
    def flush(self):
        self.console.flush()
        self.file.flush()

sys.stdout = Logger(path)

# Strip the: "https://www.youtube.com/channel/"
channel_id_input = input()
channel_id = channel_id_input.strip("https://www.youtube.com/channel/")

videos = scrapetube.get_channel(channel_id)

for video in videos:
    print("https://www.youtube.com/watch?v="+str(video['videoId']))
#    print(video['videoId'])