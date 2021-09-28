export PYTHONPATH=~/workspace/megengine-trafficsign/trafficdet:$PYTHONPATH
cd ~/workspace/megengine-trafficsign/trafficdet
python3 tools/train.py -l exp1 -n 2 -b 1 -f configs/faster_rcnn_res50_800size_trafficdet_demo.py -d ~/dataset -w weights/faster_rcnn_res50_coco_3x_800size_40dot1_8682ff1a.pkl
