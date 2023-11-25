import argparse
import subprocess

def main(args):

    args.fps = 25
    start_time = args.start_frame / 25
    end_time = args.end_frame / 25
    print(start_time)

    command = [
        "ffmpeg",
        "-ss", str(start_time),
        "-t", str(end_time),
        "-i", args.input_file,      
        "-c:v", "libx264", 
        "-c:a", "aac",           
        args.output_file           
    ]

    try:
        subprocess.run(command, check=True)
        print("Success !")
    except subprocess.CalledProcessError as e:
        print("Failed !", e)

if __name__ == '__main__':

    """
    cut the video by timestamp with only given fps and frame index
    there are total (end_frame-start_frame) extracted frames
    end_frame+1 to extract index end_frame included
    """
    
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--fps',            type=int,  default=25,     help="frame per second")
    parser.add_argument('--start_frame',    type=int,    default=0)
    parser.add_argument('--end_frame',      type=int,  default=300) 
    parser.add_argument('--input_file',     type=str, default="./vids/Obama_groundtruth.mp4")
    parser.add_argument('--output_file',    type=str, default="./vids/Obama_groundtruth_output.mp4")

    args = parser.parse_args()
    main(args)