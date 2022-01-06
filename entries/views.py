from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

# Create your views here.

class EnrtyCreateView(View):

    def post(self, request):
        try:

            return JsonResponse({'MESSAGE':'USER_CREATED'}, status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)

    def get(self, request):
        return JsonResponse({'MESSAGE':'USER_CREATED'}, status=201)

