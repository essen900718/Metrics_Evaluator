import argparse
import subprocess

def main(args):

    command = [
        "ffmpeg",
        "-i", args.input_file,       # input file name
        "-vf", "scale={}:{}".format(str(args.res),str(args.res)),  # set the resolution
        "-r", str(args.fps),              # set the fps
        args.output_file             # output file name
    ]

    try:
        subprocess.run(command, check=True)
        print("Success !")
    except subprocess.CalledProcessError as e:
        print("Failed !", e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--res',            type=int,    default=512,    help="resolution")
    parser.add_argument('--fps',            type=int,  default=25,     help="frame per second")
    parser.add_argument('--input_file',     type=str, default="./vids/Obama_groundtruth.mp4")
    parser.add_argument('--output_file',    type=str, default="./vids/Obama_groundtruth_output.mp4")

    args = parser.parse_args()
    main(args)
