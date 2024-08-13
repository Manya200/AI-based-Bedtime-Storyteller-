from moviepy.editor import VideoFileClip

# Replace 'video.mp4' with the path to your video file
video_path = 'New project.mp4'

# Load the video clip
clip = VideoFileClip(video_path)

# Preview the video
clip.preview()

# Close the video preview window after playback
clip.close()
