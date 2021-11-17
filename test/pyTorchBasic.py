import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.zeros(1).cuda())
print(torch.cuda.max_memory_allocated(device=None))