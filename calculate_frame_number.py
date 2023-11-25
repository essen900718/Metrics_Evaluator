import argparse
from moviepy.editor import VideoFileClip

def main(args):

    # Load the video clip
    video_clip = VideoFileClip(args.video_path)

    # Get the total number of frames
    total_frames = int(video_clip.fps * video_clip.duration)

    # Print the total number of frames
    print(f'The video has {total_frames} frames.')

    # Close the video clip object
    video_clip.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--video_path',     type=str, default="./vids/Obama_groundtruth.mp4")

    args = parser.parse_args()
    main(args)