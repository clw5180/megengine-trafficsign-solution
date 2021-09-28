# -*- coding: utf-8 -*-
# MegEngine is Licensed under the Apache License, Version 2.0 (the "License")
#
# Copyright (c) 2014-2020 Megvii Inc. All rights reserved.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT ARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import models


class CustomerConfig(models.FasterRCNNConfig):
    def __init__(self):
        super().__init__()

        # ------------------------ dataset cfg ---------------------- #
        self.train_dataset = dict(
            # name="traffic5",
            name="dataset-2805",
            root="images",
            ann_file="annotations/train.json",
            remove_images_without_annotations=True,
        )
        self.test_dataset = dict(
            name="traffic5",
            root="images",
            ann_file="annotations/val.json",
            test_final_ann_file="annotations/test.json",
            remove_images_without_annotations=False,
        )
        self.num_classes = 5

        # ------------------------ training cfg ---------------------- #
#         self.train_image_short_size = (640, 672, 704, 736, 768, 800)
        self.train_image_short_size = range(1280, 1600+1, 32)
#         self.train_image_max_size = 1333
        self.train_image_max_size = 2666
        self.basic_lr = 0.02 / 16
        self.max_epoch = 24
        self.lr_decay_stages = [16, 22]

        self.nr_images_epoch = 2226
        self.warm_iters = 100
        self.log_interval = 10

        self.test_image_short_size = 1600
        self.test_image_max_size = 9999
        # ------------------------ testing cfg ----------------------- #
        self.test_cls_threshold = 0.001
        self.test_nms = 0.7
        
Net = models.FasterRCNN
Cfg = CustomerConfig
