"""Product generic retrieve api view"""
from rest_framework import generics, mixins, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404



from .models import Product
from.serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """Generic CreateAPIView"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    """Generic RetrieveAPIView"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
    """Generic UpdateAPIView"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_update(self, serializer):
        """Update function"""
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # return super().perform_update(serializer)

product_update_view = ProductUpdateAPIView.as_view()

class ProductDestroyAPIView(generics.DestroyAPIView):
    """Generic DeleteAPIView"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_destroy(self, instance):
        """Delete function"""
        self.perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    """Generic ListAPIView"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

product_list_view = ProductListAPIView.as_view()

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    """Mixins and Generic API View"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        """Get Function"""
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create Function"""
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "This is quite nice"
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        """Update Function"""
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete function"""
        return self.destroy(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    """PRODUCT ALT VIEW"""
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "Not good data"}, status=400)
