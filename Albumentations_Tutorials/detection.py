
import cv2
import albumentations as A
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

def visualize(image):
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(image)
    plt.show()

def visualize_bbox(img, bbox, class_name, color=(255, 0, 0), thickness=2):
    """Visualizes a single bounding box on the image"""
    x_min, y_min, x_max, y_max = bbox
    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)
    
    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), color, -1)
    cv2.putText(
        img,
        text=class_name,
        org=(x_min, y_min - int(0.3 * text_height)),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=0.35, 
        color=(255, 255, 255), 
        lineType=cv2.LINE_AA,
    )
    return img

def plot_examples(images, bboxes=None):
    fig = plt.figure(figsize=(15, 15))
    columns = 4
    rows = 5
    max_images = rows * columns # 20 images max

    num_images_to_plot = min(len(images), max_images)
    
    for i in range(num_images_to_plot):
        if bboxes is not None and i < len(bboxes):
            img = visualize_bbox(images[i].copy(), bboxes[i], class_name="Animals")
        else:
            img = images[i]
        
        fig.add_subplot(rows, columns, i + 1)
        plt.imshow(img)
        plt.axis("on")
    
    plt.tight_layout()
    plt.show()

image = cv2.imread("Cats_Dogs_Imgs/cats/cat_5.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height, width = image.shape[:2]
bboxes = [[int(width * 0.05), int(height * 0.20), int(width * 0.40), int(height * 0.95)]]
#Pascal_voc (x_min, y_min, x_max, y_max), YOLO, COCO

transform = A.Compose(
    [
        A.Resize(width=1920, height=1080),
        A.RandomCrop(width=1280, height=780),
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.35),
        A.Rotate(limit=40, p=0.9, border_mode=cv2.BORDER_CONSTANT),
        A.VerticalFlip(p=0.1),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.9),
        #A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)), #Adjusts pixel values for consistency -> good for better neural network training
        A.OneOf([
            A.Blur(blur_limit=3, p=0.5),
            A.ColorJitter(p=0.5)
        ], p=1.0)
    ], bbox_params=A.BboxParams(format="pascal_voc", label_fields=[])
)

resize_transform = A.Compose([
    A.Resize(width=1920, height=1080)
], bbox_params=A.BboxParams(format="pascal_voc", label_fields=[]))

resized = resize_transform(image=image, bboxes=bboxes)
image = resized["image"]
bboxes = resized["bboxes"]

images_list = [image]
saved_bboxes=[bboxes[0]]

for i in range(15):
    augmentations = transform(image=image, bboxes=bboxes)
    augmented_img = augmentations["image"]

    if len(augmentations["bboxes"]) > 0:  # Added this check
        images_list.append(augmented_img)
        saved_bboxes.append(augmentations["bboxes"][0])

plot_examples(images_list, saved_bboxes)
