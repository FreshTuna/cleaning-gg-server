import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from entries.models import Entry
from matches.models import Match
from members.models import Member

# Create your views here.

class EntryCreateView(View):

    def post(self, request):
        try:
            data = json.loads(request.body)

            game_nickname = data['game_nickname']
            match_id      = data['match_id'] 

            print(match_id)

            if not Match.objects.filter(id=match_id).exists():
                return JsonResponse({'MESSAGE':'NO_MATCH_EXISTING'}, status=200)

            member = Member.objects.get(game_nickname=game_nickname)

            if Entry.objects.filter(match_id=match_id, member_id=member.id).exists():
                return JsonResponse({'MESSAGE':'ENTRY_EXISTING'}, status=200)

            if Entry.objects.filter(match_id=match_id).count() > 9:
                return JsonResponse({'MESSAGE':'ENTRY_FULL'}, status=200)

            entry = Entry.objects.create(
                match_id = match_id,
                member_id = member.id
            )

            res = {
                'match_id': match_id,
                'entry_id': entry.id,
                'member_id': member.id,
                'game_nickname': member.game_nickname,
                'tier': member.tier,
                'nickname': member.nickname,
            }

            return JsonResponse({'MESSAGE':'ENTRY_CREATED','member':res}, status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)

    def get(self, request):
        return JsonResponse({'MESSAGE':'USER_CREATED'}, status=201)

class EntryGetView(View):

    def get(self, request):
        try:
            match_id = request.GET['match_id']

            for entry in Entry.objects.filter(match_id=match_id) :
                member = Member.objects.get(id=entry.member_id)
                entry_list = [{
                    'member_id': entry.member_id,
                    'tier' : member.tier,
                    'game_nickname': member.game_nickname,
                    'nickname' : member.nickname
                }]

            return JsonResponse({'entry_list':entry_list}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)
