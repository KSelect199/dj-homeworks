import csv
from django.core.management.base import BaseCommand
from catalog.models import Phone 


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
           
            next(phone_reader)

            for line in phone_reader:
       
                try:
                    phone_id = int(line[0])
                    name = line[1]
                    price = float(line[2])
                    image = line[3]
                    release_date = line[4] 
                    lte_exists = line[5].lower() == 'true'

                    Phone.objects.update_or_create(
                        id=phone_id,
                        defaults={
                            'name': name,
                            'price': price,
                            'image': image,
                            'release_date': release_date,
                            'lte_exists': lte_exists,
                        }
                    )
                except (IndexError, ValueError) as e:
                    self.stdout.write(
                        self.style.ERROR(f'Ошибка в строке: {line} — {e}')
                    )

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))
