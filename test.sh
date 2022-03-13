echo "Taking you."
# cd /project/train/src_repo/yolov5
# python t1.py

cd /project/train/src_repo
cp -r /home/data/168 ./helmet_data
python data_split.py
python path.py
cd yolov5
python train.py --batch-size 32 --epochs 300 --data ./data/coco.yaml --hyp ./data/hyps/hyp.scratch-low.yaml --weight ./weights/yolov5s.pt --img 480 --project /project/train/models/ --cfg ./models/yolov5s.yaml