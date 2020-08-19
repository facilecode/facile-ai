import torch
import torchvision.models as tvm 

model = tvm.mobilenet_v2()

data = torch.randn([1,3,224,224])

res = model(data)