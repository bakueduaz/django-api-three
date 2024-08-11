from django.http import JsonResponse, HttpResponseForbidden
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

class News:
    def __init__(self, tit, des, img):
        self.tit = tit
        self.des = des
        self.img = img

# Create news objects
news1 = News("iPhone 16 Pro Max",
             "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news2 = News("AirPods Pro 3",
             "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentially offer new color options. They are still in early development stages.",
             "https://www.apple.com/newsroom/images/live-action/wwdc-2023/standard/airpods/Apple-AirPods-Pro-2nd-gen-hero-230605.jpg.landing-big_2x.jpg")
news3 = News("Apple Watch Ultra 3",
             "The Apple Watch Ultra 3 will likely maintain the same rugged design as its predecessor but may include new health features like blood pressure monitoring and sleep apnea detection, alongside minor hardware upgrades.",
             "https://www.apple.com/newsroom/images/2023/09/apple-unveils-apple-watch-ultra-2/article/Apple-Watch-Ultra-2-hero-230912_Full-Bleed-Image.jpg.large.jpg")

# Store news objects in a list
news_list = [news1, news2, news3]

@method_decorator(csrf_exempt, name='dispatch')
class NewsView(View):
    def get(self, request):
        # Check for the API key
        api_key = request.GET.get('api_key')
        if api_key != settings.API_KEY:
            return HttpResponseForbidden("Invalid API key")

        # Prepare the news data
        news_data = [{'tit': news.tit, 'des': news.des, 'img': news.img} for news in news_list]
        
        # Return the response
        return JsonResponse({'news': news_data})
