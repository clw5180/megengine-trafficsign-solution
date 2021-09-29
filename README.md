# Traffic sign detection 

## 赛题

旷视AI智慧交通开源赛道，初赛6/177，决赛4/12。
本赛题为复杂场景的交通标志检测，对五种交通标志进行识别。

## 算法方案

网络结构：faster-rcnn r50
训练策略：学习率为 0.02 / 16 * gpu数量 * batchsize, batchsize=1，训练24epoch，在16, 22下降；（初赛分数 44->47；训练36epoch基本没有提升）
训练尺寸：多尺度，短边范围：1280到1600，步长32；长边不超过2666；（尺寸较默认设置提升一倍，线上、线下分数提升明显，初赛分数47->54）
后处理参数：置信度阈值0.001， nms阈值0.7；（线上有一个点多的提升，初赛分数54->55.5）
评测尺寸：加入了多尺度测试的代码，短边设置了1280, 1440, 1760 三种尺寸，并且采用了水平翻转；（初赛线上有一个点多的提升,初赛分数55.5->56.6）
其他改进：实现了读取mmdetection coco预训练权重文件的功能，尝试了加载mmdetection提供的mask rcnn预训练权重，但由于线上分数非常接近，最终还是只用官方提供的权重进行训练；
