from pytube import YouTube

url = input("Enter the Youtube URL: ")

yt = YouTube(url)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("C:/Users/ACER/Pictures/Screenshots")

print("Dowload complete") 