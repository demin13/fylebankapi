from rest_framework.pagination import PageNumberPagination

class pageForBranches(PageNumberPagination):
    page_size = 100