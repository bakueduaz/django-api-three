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
news1 = News("Iphone 14 Pro",
             "iPhone 14 Pro and iPhone 14 Pro Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529(maximum depth of 6 meters up to 30 minutes.",
             "https://netrinoimages.s3.eu-west-2.amazonaws.com/2022/12/08/1373191/426752/iphone_14_pro_max_3d_model_c4d_max_obj_fbx_ma_lwo_3ds_3dm_stl_4402727_o.png")
news2 = News("New iPadOS 17",
             "iPadOS 17 takes iPad even further. With new levels of personalization, beautiful and helpful custom Lock Screens, and features to help you get more done, iPad is more capable than ever.",
             "https://b2c-contenthub.com/wp-content/uploads/2023/06/iPadOS-17-lock-screen-customization.jpg?quality=50&strip=all&w=1200")
news3 = News("New General AI",
             "The ultimate achievement to some in the AI industry is creating a system with artificial general intelligence (AGI), or the ability to understand and learn any task that a human can.",
             "https://rare-gallery.com/thumbs/1170002-white-digital-art-simple-background-robot-vehicle-sculpture-technology-Toy-machine-artificial-intelligence-Hi-Tech-hand-product.jpg")

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
