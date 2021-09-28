import json
from tqdm import tqdm
from collections import defaultdict

#train_label_path = '/home/megstudio/dataset/dataset-2805/annotations/val.json'
train_label_path = '/home/megstudio/dataset/dataset-2805/annotations/train.json'


data = json.load(open(train_label_path))
print(data['categories'])

annotations = data['annotations']

category_dict = defaultdict(int)
for ann in tqdm(annotations):
    category_dict[ann['category_id']] += 1
print(category_dict)
