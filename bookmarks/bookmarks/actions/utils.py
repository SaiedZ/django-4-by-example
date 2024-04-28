import datetime

from django.utils import timezone


from django.contrib.contenttypes.models import ContentType

from .models import Action
from .constants import ACTION_DELAY


def create_action(user, verb, target=None):

    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=ACTION_DELAY)
    similar_actions = Action.objects.filter(
        user=user, verb=verb, created__gte=last_minute
    )
    if target is not None:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(
            target_ct=target_ct, target_id=target.id
        )

    if not similar_actions.exists():

        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True

    return False
