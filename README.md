# DRF

        This is first steps for learning DRF.

## What I Learned

- CRUD

### Problems to care of

- when u have this problem : `AttributeError: 'collections.OrderedDict' object has no attribute 'get_discount'` this means that there is no instance check the serializers.py

```py
@api_view(['POST'])
def api_home(request,*args,**kwargs):
    serializer = ProductSerializer(data=request.data)
    if(serializer.is_valid()):
        # data = serializer.save() # this gonna save the data to DB
        print(serializer.data)
        # data = serializer.data
        return Response(serializer.data)
```

```py
class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    limited = serializers.SerializerMethodField(read_only=True)

    **
    # when we use SerializerMethodField() she make sure that the obj has an instance
    # in this case in our views file we dont have an instance that's why we got and erro to fix it very simple you
    # just have to add conditions like this
    **
    def get_discount(self,obj):
        # if not hasattr(obj,'id'):
            #return None
        # if not isiinstance(obj,Product):
            # return None
        return obj.get_discount()
    # same thing for other methods
    def get_limited(self,obj):
        return obj.get_limited()
```
