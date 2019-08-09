from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.files import File
from sounds.models import Category, SoundByte
import shutil
import os


class Command(BaseCommand):
    help = 'initializes sounds from init directory'

    def add_arguments(self,parser):
        parser.add_argument('--delete',action='store_true',help='Delete all categories')

    def handle(self, *args, **options):
        if options['delete']:
            Category.objects.all().delete()
        for category in os.listdir(settings.INIT_DIR):
            c = Category(name=category)
            c.save()
            for sound in os.listdir(os.path.join(settings.INIT_DIR, category)):
                old_path = os.path.join(settings.INIT_DIR,category,sound)
                s = SoundByte(name=sound.split(".")[0], category=c)
                s.file = File(open(old_path,'rb'))
                s.save()

