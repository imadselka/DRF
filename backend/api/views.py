import json
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer

# @api_view(['GET'])
# def api_home(request,*args,**kwargs):
#     # for product in model_data:
#     #     data.append({
#     #         'title': product.title,
#     #         'content': product.content,
#     #         'price': product.price
#     #     })
#     # if (model_data):
#     #     data = {
#     #         'id': model_data.id,
#     #         'title': model_data.title,
#     #         'content': model_data.content,
#     #         'price': model_data.price
#     #     }
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         # model_data = model_to_dict(model_data,fields=['id','title','price','sale_price'])
#         data = ProductSerializer(instance).data # this is the same as the above line
#         # explain this line: we are serializing the instance of the model to a json object using the ProductSerializer
#         # and then we are getting the data from the serialized object using the .data attribute
#         # the .data attribute is a property of the serializer class that returns the serialized data as a dictionary
        
#     else:
#         data = {
#             'message': 'No data found'
#         }

#     return Response(data)
#     # instead of  serialzing the data manually we can use JsonResponse to do the same thing
#     # return JsonResponse(model_data)
#     # an it more accurate and faster than manual serialization like this below:
#         # print(model_data)
#         # model_data = dict(model_data)
#         # json_data_srt = json.dumps(model_data)
#     # return HttpResponse(json_data_srt,headers={'Content-Type':'application/json'})


@api_view(['POST'])
def api_home(request,*args,**kwargs):
    serializer = ProductSerializer(data=request.data)
    if(serializer.is_valid()):
        print(serializer.data)
        data = serializer.data
        return Response(data)