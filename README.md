# Traffic sign detection 

## 介绍

本Repo包含了采用MegEngine实现的Faster-RCNN、FCOS、ATSS三个主流模型，并提供了在交通标志数据集(包括红灯，直行路标，向左转弯路标，禁止驶入，禁止车辆临时或长时停放5个类别)上的完整训练和测试代码

## 相关项目链接

- 本目录下代码基于最新版MegEngine，在开始运行本目录下的代码之前，请确保已经正确安装[MegEngine](https://github.com/MegEngine/MegEngine)

- [Models](https://github.com/MegEngine/Models/tree/master/official/vision/detection)

## 如何使用

script目录提供了(frcn__demo, fcos_demo, atss_demo).sh脚本，当准备工作完成之后（如数据、预训练模型等），可以一键跑通训练+测试+推理

- 克隆仓库:

  `https://github.com/er-muyue/megengine-trafficsign.git`

- 安装依赖包(包含了megengine):

  `pip3 install --user -r requirements.txt`

- 关于数据
  - 本目录使用的是交通标志数据集，megstudio环境启动之后默认已经包含数据即，（放到当前目录的data文件夹下，待定）
  - annotations 选用 `...traffic5/annotations_train_val_test`
  ```
  /path/to/
      |->traffic
      |    |images
      |    |annotations->|train.json
      |    |             |val.json
      |    |             |test.json
  ```
- 关于预训练参数

  - 下载对应模型的预训练参数放到`/path/to/weights`
  
  | 模型                                 | 初始化参数                            |
  | ---                                 | ---                                 |
  | FRCN     | https://data.megengine.org.cn/models/weights/faster_rcnn_res50_coco_3x_800size_40dot1_8682ff1a.pkl |
  | FCOS     | https://data.megengine.org.cn/models/weights/fcos_res50_coco_3x_800size_42dot2_b16f9c8b.pkl |
  | ATSS     | https://data.megengine.org.cn/models/weights/atss_res50_coco_3x_800size_42dot6_9a92ed8c.pkl |

- 训练模型
  - `tools/train.py`的命令行选项如下：
    - `-f`, 所需要训练的网络结构描述文件
    - `-n`, 用于训练的devices(gpu)数量
    - `-w`, 预训练的backbone网络权重
    - `-b`，训练时采用的`batch size`, 默认2，表示每张卡训2张图
    - `-d`, 数据集的上级目录，默认`/data/datasets`
  - 默认情况下模型会存在 `logs/模型_gpus{}`目录下。

- 测试模型
  - `tools/test.py`的命令行选项如下：
    - `-f`, 所需要测试的网络结构描述文件
    - `-n`, 用于测试的devices(gpu)数量
    - `-w`, 需要测试的模型权重
    - `-d`，数据集的上级目录，默认`/data/datasets`
    - `-se`，连续测试的起始epoch数，默认为最后一个epoch，该参数的值必须大于等于0且小于模型的最大epoch数
    - `-ee`，连续测试的结束epoch数，默认等于`-se`（即只测试1个epoch），该参数的值必须大于等于`-se`且小于模型的最大epoch数

- 图片推理
  - `tools/inference.py`的命令行选项如下:
    - `-f`, 测试的网络结构描述文件。
    - `-w`, 需要测试的模型权重。
    - `-i`, 需要测试的样例图片。

- 一键运行
  - (frcn__demo, fcos_demo, atss_demo).sh提供了一键运行脚本，默认用户已经申请了两块GPU
 
- 评测结果（COCO Pretrained）—— train set 训练，val set测试，2卡

  |Model|AP|AP50|AP75|APs|APm|APl|AR@1|AR@10|AR@100|ARs|ARm|ARl|注|
  |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
  |FRCN |44.5 |69.4 |49.6 |30.3 |52.4 |67.9 |42.3 |56.3 |56.6 |41.6 |63.3 |76.9 |1X |
  |FRCN |48.0 |71.4 |55.3 |32.7 |58.0 |74.2 |44.7 |58.6 |58.7 |42.3 |67.8 |81.5 |2X |
  |FCOS |38.2 |60.4 |41.2 |18.8 |48.2 |68.3 |37.5 |51.0 |52.3 |31.7 |63.0 |80.3 |1X |
  |FCOS |46.6 |66.9 |51.7 |26.3 |57.5 |75.0 |45.0 |60.0 |60.9 |40.8 |71.9 |84.7 |2X |
  |ATSS |38.4 |59.6 |42.2 |20.4 |48.4 |65.7 |37.6 |51.8 |52.8 |33.3 |63.0 |77.3 |1X |
  |ATSS |46.8 |67.5 |52.6 |25.7 |58.8 |75.1 |44.3 |60.5 |61.2 |40.3 |73.2 |85.7 |2X |

- 参考链接
  - 暂无
