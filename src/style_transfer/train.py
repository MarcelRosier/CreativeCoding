from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.optim as optim
import requests
from torchvision import transforms, models

# use the convolutional and pooling layers to get the "features"
# portion of VGG19
vgg = models.vgg19(pretrained=True).features
# freeze all VGG parameters as we're only optimizing the target
# image
for param in vgg.parameters():
    param.requires_grad_(False)
