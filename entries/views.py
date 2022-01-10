import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from entries.models import Enrty
from matches.models import Match
from members.models import Member

# Create your views here.

class EnrtyCreateView(View):

    def post(self, request):
        try:
            data = json.loads(request.body)

            game_nickname = data['game_nickname']
            match_id      = data['match_id'] 

            if not Match.objects.filter(match_id=match_id).exits():
                return JsonResponse({'MESSAGE':'NO_MATCH_EXISTING'}, status=200)

            if Entry.objects.filter(match_id=match_id, game_nickname=game_nickname).exists():
                return JsonResponse({'MESSAGE':'ENTRY_EXISTING'}, status=200)

            if Entry.objects.filter(match_id=match_id).count() > 9:
                return JsonResponse({'MESSAGE':'ENTRY_FULL'}, status=200)

            member = Member.objects.get(game_nickname=game_nickname)

            Entry.create(
                match_id = match_id,
                member_id = member.id
            )

            return JsonResponse({'MESSAGE':'ENTRY_CREATED'}, status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)

    def get(self, request):
        return JsonResponse({'MESSAGE':'USER_CREATED'}, status=201)

