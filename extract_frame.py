import cv2, os
import argparse

def extract_frames(video_path, output_folder, start_frame, end_frame):
    video_capture = cv2.VideoCapture(video_path)
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))

    # Set the capture to the start frame
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    frame_id = 0
    for frame_number in range(start_frame, min(end_frame, total_frames)):
        success, image = video_capture.read()
        if not success:
            break

        frame_path = f"{output_folder}/{frame_id}.jpg"
        cv2.imwrite(frame_path, image)
        frame_id += 1
        print(f"Frame {frame_number} extracted")

    video_capture.release()
    cv2.destroyAllWindows()

def main(args):
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    extract_frames(args.input_file, args.output_folder, args.start_frame, args.end_frame)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--start_frame',    type=int,    default=0)
    parser.add_argument('--end_frame',      type=int,  default=300) # there are total (end_frame-start_frame) extracted frames
    parser.add_argument('--input_file',     type=str, default="./vids/Obama_groundtruth.mp4")
    parser.add_argument('--output_folder',  type=str, default="./extracted_frame")

    args = parser.parse_args()
    main(args)