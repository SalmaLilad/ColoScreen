# Albumentations Tutorials

Hands-on examples for learning the Albumentations augmentation library, from basic transforms to production PyTorch pipelines.

## What's Included

**Basic Augmentation**
- `classification.py` - Image augmentation for classification tasks
- `detection.py` - Bounding box augmentation for object detection  
- `segmentation.py` - Mask augmentation for semantic segmentation

**PyTorch Integration**
- `full_pytorch_example.py` - Minimal PyTorch Dataset integration (START HERE)
- `pytorch_albumentations_example.py` - Complete training pipeline with validation loops

## Quick Start: PyTorch Integration

The `full_pytorch_example.py` shows the essential pattern:
```python
class ImageFolder(nn.Module):
    def __getitem__(self, index):
        image = load_image(index)
        if self.transform:
            augmented = self.transform(image=image)
            image = augmented["image"]
        return image, label

```

Key differences from torchvision transforms:
- **Dictionary input/output**: `transform(image=img)` returns `{"image": augmented_img}`
- **NumPy arrays**: Albumentations expects `np.array`, not PIL Images
- **ToTensorV2**: Converts to PyTorch tensor at the end of pipeline

## Augmentation Pipelines

All examples use consistent transform strategies:
- **Geometric**: Resize → RandomCrop → Rotate → Flip
- **Color**: Brightness/contrast, RGB shifts, hue/saturation
- **Quality**: Random blur or noise

Detection/segmentation add synchronized transforms for bboxes/masks.

## Extension to Medical Imaging

For ColoScreen's colorectal pathology detection:
- **Tighter rotations**: ±15-20° instead of ±40° (preserve anatomical orientation)
- **Calibrated color**: Controlled shifts to maintain blood/stool diagnostic features
- **Edge preservation**: Avoid aggressive blur near polyp boundaries
- **Elastic deformation**: Realistic tissue warping for segmentation

The `pytorch_albumentations_example.py` implements these medical-specific augmentations with complete training infrastructure.

## Usage
```bash
# Test basic augmentation
python classification.py
python detection.py
python segmentation.py

# Test PyTorch integration
python full_pytorch_example.py

# Full training pipeline (requires dataset setup)
python pytorch_albumentations_example.py
```

## Key Concepts

**Transform Composition**
```python
transform = A.Compose([
    A.Resize(224, 224),
    A.HorizontalFlip(p=0.5),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ToTensorV2()
])
```

**Bounding Box Augmentation** (detection.py)
```python
transform = A.Compose([
    A.Rotate(limit=20, p=0.5),
    # ... other transforms
], bbox_params=A.BboxParams(format='pascal_voc'))
```

**Mask Augmentation** (segmentation.py)
```python
augmented = transform(image=image, mask=mask)
image = augmented['image']
mask = augmented['mask']  # Automatically transformed
```

## Medical Imaging Best Practices

1. **Conservative geometric transforms**: Medical anatomy has meaningful orientation
2. **Preserve diagnostic features**: Color carries clinical information (blood, tissue types)
3. **Test augmentation quality**: Visualize to ensure transforms don't corrupt ground truth
4. **Separate train/val pipelines**: Only resize+normalize for validation
5. **Use appropriate normalization**: ImageNet stats for transfer learning

## Resources

- [Albumentations Documentation](https://albumentations.ai/docs/)
- [Albumentations GitHub](https://github.com/albumentations-team/albumentations)
- [Medical Imaging Examples](https://albumentations.ai/docs/examples/example_kaggle_salt/)

---
##  AI Assistance Disclosure
  
This README was prepared with the assistance of an AI agent to enhance structure, clarity, and technical documentation quality. All project code, architecture, and experimental results were implemented, and verified by me without any AI use. I provided the outline, structure and content for this ReadME and the AI assistant was used exclusively for documentation, drafting, formatting, and summarization purposes.
