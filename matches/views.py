import json

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

from matches.models import Match
from members.models import Member
from entries.models import Entry

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
            if not Match.objects.filter(status='MATCHING'):
                return JsonResponse({'MESSAGE':'NO_MATCH'}, status=200)

            match = Match.objects.get(status='MATCHING')

            res_dict = {
                'match_id': match.id,
                'owner': match.owner,
                'status': match.status,
            }

            entry_list =[]

            for entry in Entry.objects.filter(match_id=match.id):
                member = Member.objects.get(id=entry.member_id)
            
                entry_list.append({
                    'member_id': entry.member_id,
                    'entry_id': entry.id,
                    'tier' : member.tier,
                    'leader_yn': entry.leader_yn,
                    'game_nickname': member.game_nickname,
                    'nickname' : member.nickname
                })

            return JsonResponse({'MESSAGE':'MATCH_JOINED', 'match':res_dict,'entry_list':entry_list}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)

class MatchStartView(View):
    def post(self, request):
        try:

            return JsonResponse({'MESSAGE':'MATCH_STARTED'}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)


class MatchRandomizeView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            match_id = data['match_id']

            entries = Entry.objects.filter(match_id=match_id).order_by('leader_yn')

            print(entries.filter(leader_yn=True))

            leaders = entries.filter(leader_yn=True)

            # entries = entries.exclude(leader_yn=True)

            over_gold = entries.filter(member__tier__in=['GOLD','PLATINUM','DIAMOND','MASTER','GRAND_MASTER','CHALLENGER'])

            under_gold = entries.filter(member__tier__in=['BRONZE','SILVER'])

            roaster =[]

            for entry in entries:
                member = Member.objects.get(id=entry.member_id)

                roaster.append({
                    'entry_id':entry.id,
                    'member_id': entry.member_id,
                    'match_id': entry.match_id,
                    'game_nickname': member.game_nickname,
                    'nickname' : member.nickname
                })
            
            return JsonResponse({'MESSAGE':'MATCH_RANDOMIZED', 'roaster':roaster}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)