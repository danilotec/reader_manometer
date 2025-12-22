from regression import Manometer
from utils import angle_to_percent, get_volume

man = Manometer("runs/detect/train2/weights/best.pt")
angle = man.get_angle("dataset/regression_dataset/images/image3_2.jpg")


if angle: 
    print('angulo: ', round(angle, 2))
    percent = angle_to_percent(angle)
    print('porcentagem: ', round(percent, 2))

    print('volume: ', round(get_volume(percent, 800), 2))
