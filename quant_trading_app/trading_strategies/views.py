from rest_framework.views import APIView
from rest_framework.response import Response
from .scripts import macd_oscillator_backtest

class MACDBacktestView(APIView):
    def post(self, request):
        ticker = request.data.get('ticker')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        ma1 = int(request.data.get('ma1'))
        ma2 = int(request.data.get('ma2'))

        encoded_string = macd_oscillator_backtest.run_macd_backtest(ticker, start_date, end_date, ma1, ma2)

        return Response({'plot': encoded_string})
