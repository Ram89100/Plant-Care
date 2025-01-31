# import torch
# import torch.nn as nn
# import torchvision.models as models
# import torchvision.transforms as transforms
# from PIL import Image
# import io

# # Define the model class
# class PlantDiseaseModel(nn.Module):
#     def __init__(self):
#         super().__init__()
#         # Using pre-trained ResNet34
#         self.network = models.resnet34(pretrained=True)  # Ensure pre-trained weights are used
#         num_ftrs = self.network.fc.in_features
#         self.network.fc = nn.Linear(num_ftrs, 38)  # Adjust for 38 classes

#     def forward(self, xb):
#         return self.network(xb)

# # Image preprocessing function: Resize, Convert to Tensor (no normalization)
# transform = transforms.Compose([
#     transforms.Resize(128),  # Resize to 128x128
#     transforms.ToTensor()    # Convert to tensor
# ])

# # Define the plant disease classes
# num_classes = [
#     'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
#     'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
#     'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
#     'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
#     'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
#     'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
#     'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
#     'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
#     'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites_Two-spotted_spider_mite', 'Tomato___Target_Spot',
#     'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
# ]

# # Load the pre-trained model
# def load_model():
#     model = PlantDiseaseModel()
#     try:
#         model.load_state_dict(torch.load('./Models/plantDisease-resnet34.pth', map_location=torch.device('cpu')))
#         model.eval()  # Set to evaluation mode
#         print("Model loaded successfully.")
#     except Exception as e:
#         print(f"Error loading the model: {e}")
#         raise e
#     return model

# # Predict disease from uploaded image
# def predict_disease(image_bytes, model, labels):
#     try:
#         img_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")  # Ensure image is RGB
#         tensor = transform(img_pil)  # Apply transformations
#         xb = tensor.unsqueeze(0)  # Add batch dimension
#         with torch.no_grad():  # Disable gradient calculation
#             yb = model(xb)  # Forward pass
#         _, preds = torch.max(yb, dim=1)  # Get the predicted class index
#         predicted_class = labels[preds[0].item()]  # Map index to class label
#         return predicted_class
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         return {"error": "Prediction failed"}

# # Example usage:
# if __name__ == "__main__":
#     # Load the model
#     model = load_model()
    
#     # Example image (replace with actual image bytes)
#     with open("test_image.jpg", "rb") as f:
#         image_bytes = f.read()
    
#     # Predict the class
#     result = predict_disease(image_bytes, model, num_classes)
#     print(f"Predicted class: {result}")
import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import io

# Define the model class
class PlantDiseaseModel(nn.Module):
    def __init__(self):
        super().__init__()
        # Using pre-trained ResNet34
        self.network = models.resnet34(pretrained=True)  # Ensure pre-trained weights are used
        num_ftrs = self.network.fc.in_features
        self.network.fc = nn.Linear(num_ftrs, 38)  # Adjust for 38 classes

    def forward(self, xb):
        return self.network(xb)

# Image preprocessing function: Resize, Convert to Tensor (no normalization)
transform = transforms.Compose([
    transforms.Resize(128),  # Resize to 128x128
    transforms.ToTensor()    # Convert to tensor
])

# Define the plant disease classes and their descriptions
num_classes = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
    'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites_Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]

