import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, State, Iso, Region, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()

    valid_cnt = 0
    for idx, row in enumerate(reader):
        print(idx, row)
        try:
            # name	description	justification	year	longitude	latitude	area_hectares	category	state	region	iso
            try:
                name = str(row[0]).strip()
                if not name:
                    continue
            except:
                continue
            try:
                year = int(row[3])
            except:
                year = None
            try:
                latitude = float(row[5])
            except:
                latitude = None
            try:
                longitude = float(row[4])
            except:
                longitude = None
            try:
                description = str(row[1]).strip()
                if not description:
                    description = None
            except:
                description = None
            try:
                justification = str(row[2]).strip()
                if not justification:
                    justification = None
            except:
                justification = None
            try:
                area_hectares = float(row[6])
            except:
                area_hectares = None

            txt = str(row[7]).strip()
            if txt:
                category, created = Category.objects.get_or_create(name=txt)
            else:
                category = None
            txt = str(row[8]).strip()
            if txt:
                state, created = State.objects.get_or_create(name=txt)
            else:
                state = None
            txt = str(row[9]).strip()
            if txt:
                region, created = Region.objects.get_or_create(name=txt)
            else:
                region = None
            txt = str(row[10]).strip()
            if txt:
                iso, created = Iso.objects.get_or_create(name=txt)
            else:
                iso = None
            site = Site(name=name, year=year, latitude=latitude, longitude=longitude, description=description,
                 justification=justification, area_hectares=area_hectares,
                 category=category, region=region, iso=iso, state=state)
            site.save()
            valid_cnt += 1
        except Exception as e:
            print(e)
    print("valid_cnt={}".format(valid_cnt))
    print("record_num={}".format(Site.objects.all().count()))
