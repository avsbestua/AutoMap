from moviepy import VideoFileClip, TextClip, CompositeVideoClip, ImageClip, AudioFileClip


def video_edit(theme: str):
    bg = VideoFileClip('bg.mp4').with_duration(15)
    music = AudioFileClip('evint2.mp3').with_duration(bg.duration)
    bg = bg.with_audio(music)

    text = TextClip(text=theme,
                    font='font.ttf',
                    font_size=30,
                    color='white',
                    stroke_color='black',
                    stroke_width=8,
                    size=(bg.w - 100, None),
                    text_align='center',
                    method='caption',
                    ).with_duration(bg.duration).with_position((50, 60))

    water_mark = TextClip(text="FutureGeo",
                          font='font.ttf',
                          font_size=30,
                          color='#8603a7',
                          size=(bg.w - 100, None),
                          text_align='center',
                          method='caption',
                          ).with_duration(bg.duration).with_position(('center', bg.h - 160)).with_opacity(0.5)

    stars = VideoFileClip('stars.mov', has_mask=True).with_duration(bg.duration).resized(0.2).with_position((140, 10))
    stars.with_position('top', 'center')

    map_img = ImageClip(r'../img.png').with_duration(bg.duration).with_position('center').resized(width=bg.w)

    subscribe = VideoFileClip('sub_button.mov', has_mask=True).with_position((-160, 115)).resized(0.25)

    video = CompositeVideoClip([bg, stars, text, map_img, water_mark, subscribe])

    video.write_videofile('video.mp4', preset='ultrafast', threads=8)


video_edit("Does your country recognize Palestine?")