# Disease descriptions for each class
disease_descriptions = {
    'Apple___Apple_scab': 'Apple Scab - Fungal infection affecting apple trees.',
    'Apple___Black_rot': 'Black Rot - A common fungal disease in apples.',
    'Apple___Cedar_apple_rust': 'Cedar Apple Rust - A fungal disease impacting apples and cedars.',
    'Apple___healthy': 'Healthy Apple - No visible disease or infection.',
    'Blueberry___healthy': 'Healthy Blueberry - No visible disease or infection.',
    'Cherry_(including_sour)___Powdery_mildew': 'Powdery Mildew - Fungal infection affecting cherry trees.',
    'Cherry_(including_sour)___healthy': 'Healthy Cherry - No visible disease or infection.',
    'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot': 'Gray Leaf Spot - Fungal disease affecting corn leaves.',
    'Corn_(maize)___Common_rust_': 'Common Rust - A fungal disease affecting corn.',
    'Corn_(maize)___Northern_Leaf_Blight': 'Northern Leaf Blight - A fungal infection of corn leaves.',
    'Corn_(maize)___healthy': 'Healthy Corn - No visible disease or infection.',
    'Grape___Black_rot': 'Black Rot - Fungal disease affecting grapevines.',
    'Grape___Esca_(Black_Measles)': 'Esca - A fungal disease causing symptoms like black spots on grapevines.',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Leaf Blight - Fungal infection causing leaf spots on grapevines.',
    'Grape___healthy': 'Healthy Grape - No visible disease or infection.',
    'Orange___Haunglongbing_(Citrus_greening)': 'Citrus Greening - Bacterial disease affecting orange trees.',
    'Peach___Bacterial_spot': 'Bacterial Spot - Bacterial disease causing lesions on peach leaves.',
    'Peach___healthy': 'Healthy Peach - No visible disease or infection.',
    'Pepper,_bell___Bacterial_spot': 'Bacterial Spot - A bacterial infection affecting bell peppers.',
    'Pepper,_bell___healthy': 'Healthy Bell Pepper - No visible disease or infection.',
    'Potato___Early_blight': 'Early Blight - Fungal disease affecting potato plants.',
    'Potato___Late_blight': 'Late Blight - Fungal infection affecting potatoes, especially during wet conditions.',
    'Potato___healthy': 'Healthy Potato - No visible disease or infection.',
    'Raspberry___healthy': 'Healthy Raspberry - No visible disease or infection.',
    'Soybean___healthy': 'Healthy Soybean - No visible disease or infection.',
    'Squash___Powdery_mildew': 'Powdery Mildew - Fungal disease affecting squash plants.',
    'Strawberry___Leaf_scorch': 'Leaf Scorch - Condition caused by environmental stress or disease in strawberries.',
    'Strawberry___healthy': 'Healthy Strawberry - No visible disease or infection.',
    'Tomato___Bacterial_spot': 'Bacterial Spot - Bacterial disease causing spots on tomato leaves.',
    'Tomato___Early_blight': 'Early Blight - Fungal disease affecting tomato plants.',
    'Tomato___Late_blight': 'Late Blight - Fungal disease, often associated with potato blight, affecting tomatoes.',
    'Tomato___Leaf_Mold': 'Leaf Mold - Fungal infection causing mold on tomato leaves.',
    'Tomato___Septoria_leaf_spot': 'Septoria Leaf Spot - Fungal disease causing circular spots on tomato leaves.',
    'Tomato___Spider_mites_Two-spotted_spider_mite': 'Spider Mites - Tiny pests causing damage to tomato plants.',
    'Tomato___Target_Spot': 'Target Spot - Fungal disease causing target-shaped spots on tomato leaves.',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Tomato Yellow Leaf Curl Virus - A viral disease affecting tomato plants.',
    'Tomato___Tomato_mosaic_virus': 'Tomato Mosaic Virus - A viral disease affecting tomato plants.',
    'Tomato___healthy': 'Healthy Tomato - No visible disease or infection.'
}

# Load the pre-trained model
def load_model():
    model = PlantDiseaseModel()
    try:
        model.load_state_dict(torch.load('./Models/plantDisease-resnet34.pth', map_location=torch.device('cpu')))
        model.eval()  # Set to evaluation mode
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading the model: {e}")
        raise e
    return model

# Predict disease from uploaded image
def predict_disease(image_bytes, model, labels, descriptions):
    try:
        img_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")  # Ensure image is RGB
        tensor = transform(img_pil)  # Apply transformations
        xb = tensor.unsqueeze(0)  # Add batch dimension
        with torch.no_grad():  # Disable gradient calculation
            yb = model(xb)  # Forward pass
        _, preds = torch.max(yb, dim=1)  # Get the predicted class index
        predicted_class = labels[preds[0].item()]  # Map index to class label
        description = descriptions.get(predicted_class, "No description available.")
        return {
            "class": predicted_class,
            "description": description
        }
    except Exception as e:
        print(f"Error during prediction: {e}")
        return {"error": "Prediction failed"}

# import os
# import gdown
# import torch
# import torch.nn as nn
# import torchvision.models as models
# import torchvision.transforms as transforms
# from PIL import Image
# import io

# # Define the model class
# class PlantDiseaseModel(nn.Module):
#     def __init__(self):
#         super().__init__()
#         # Using pre-trained ResNet34
#         self.network = models.resnet34(pretrained=True)  # Ensure pre-trained weights are used
#         num_ftrs = self.network.fc.in_features
#         self.network.fc = nn.Linear(num_ftrs, 38)  # Adjust for 38 classes

#     def forward(self, xb):
#         return self.network(xb)

# # Image preprocessing function: Resize, Convert to Tensor (no normalization)
# transform = transforms.Compose([
#     transforms.Resize(128),  # Resize to 128x128
#     transforms.ToTensor()    # Convert to tensor
# ])

# # Define the plant disease classes and their descriptions
# num_classes = [
#     'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
#     'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
#     'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight',
#     'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
#     'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
#     'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
#     'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
#     'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
#     'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites_Two-spotted_spider_mite', 'Tomato___Target_Spot',
#     'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
# ]

