import json
from django.http import HttpResponse
from doge.models import DogeConversion

def exchange(request):
    """API endpoint for requesting current BTC-DOGE exchange rate."""
    conversion = DogeConversion.objects.latest('timestamp')
    response = {'conversion': conversion.rate}
    return HttpResponse(
        json.dumps(response),
        content_type='application/json'
    )
