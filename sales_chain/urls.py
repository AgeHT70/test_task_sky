from rest_framework import routers

from sales_chain.views import ChainLinkViewSet

app_name = 'chainlink'
router = routers.SimpleRouter()
router.register('chainlink', ChainLinkViewSet)

urlpatterns = []

urlpatterns += router.urls
