from regression import Manometer

man = Manometer("runs/detect/train/weights/best.pt")
print(man.get_angle("dataset/regression_dataset/images/image_3.jpg"))

