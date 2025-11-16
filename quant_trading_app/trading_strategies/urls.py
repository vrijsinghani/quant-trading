from django.urls import path
from .views import MACDBacktestView

urlpatterns = [
    path('macd/', MACDBacktestView.as_view(), name='macd_backtest'),
]
