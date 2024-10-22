import torch

# Проверка доступности CUDA (GPU)
print("CUDA доступен:", torch.cuda.is_available())

# Если CUDA доступен, выведем информацию о доступных GPU
if torch.cuda.is_available():
    print("Используемое устройство:", torch.cuda.get_device_name(0))
else:
    print("Используется CPU")
