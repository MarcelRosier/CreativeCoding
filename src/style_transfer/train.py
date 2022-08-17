from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.optim as optim
import requests
from torchvision import transforms, models


def load_image(img_path, max_size=400, shape=None):
    ''' Load in and transform an image, making sure the image
       is <= 400 pixels in the x-y dims.'''
    if "http" in img_path:
        response = requests.get(img_path)
        image = Image.open(BytesIO(response.content)).convert('RGB')
    else:
        image = Image.open(img_path).convert('RGB')
    
    # large images will slow down processing
    if max(image.size) > max_size:
        size = max_size
    else:
        size = max(image.size)
    
    if shape is not None:
        size = shape
        
    in_transform = transforms.Compose([
                        transforms.Resize(size),
                        transforms.ToTensor(),
                        transforms.Normalize((0.485, 0.456, 0.406), 
                                             (0.229, 0.224, 0.225))])

    # discard the transparent, alpha channel (that's the :3) and add the batch dimension
    image = in_transform(image)[:3,:,:].unsqueeze(0)
    
    return image
# use the convolutional and pooling layers to get the "features"
# portion of VGG19
vgg = models.vgg19(weights=models.VGG19_Weights.IMAGENET1K_V1).features
# freeze all VGG parameters as we're only optimizing the target
# image
for param in vgg.parameters():
    param.requires_grad_(False)

# move the model to GPU, if available (but since I'm using colab
# it doesn't really matter
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
vgg.to(device)
# print (vgg)

# load in content and style image
content = load_image('worker.jpg').to(device)
# Resize style to match content, makes code easier
style = load_image('vangogh.jpg', shape=content.shape[-2:]).to(device)