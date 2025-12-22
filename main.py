from regression import Manometer
from utils import angle_to_percent, get_volume

man = Manometer("runs/detect/train/weights/best.pt")
angle = man.get_angle("dataset/regression_dataset/images/image_3.jpg")


if angle: 
    percent = angle_to_percent(angle)
    print(percent)

    print(get_volume(percent, 25))

