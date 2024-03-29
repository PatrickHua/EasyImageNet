# EasyImageNet
This repo gives an easy way to download ImageNet dataset on a remote server

### How to download ImageNet

`yes| apt-get install transmission-cli transmission-common transmission-daemon`


`service transmission-daemon start`
optional: `vim /var/lib/transmission-daemon/info/settings.json` (change default download folder from /var/lib/transmission-daemon/downloads/)

`transmission-remote -n 'transmission:transmission' -a http://academictorrents.com/download/a306397ccf9c2ead27155983c254227c0fd938e2.torrent` (train)
`transmission-remote -n 'transmission:transmission' -a http://academictorrents.com/download/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5.torrent` (validation)

`transmission-remote -n 'transmission:transmission' -l` or `watch -n 1 "transmission-remote -n 'transmission:transmission' -l"` for monitoring purpose

(https://help.ubuntu.com/community/TransmissionHowTo)

`service transmission-daemon stop` turn it off after download

# Extract the training data
`mkdir train && mv ILSVRC2012_img_train.tar train/ && cd train`

`tar -xvf ILSVRC2012_img_train.tar && rm -f ILSVRC2012_img_train.tar`

`find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done`

`cd ..`

#
# Extract the validation data and move images to subfolders:
#
`wget https://raw.githubusercontent.com/PatrickHua/EasyImageNet/main/valprep.sh`
`mkdir val && mv ILSVRC2012_img_val.tar val/ && mv valprep.sh val/ && cd val && tar -xvf ILSVRC2012_img_val.tar && sh valprep.sh; cd ..`


# Download ILSVRC2012_devkit_t12.tar.gz
`wget https://image-net.org/data/ILSVRC/2012/ILSVRC2012_devkit_t12.tar.gz`


`tar xzf ILSVRC2012_devkit_t12.tar.gz`


# Create an ImageNet subset for debugging in your local machine

python create_subset.py --source /folder/to/ImageNet/ --target /folder/to/ImagenetSubset/ --samples_per_class 1

