import helpers.billing
from typing import Any
from django.core.management.base import BaseCommand

from subscriptions import utils as subs_utils

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--clear-dangling", action="store_true", default=False)

    def handle(self, *args: Any, **options: Any):
        clear_dangling = options.get("clear_dangling", False)
        if clear_dangling:
            subs_utils.clear_dangling_subs()
        else:
            subs_utils.sync_user_subs()
