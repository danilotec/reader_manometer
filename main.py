from regression import Manometer

man = Manometer("runs/detect/train/weights/best.pt")
angle = man.get_angle("dataset/regression_dataset/images/image_1.jpg")

def angle_to_percent(angle):
    if angle < 135:
        angle += 360

    percentual = (angle - 135) / 270
    return max(0.0, min(1.0, percentual))

print(angle_to_percent(angle))