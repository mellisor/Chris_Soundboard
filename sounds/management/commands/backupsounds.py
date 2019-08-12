from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.files import File
from sounds.models import Category, SoundByte
import shutil
import os


class Command(BaseCommand):
    help = 'initializes sounds from init directory'

    def handle(self, *args, **options):
        dirs = set()
        shutil.rmtree(settings.INIT_DIR)
        os.makedirs(settings.INIT_DIR)
        for sound in SoundByte.objects.all():
            if sound.category.name not in dirs:
                dirs.add(str(sound.category.name))
                try:
                    os.mkdir(os.path.join(settings.INIT_DIR,sound.category.name))
                except FileExistsError:
                    pass
            shutil.copyfile(sound.file.path,os.path.join(settings.INIT_DIR,sound.category.name,"{}.wav".format(sound.name)))
        print(dirs)


