export PYTHONPATH=~/workspace/megengine-trafficsign/trafficdet:$PYTHONPATH
cd ~/workspace/megengine-trafficsign/trafficdet
python3 tools/test.py -l exp2 -n 1 -se 19 -f configs/faster_rcnn_res50_800size_trafficdet_demo.py -d ~/dataset
