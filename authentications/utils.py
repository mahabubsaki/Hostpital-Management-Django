import requests
import base64
from .models import UserProfile,User

def upload_image_to_imgbb(image_file):
    url = "https://api.imgbb.com/1/upload"
    image_data = image_file.read()
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')
    payload = {
        "key": "fe2a5ac70ac4f688f2fa81bdeaf23269",
        "image": image_data_base64 
    }
    response = requests.post(url, data=payload)
    data = response.json()
    if data["status"] == 200:
        return data["data"]["display_url"]
    else:

        return None
    
def get_current_user(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if user:
            user_profile = UserProfile.objects.get(user=user)
            return user_profile
    return None
    
    
    