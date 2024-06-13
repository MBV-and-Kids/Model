import torch
from torchvision import transforms

height, width, channel = 480, 480, 1
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
ngpu = 1
ksize = 4
z_dim = 20
learning_rate = 1e-3

img_size = 480

transform = transforms.Compose([
    transforms.Resize((img_size, img_size)),
    transforms.Grayscale(),
    transforms.ToTensor(),
])

epochs = 100
batch_size =32