import os
import subprocess
from config import DIRECTORY_PATH
from tqdm import tqdm


def extract_audio_with_ffmpeg(video_path, output_path):
    try:
        command = [
            'ffmpeg', '-i', video_path, '-q:a', '0',
            '-ar', '16000', '-map', 'a', output_path, '-y'
        ]
        process = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            print(f"Error extracting audio: {process.stderr.decode()}")
        else:
            print(f"Extracted audio saved as {output_path}")
    except Exception as e:
        print(f"Failed to extract audio from {video_path}: {e}")


def convert_video_fps(video_path, output_path):
    try:
        command = ['ffmpeg', '-i', video_path, '-r', '24', '-y', output_path]
        process = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if process.returncode != 0:
            print(f"Error converting video: {process.stderr.decode()}")
        else:
            print(f"Video converted and saved as {output_path}")
            os.remove(video_path)
            print(f"Original video {video_path} removed after conversion.")
        return output_path
    except Exception as e:
        print(f"Failed to convert video {video_path} to 24 fps: {e}")


def process_videos_from_directory_ffmpeg(directory_path):
    files = [f for f in os.listdir(
        directory_path) if f.lower().endswith('.mp4')]
    for filename in tqdm(files, desc="Processing videos"):
        video_path = os.path.join(directory_path, filename)
        audio_path = os.path.join(
            directory_path, f"{os.path.splitext(filename)[0]}.mp3")
        converted_video_path = os.path.join(
            directory_path, f"{os.path.splitext(filename)[0]}_convert.mp4")
        extract_audio_with_ffmpeg(video_path, audio_path)
        convert_video_fps(video_path, converted_video_path)


if __name__ == "__main__":
    process_videos_from_directory_ffmpeg(DIRECTORY_PATH)
