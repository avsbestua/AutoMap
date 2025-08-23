from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, ImageClip
from moviepy import vfx
from PIL import Image, ImageDraw
import numpy as np

def make_circle_mask(size):
    img = Image.new("L", size, 0)
    draw = ImageDraw.Draw(img)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    return np.array(img) / 255.0

def video_edit(theme: str):
    bg = VideoFileClip('bg.mp4').with_duration(15)

    music = AudioFileClip('music.mp3').with_duration(15)

    text = TextClip(text=theme,
                    font= r'./font_video.ttf',
                    font_size=100,
                    size=(bg.w - 100, None),
                    method='caption',
                    color='white',
                    stroke_color='black',
                    stroke_width=10,
                    text_align='center'
                    ).with_duration(bg.duration).with_position((35, 50))

    text = text.with_effects([vfx.FadeIn(3)])

    map_img = ImageClip(r'../img.png').with_position('center').with_duration(bg.duration)
    map_img = map_img.resized(height=bg.w)
    map_img = map_img.with_effects([vfx.FadeIn(1)])

    pfp = ImageClip(r'./pfp.png').with_position((35, bg.h - 260)).with_duration(bg.duration).resized(height=200).with_effects([vfx.FadeIn(2)])

    mask_array = make_circle_mask((pfp.w, pfp.h))
    mask_clip = ImageClip(mask_array, is_mask=True).with_duration(bg.duration)
    pfp = pfp.with_mask(mask_clip)

    pfp_text = TextClip(text="Uranian Guy",
                    font= r'./font_video.ttf',
                    font_size=150,
                    size=(bg.w - 100, None),
                    method='caption',
                    color='#7AD2D7',
                    stroke_color='black',
                    stroke_width=10,
                    text_align='center'
                    ).with_duration(bg.duration).with_position((130, bg.h - 240)).with_effects([vfx.FadeIn(2)])

    video = CompositeVideoClip([bg, text, map_img, pfp, pfp_text])
    video = video.with_audio(music)
    video.write_videofile(f'{theme[:-1]}.mp4', codec='h264_nvenc')

video_edit("When your country first joined the UN?")