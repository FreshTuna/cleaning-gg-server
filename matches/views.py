import json
from random import shuffle, choice

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

            if not Entry.objects.filter(match_id=match_id).count() == 10:
                return JsonResponse({'MESSAGE':'ENTRY_NOT_FULL'}, status=200)

            entries = Entry.objects.filter(match_id=match_id).order_by('leader_yn')

            RED_LINE = ['TOP','JUNGLE','MID','ADC','SUPPORT']
            BLUE_LINE = ['TOP','JUNGLE','MID','ADC','SUPPORT']

            leaders = entries.filter(leader_yn=True)

            entries = entries.exclude(leader_yn=True)

            over_gold = entries.filter(member__tier__in=['GOLD','PLATINUM','DIAMOND','MASTER','GRAND_MASTER','CHALLENGER'])

            under_gold = entries.filter(member__tier__in=['BRONZE','SILVER'])

            roaster = []
            red_team = []
            blue_team = []

            over_gold = list(over_gold)
            leaders = list(leaders)

            shuffle(over_gold)
            shuffle(leaders)

            for index, leader in enumerate(leaders):
                member = Member.objects.get(id=leader.member_id)

                if index % 2 == 1 :
                    red_team.append({
                        'entry_id':leader.id,
                        'member_id': leader.member_id,
                        'match_id': leader.match_id,
                        'game_nickname': member.game_nickname,
                        'nickname' : member.nickname,
                        'leader_yn' : True,
                    })
                    if member.line in RED_LINE: RED_LINE.remove(member.line)
                else:
                    blue_team.append({
                        'entry_id':leader.id,
                        'member_id': leader.member_id,
                        'match_id': leader.match_id,
                        'game_nickname': member.game_nickname,
                        'nickname' : member.nickname,
                        'leader_yn' : True,
                    })
                    if member.line in BLUE_LINE: BLUE_LINE.remove(member.line)

            for index, entry in enumerate(over_gold):
                member = Member.objects.get(id=entry.member_id)

                if index % 2 == 1 :
                    red_team.append({
                        'entry_id':entry.id,
                        'member_id': entry.member_id,
                        'match_id': entry.match_id,
                        'game_nickname': member.game_nickname,
                        'nickname' : member.nickname,
                        'leader_yn' : False,
                    })
                    if member.line in RED_LINE: RED_LINE.remove(member.line)
                else:
                    blue_team.append({
                         'entry_id':entry.id,
                         'member_id': entry.member_id,
                         'match_id': entry.match_id,
                         'game_nickname': member.game_nickname,
                         'nickname' : member.nickname,
                         'leader_yn' : False,
                    })
                    if member.line in BLUE_LINE: BLUE_LINE.remove(member.line)

            pool_size = len(under_gold)
            for i in range(pool_size):

                current_pick = "RED" if len(red_team) < len(blue_team) else "BLUE"
                temp_pool    = list(under_gold)
                if current_pick == "RED":
                    temp = under_gold.filter(member__line__in=RED_LINE)

                    if temp:
                        temp_pool.append(temp.first())

                    chosen_entry = choice(temp_pool)

                    under_gold = under_gold.exclude(id = chosen_entry.id)

                    member = Member.objects.get(id=chosen_entry.member_id)

                    red_team.append({
                        'entry_id':chosen_entry.id,
                        'member_id': chosen_entry.member_id,
                        'match_id': chosen_entry.match_id,
                        'game_nickname': member.game_nickname,
                        'nickname' : member.nickname,
                        'leader_yn' : False,
                    })
                    if member.line in RED_LINE: RED_LINE.remove(member.line)

                else:
                    temp = under_gold.filter(member__line__in=BLUE_LINE)

                    if temp:
                        temp_pool.append(temp.first())

                    chosen_entry = choice(temp_pool)

                    under_gold = under_gold.exclude(id = chosen_entry.id)

                    member = Member.objects.get(id=chosen_entry.member_id)

                    blue_team.append({
                         'entry_id':chosen_entry.id,
                         'member_id': chosen_entry.member_id,
                         'match_id': chosen_entry.match_id,
                         'game_nickname': member.game_nickname,
                         'nickname' : member.nickname,
                         'leader_yn' : False,
                    })
                    if member.line in BLUE_LINE: BLUE_LINE.remove(member.line)

                print("픽 : ",member.nickname)

            print("red team :", red_team,"\n red line:", RED_LINE)
            print("blue team :", blue_team,"\n blue line:", BLUE_LINE)

            roaster = {
                'red_team':red_team,
                'blue_team':blue_team
            }
            
            return JsonResponse({'MESSAGE':'MATCH_RANDOMIZED','roaster':roaster}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)