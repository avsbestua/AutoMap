# from moviepy import VideoFileClip
# import os
#
# video = VideoFileClip("sub_button.mp4")
# os.makedirs("frames", exist_ok=True)
#
# for i, frame in enumerate(video.iter_frames(fps=video.fps, dtype='uint8')):
#     from PIL import Image
#     img = Image.fromarray(frame)
#     img.save(f"frames/frame_{i:04d}.png")

# from PIL import Image
# import os
#
# frame_files = sorted(os.listdir("frames"))
# os.mkdir('frames_alpha')
# for file in frame_files:
#     img = Image.open(f"frames/{file}").convert("RGBA")
#     datas = img.getdata()
#
#     newData = []
#     for item in datas:
#         # Якщо чорний піксель, робимо прозорим
#         if item[0] == 0 and item[1] == 254 and item[2] == 0:
#             newData.append((0, 0, 0, 0))
#         else:
#             newData.append(item)
#
#     img.putdata(newData)
#     img.save(f"frames_alpha/{file}")

from moviepy import ImageSequenceClip
import os

frame_files = sorted(os.listdir("frames_alpha"))
frame_paths = [os.path.join("frames_alpha", f) for f in frame_files]

# fps беремо, наприклад, 30, або той, що був у оригінальному відео
clip = ImageSequenceClip(frame_paths, fps=60)

# Зберігаємо відео з альфа-каналом (mov + png codec підтримує прозорість)
clip.write_videofile("sub_button.mov", codec="png", fps=60)

