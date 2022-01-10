import json

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

from matches.models import Match
from members.models import Member

# Create your views here.

class MatchCreateView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            owner_nickname = data['owner_nickname']

            if Match.objects.filter(status="MATCHING").exists():
                return JsonResponse({'MESSAGE':'MATCHING_STATUS_EXISTING'}, status=200)
            
            print(owner_nickname)
            owner = Member.objects.get(game_nickname=owner_nickname)

            Match.objects.create(
                owner=owner.id,
                status='MATCHING'
            )

            return JsonResponse({'MESSAGE':'MATCH_CREATED'}, status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)

    class MatchGetView(View):
        def get(self, request):
            try:
                
                if not Match.objects.filter(status__in=['MATCHING','PLAYING']):
                    return JsonResponse({'MESSAGE':'NO_MATCH'}, status=200)

                return JsonResponse({'MESSAGE':'MATCH_CREATED'}, status=201)
            except json.decoder.JSONDecodeError:
                return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
            except KeyError:
                return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
            except TypeError:
                return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)
