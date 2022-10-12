from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from clothes.models import Good, Category
from clothes.serializers import AdminTicketSerializer


class GoodsAPIView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Good.objects.all()
    serializer_class = AdminTicketSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'clothes/shop.html'
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('price', 'category')

    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        # section = get_object_or_404(Good, slug=kwargs['slug'])
        # sort = request.GET.getlist('sort')
        # articles = section.article_set.all().order_by(*sort)

        goods = self.queryset.all()
        category = Category.objects.all()
        print(goods)
        return Response({'goods': goods, 'category': category})

    def post(self, request, *args, **kwargs):
        serializer = AdminTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['author'] = self.request.user
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


def index(request):
    return render(request, 'clothes/index.html')


def about(request):
    return render(request, 'clothes/about.html')


def contact(request):
    return render(request, 'clothes/contact.html')


def shop(request):
    goods = Good.objects.all()
    category = Category.objects.all()

    data = {
        'goods': goods,
        'category': category
    }
    return render(request, 'clothes/shop.html', context=data)


def filter_shop(request, cat_slug):
    category = Category.objects.all()
    goods = Good.objects.filter(category__slug=cat_slug)

    if cat_slug in ("male", "female"):
        if cat_slug == "male":
            goods = Good.objects.filter(gender=1)
        elif cat_slug == "female":
            goods = Good.objects.filter(gender=2)

    data = {
        'goods': goods,
        'category': category
    }
    return render(request, 'clothes/shop.html', context=data)


def shop_single(request, goods_slug):
    model = Good.objects.get(slug=goods_slug)
    data = {
        'model': model
    }
    return render(request, 'clothes/shop-single.html', context=data)


def login(request):
    model = Good.objects.all()
    data = {
        'model': model
    }
    return render(request, 'clothes/login.html', context=data)
