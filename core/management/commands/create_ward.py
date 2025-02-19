import sys
import argparse

from django.core.management.base import BaseCommand

import pandas as pd

from core.models import Municipality, Ward, District, Province


class Command(BaseCommand):
        # help = 'load ward from LocalLevelNepal.csv file'

    def add_arguments(self, parser):
        parser.add_argument("-f", type=argparse.FileType(), required=True)

    def handle(self, *args, **options):
        df = pd.read_csv(sys.argv[3])
        for row in range(0, 6781):
            municipality = Municipality.objects.get(hlcit_code=df['hlcit_code_palika'][row])
            district = municipality.district
            province = municipality.province

            ward = Ward.objects.create(
                name=df['NEW_WARD_N'][row],
                municipality=municipality,
                district=district,
                province=province
            )

            print(row, 'ward successfully updated')

            #
            # print(row)
            # # district=District.objects.get(name=(df['DISTRICT'][row]).upper())
            # municipality = Municipality.objects.get(name=df['GaPa_NaPa'][row])
            # print(municipality.name)

        # ward = [
        #     Ward(
        #         name=df['NEW_WARD_N'][row],
        #         municipality=Municipality.objects.get(name=df['GaPa_NaPa'][row], district=District.objects.get(name=(df['DISTRICT'][row]).upper())),
        #         district=District.objects.get(name=(df['DISTRICT'][row]).upper()),
        #         province=Province.objects.get(code=df['STATE_CODE'][row])
        #
        # ) for row in range(0, 6780)
        # ]
        # ward = Ward.objects.bulk_create(ward)
        # if ward:
        #     self.stdout.write('Successfully loaded wards.."%s"' % ward)
