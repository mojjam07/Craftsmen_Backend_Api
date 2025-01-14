# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import User, Craftsman, Apprentice, Category, Order, Job
from .serializers import UserSerializer, CraftsmanSerializer, ApprenticeSerializer, CategorySerializer, OrderSerializer, JobSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        users = User.objects.all()
        if not users.exists():
            return Response({"success": False, "message": "No users found"}, status=status.HTTP_404_NOT_FOUND)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CraftsmanView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        craftsmen = Craftsman.objects.all()
        if not craftsmen.exists():
            return Response({"success": False, "message": "No craftsmen found"}, status=status.HTTP_404_NOT_FOUND)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(craftsmen, request)
        serializer = CraftsmanSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = CraftsmanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ApprenticeView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        apprentices = Apprentice.objects.all()
        if not apprentices.exists():
            return Response({"success": False, "message": "No apprentices found"}, status=status.HTTP_404_NOT_FOUND)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(apprentices, request)
        serializer = ApprenticeSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ApprenticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        categories = Category.objects.all()
        if not categories.exists():
            return Response({"success": False, "message": "No categories found"}, status=status.HTTP_404_NOT_FOUND)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(categories, request)
        serializer = CategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class OrderView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        orders = Order.objects.all()
        if not orders.exists():
            return Response({"success": False, "message": "No orders found"}, status=status.HTTP_404_NOT_FOUND)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(orders, request)
        serializer = OrderSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class JobView(APIView):
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        jobs = Job.objects.all()
        if not jobs.exists():
            return Response({"success": False, "message": "No jobs found"}, status=status.HTTP_404_NOT_FOUND)
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(jobs, request)
        serializer = JobSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)