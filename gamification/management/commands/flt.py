from django.core.management.base import BaseCommand, CommandError

from Create_Test.models import FullLengthTest


class Command(BaseCommand):

    def handle(self, *args, **options):
        flt = FullLengthTest.objects.filter(id=2).values(
                'reading_set__Reading','speaking_set__Speaking',
                'listening_set__Listening','writing_set__Writing')
        
        other_ids = list(flt.values_list('reading_set__Reading','listening_set__Listening'))      
        speaking_ids = list(flt.values_list('speaking_set__Speaking',flat=True))
        unpack_other_ids = list(map(lambda x: (i for i in x),other_ids ))
        print(speaking_ids)
        print(unpack_other_ids)
        