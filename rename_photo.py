import os
import shutil

inicio = './novo_dataset/raw/'
imagens = os.listdir(inicio)

destino = './novo_dataset/images/train/'

i = 1
for image in imagens:
    shutil.copy(f'{inicio}{image}', f'{destino}volume{i}.jpg')
    i += 1
    