import json
import jwt

from django.shortcuts import render
from django.views     import View
from django.http      import JsonResponse

from my_settings      import SECRET_KEY, ALGORITHM
from members.models   import Member

# Create your views here.

class SignUpView(View):

    def post(self, request):
        try: 
            data = json.loads(request.body)

            nickname      = data['nickname']
            game_nickname = data['game_nickname']
            tier          = data['tier']
            line          = data['line']

            Member.objects.create(
                nickname      = nickname,
                game_nickname = game_nickname,
                tier          = tier,
                line          = line
            )

            return JsonResponse({'MESSAGE':'USER_CREATED'}, status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)

    def get(self, request):
        return JsonResponse({'MESSAGE':'USER_CREATED'}, status=201)


class SignInView(View):

    def post(self, request):
        try:
            data = json.loads(request.body)

            game_nickname = data['game_nickname']

            if not Member.objects.filter(game_nickname = game_nickname).exists():
                return JsonResponse({'MESSAGE':'WRONG_EMAIL'}, status=400)
            
            member = Member.objects.get(game_nickname = game_nickname)

            member_token = jwt.encode({'member_id':member.id}, SECRET_KEY, algorithm=ALGORITHM)

            return JsonResponse({'MESSAGE':'SUCCESS', 'TOKEN':member_token}, status=200)
        except json.decoder.JSONDecodeError:
            return JsonResponse({'MESSAGE': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'MESSAGE':'KEY_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'MESSAGE':'TYPE_ERROR'}, status=400)