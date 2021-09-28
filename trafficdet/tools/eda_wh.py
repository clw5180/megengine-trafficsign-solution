import seaborn as sns
import pandas as pd
import numpy as np
import json
from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import defaultdict

%matplotlib inline

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['figure.figsize'] = (10.0, 10.0)

json_paths = ['/home/megstudio/dataset/dataset-2805/annotations/val.json']
images_file = None
new_data = defaultdict(list)
for json_path in json_paths:
    data = json.load(open(json_path))
    new_data['annotations'] += data['annotations']

import json
import os
import cv2
import matplotlib.pyplot as plt

def visualize(image_dir, annotation_file, file_name):
    '''
    Args:
        image_dir (str): image directory
        annotation_file (str): annotation (.json) file path
        file_name (str): target file name (.jpg)
    Returns:
        None
    Example:
        image_dir = "./images"
        annotation_file = "./annotations.json"
        file_name = 'img_0028580.jpg'
        visualize(image_dir, annotation_file, file_name)
    '''
    image_path = os.path.join( image_dir, file_name )
    assert os.path.exists( image_path ), "image path not exist."
    assert os.path.exists( annotation_file ), "annotation file path not exist"
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    with open(annotation_file) as f:
        data = json.load(f)
    image_id = None
    for i in data['images']:
        if i['file_name'] == file_name:
            image_id = i['id']
            break
    if not image_id:
        print("file name {} not found.".format(file_name))
    large_img = True if max( image.shape[0], image.shape[1] ) > 1000 else False
    linewidth = 10 if large_img else 2
    for a in data['annotations']:
        if a['image_id'] == image_id:
            bbox = [int(b) for b in a['bbox']]
            bbox[2] = bbox[2] + bbox[0] - 1
            bbox[3] = bbox[3] + bbox[1] - 1
            cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), linewidth )
    if large_img:
        plt.figure(figsize=(12,10))
    else:
        plt.figure(figsize=(5,5))
    plt.imshow(image)
    plt.show()
    return
### 测试 visualize(image_dir, annotation_file, file_name)
# img_names = [img for img in os.listdir(images_file) if img.endswith('.jpg')]
# for img_name in img_names:
#     visualize(images_file, ann_json, img_name)



'''
### 统计标签类别、图片及bbox数量
print('标签类别:', ann['categories'])
print('类别数量：',len(ann['categories']))
print('训练集图片数量：',len(ann['images']))
print('训练集标签数量：',len(ann['annotations']))
### 统计各尺寸图片数量
total=[]
for img in ann['images']:
    hw=(img['height'],img['width'])
    total.append(hw)
unique=set(total)
for k in unique:
    print('长宽为(%d,%d)的图片数量为：'%k,total.count(k))
### 统计各类别标签数量，并做饼状图
category_dic=dict([(i['id'],i['name']) for i in ann['categories']])  # 创建类别标签字典
counts_label=dict([(i['name'],0) for i in ann['categories']])
for i in ann['annotations']:
    counts_label[category_dic[i['category_id']]]+=1
print('各类别标签数量：', counts_label)
indexs=counts_label.keys()
values=counts_label.values()
Count_df=pd.DataFrame(list(values),index=indexs)
Count_df.plot(kind='pie',y=Count_df.columns,)
#plt.show()
### 标注框宽高比
box_w = []
box_h = []
box_wh = []
categorys_wh = [[] for j in range(len(ann['categories']))]
for a in ann['annotations']:
    if a['category_id'] != 0:
        box_w.append(round(a['bbox'][2],2))
        box_h.append(round(a['bbox'][3],2))
        wh = round(a['bbox'][2]/a['bbox'][3],0)
        if wh <1 :  ## 注意这里所谓的宽高比，是在 '宽高比'和'高宽比'中找到最大值
            wh = round(a['bbox'][3]/a['bbox'][2],0)  # 比如w=10, h=20，那么所谓的宽高比是max(w/h, h/w)而不是w/h=0.5
        box_wh.append(wh)
        categorys_wh[a['category_id']-1].append(wh)
i = 0
plt.figure(figsize=(16, 12))
for c_wh in categorys_wh:
    # 统计每种宽高比的个数
    c_wh_unique = list(set(c_wh))
    c_wh_count = [c_wh.count(i) for i in c_wh_unique]
    # 绘图
    plt.subplot(2, 6, i + 1)
    wh_df = pd.DataFrame(c_wh_count, index=c_wh_unique, columns=[category_dic[i + 1]])
    #     wh_df.plot(kind='bar')
    plt.title(category_dic[i + 1])
    plt.bar(list(wh_df.index), wh_df[category_dic[i + 1]])
    i += 1
# 统计每种宽高比的个数
box_wh_unique = list(set(box_wh))
box_wh_count=[box_wh.count(i) for i in box_wh_unique]
# 绘图,
wh_df = pd.DataFrame(box_wh_count,index=box_wh_unique,columns=['宽高比/高宽比数量'])
wh_df.plot(kind='bar',color="#55aacc")
print('实际存在的宽高比/高宽比（四舍五入的整数）值', list(wh_df.index))
plt.show()
'''

### 1、按class绘制bbox的wh分布
# categorys_w = [[] for j in range(len(ann['categories']))]
# categorys_h = [[] for j in range(len(ann['categories']))]
# for a in ann['annotations']:
#     if a['category_id'] != 0:
#         categorys_w[a['category_id'] - 1].append(round(a['bbox'][2], 2))
#         categorys_h[a['category_id'] - 1].append(round(a['bbox'][3], 2))
# class_id = 12  # clw note: 这里修改需要看bbox宽和高分布的那个class的id
# data_list = list(zip(categorys_w[class_id-1], categorys_h[class_id-1]))
# data = np.array(data_list)

### 2、绘制所有bbox的wh分布
ws = []
hs = []
for a in tqdm(new_data['annotations']):
    ws.append(round(a['bbox'][2], 2))
    hs.append(round(a['bbox'][3], 2))
data_wh = np.array(list(zip(ws, hs)))

### 或者随机生成一些数据
# np.random.seed(sum(map(ord, "distributions")))
# mean, cov = [0, 1], [(1, .5), (.5, 1)]
# data = np.random.multivariate_normal(mean, cov, 200)


df = pd.DataFrame(data_wh, columns=["x", "y"])

sns.set(color_codes=True)
print('start sns.jointplot:')
g = sns.jointplot(x="x", y="y", data=df, kind="kde", color="m")  # 10w样本，在这一步耗时很久，约2min
print('sns.jointplot done !')
g.plot_joint(plt.scatter, c="m", s=30, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)  #画背景网格线
g.set_axis_labels("$X$", "$Y$")
plt.show()