# # Disease descriptions for each class
# disease_descriptions = {
#   'Apple___Apple_scab': 'Apple Scab - Fungal infection affecting apple trees.',
#     'Apple___Black_rot': 'Black Rot - A common fungal disease in apples.',
#     'Apple___Cedar_apple_rust': 'Cedar Apple Rust - A fungal disease impacting apples and cedars.',
#     'Apple___healthy': 'Healthy Apple - No visible disease or infection.',
#     'Blueberry___healthy': 'Healthy Blueberry - No visible disease or infection.',
#     'Cherry_(including_sour)___Powdery_mildew': 'Powdery Mildew - Fungal infection affecting cherry trees.',
#     'Cherry_(including_sour)___healthy': 'Healthy Cherry - No visible disease or infection.',
#     'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot': 'Gray Leaf Spot - Fungal disease affecting corn leaves.',
#     'Corn_(maize)___Common_rust_': 'Common Rust - A fungal disease affecting corn.',
#     'Corn_(maize)___Northern_Leaf_Blight': 'Northern Leaf Blight - A fungal infection of corn leaves.',
#     'Corn_(maize)___healthy': 'Healthy Corn - No visible disease or infection.',
#     'Grape___Black_rot': 'Black Rot - Fungal disease affecting grapevines.',
#     'Grape___Esca_(Black_Measles)': 'Esca - A fungal disease causing symptoms like black spots on grapevines.',
#     'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Leaf Blight - Fungal infection causing leaf spots on grapevines.',
#     'Grape___healthy': 'Healthy Grape - No visible disease or infection.',
#     'Orange___Haunglongbing_(Citrus_greening)': 'Citrus Greening - Bacterial disease affecting orange trees.',
#     'Peach___Bacterial_spot': 'Bacterial Spot - Bacterial disease causing lesions on peach leaves.',
#     'Peach___healthy': 'Healthy Peach - No visible disease or infection.',
#     'Pepper,_bell___Bacterial_spot': 'Bacterial Spot - A bacterial infection affecting bell peppers.',
#     'Pepper,_bell___healthy': 'Healthy Bell Pepper - No visible disease or infection.',
#     'Potato___Early_blight': 'Early Blight - Fungal disease affecting potato plants.',
#     'Potato___Late_blight': 'Late Blight - Fungal infection affecting potatoes, especially during wet conditions.',
#     'Potato___healthy': 'Healthy Potato - No visible disease or infection.',
#     'Raspberry___healthy': 'Healthy Raspberry - No visible disease or infection.',
#     'Soybean___healthy': 'Healthy Soybean - No visible disease or infection.',
#     'Squash___Powdery_mildew': 'Powdery Mildew - Fungal disease affecting squash plants.',
#     'Strawberry___Leaf_scorch': 'Leaf Scorch - Condition caused by environmental stress or disease in strawberries.',
#     'Strawberry___healthy': 'Healthy Strawberry - No visible disease or infection.',
#     'Tomato___Bacterial_spot': 'Bacterial Spot - Bacterial disease causing spots on tomato leaves.',
#     'Tomato___Early_blight': 'Early Blight - Fungal disease affecting tomato plants.',
#     'Tomato___Late_blight': 'Late Blight - Fungal disease, often associated with potato blight, affecting tomatoes.',
#     'Tomato___Leaf_Mold': 'Leaf Mold - Fungal infection causing mold on tomato leaves.',
#     'Tomato___Septoria_leaf_spot': 'Septoria Leaf Spot - Fungal disease causing circular spots on tomato leaves.',
#     'Tomato___Spider_mites_Two-spotted_spider_mite': 'Spider Mites - Tiny pests causing damage to tomato plants.',
#     'Tomato___Target_Spot': 'Target Spot - Fungal disease causing target-shaped spots on tomato leaves.',
#     'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Tomato Yellow Leaf Curl Virus - A viral disease affecting tomato plants.',
#     'Tomato___Tomato_mosaic_virus': 'Tomato Mosaic Virus - A viral disease affecting tomato plants.',
#     'Tomato___healthy': 'Healthy Tomato - No visible disease or infection.'
# }

# # Path for the model file
# local_model_path = './Models/plantDisease-resnet34.pth'

# # Google Drive file ID (replace with your actual file ID)
# google_drive_file_id = '1XcdeIewriDcFlRE_y99dcXP46dx9WuJB'

# # If the model doesn't exist locally, download it from Google Drive
# if not os.path.exists(local_model_path):
#     print("Model not found locally, downloading...")
#     gdown.download(f'https://drive.google.com/uc?id={google_drive_file_id}', local_model_path, quiet=False)
# else:
#     print("Model found locally, loading...")

# # Load the pre-trained model
# def load_model():
#     model = PlantDiseaseModel()
#     try:
#         model.load_state_dict(torch.load(local_model_path, map_location=torch.device('cpu')))
#         model.eval()  # Set to evaluation mode
#         print("Model loaded successfully.")
#     except Exception as e:
#         print(f"Error loading the model: {e}")
#         raise e
#     return model

# # Predict disease from uploaded image
# def predict_disease(image_bytes, model, labels, descriptions):
#     try:
#         img_pil = Image.open(io.BytesIO(image_bytes)).convert("RGB")  # Ensure image is RGB
#         tensor = transform(img_pil)  # Apply transformations
#         xb = tensor.unsqueeze(0)  # Add batch dimension
#         with torch.no_grad():  # Disable gradient calculation
#             yb = model(xb)  # Forward pass
#         _, preds = torch.max(yb, dim=1)  # Get the predicted class index
#         predicted_class = labels[preds[0].item()]  # Map index to class label
#         description = descriptions.get(predicted_class, "No description available.")
#         return {
#             "class": predicted_class,
#             "description": description
#         }
#     except Exception as e:
#         print(f"Error during prediction: {e}")
#         return {"error": "Prediction failed"}
