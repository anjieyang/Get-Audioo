import os
import subprocess
from config import DIRECTORY_PATH


def extract_audio_with_ffmpeg(video_path, output_path):
    try:
        command = ['ffmpeg', '-i', video_path, '-q:a',
                   '0', '-map', 'a', output_path, '-y']
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Extracted audio saved as {output_path}")
    except Exception as e:
        print(f"Failed to extract audio from {video_path}: {e}")


def save_audios_from_directory_ffmpeg(directory_path):
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.mp4')):
            video_path = os.path.join(directory_path, filename)
            audio_path = os.path.join(
                directory_path, f"{os.path.splitext(filename)[0]}.mp3")
            extract_audio_with_ffmpeg(video_path, audio_path)


if __name__ == "__main__":
    save_audios_from_directory_ffmpeg(DIRECTORY_PATH)
