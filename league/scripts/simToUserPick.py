from league.models import Draft, CurrentPick, Team, Player
from django.db.models import Q

def toUserPick():
    currentOBJ = CurrentPick.objects.first()
    currentPick = currentOBJ.pick

    userPicks = Draft.objects.filter(userPick=True).order_by('-pick')
    nextPick = None
    for pick in userPicks:
        if currentPick < pick.pick:
            nextPick = pick
        else:
            pass
    if nextPick == None:
        return None
    

    picksToSim = Draft.objects.filter(Q(Q(pick__gte=currentPick) & Q(pick__lt=nextPick.pick))).order_by('pick')
    return picksToSim


