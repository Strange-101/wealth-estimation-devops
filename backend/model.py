import torch
from torchvision import transforms
from PIL import Image
import timm

# Class names
classes = ['high', 'low', 'medium']

# Device
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# Load model
model = timm.create_model(
    "efficientnet_b0",
    pretrained=False,
    num_classes=3
)

model.load_state_dict(
    torch.load(
        "backend/wealth_model.pth",
        map_location=device
    )
)

model = model.to(device)

model.eval()

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(image_path):

    image = Image.open(image_path).convert("RGB")

    input_tensor = transform(image)

    input_tensor = input_tensor.unsqueeze(0)

    input_tensor = input_tensor.to(device)

    with torch.no_grad():

        outputs = model(input_tensor)

        probabilities = torch.softmax(outputs[0], dim=0)

        predicted_index = torch.argmax(probabilities).item()

        predicted_class = classes[predicted_index]

        confidence = probabilities[predicted_index].item()

    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 4)
    }