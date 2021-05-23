
import os
import argparse
from shutil import copy, copyfile
from tqdm import tqdm
parser = argparse.ArgumentParser()
parser.add_argument('--source_dir', type=str, default='/root/Data/ImageNet/')
parser.add_argument('--target_dir', type=str, default='ImagenetSubset')
parser.add_argument('--samples_per_class', type=int, default=20)
args = parser.parse_args()




imagenet_dir = args.source_dir

train_dir = os.path.join(imagenet_dir, 'train')
val_dir = os.path.join(imagenet_dir, 'val')
devkit = os.path.join(imagenet_dir, 'ILSVRC2012_devkit_t12.tar.gz')

# subset_dir = './ImageNet'
os.makedirs(args.target_dir, exist_ok=True)

def cp_from(source_dir, target_dir):
    # target_dir = 
    for folder in tqdm(os.listdir(source_dir)):
        if os.path.isdir(os.path.join(source_dir, folder)):
            counter = 0 
            for file in os.listdir(os.path.join(source_dir, folder)):
                if file.endswith('.JPEG'):
                    os.makedirs(os.path.join(target_dir, folder), exist_ok=True)
                    copyfile(os.path.join(source_dir, folder, file), os.path.join(target_dir, folder, file))
                    counter += 1
                    if counter >= args.samples_per_class:
                        break

target_train = os.path.join(args.target_dir, 'train')
target_val = os.path.join(args.target_dir, 'val')
os.makedirs(target_train)
os.makedirs(target_val)
cp_from(train_dir, target_train)
cp_from(val_dir, target_val)

copyfile(devkit, os.path.join(args.target_dir, 'ILSVRC2012_devkit_t12.tar.gz'))

















