# Metrics_Evaluator
Multiples metrics evaluator (PSNR, LPIPS, SyncNet...), combination of several repositories.
- SyncNet cloned from [syncnet_python](https://github.com/joonson/syncnet_python), several files from [Wav2Lip](https://github.com/Rudrabha/Wav2Lip/tree/master)

## environment
1. `moviepy` for calculator frame number
2. `cv2` for extract frames
3. `ffmpeg` for modify setting of video
4. `cv2`, `pytorch`, `scikit-image`, `lpips`, `torchvision` for calculate psnr, lpips
5. `argparse`  

## PSNR, LPIPS

`psnr_lpips_calculator`
extract the target frames for evaluation by `extract_frame.py`, and change the path in main function
```
python extract_frame.py
python psnr_lpips_calculator.py
```

## SyncNet

put the evaluation video in the folder `./syncnet_python/video`(data_root)

for one file on Windows
```
cd syncnet_python
python run_pipeline.py --videofile ./syncnet_python/video/obama_valid.mp4 --reference wav2lip --data_dir tmp_dir
python calculate_scores_real_videos.py --videofile ./syncnet_python/video/obama_valid.mp4 --reference wav2lip --data_dir tmp_dir >> all_scores.txt
```

for all video on Linux
```
cd syncnet_python
sh calculate_scores_real_videos.sh ./syncnet_python/video
```