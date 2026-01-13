import csv
from django.core.management.base import BaseCommand
from catalog.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            next(reader) 

            for row in reader:
                try:
                    phone = Phone(
                        id=int(row[0]),
                        name=row[1],
                        price=float(row[2]),
                        image=row[3],
                        release_date=row[4],
                        lte_exists=row[5].lower() == 'true'
                    )
                    phone.save() 
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Ошибка в строке {row}: {e}'))
        
        self.stdout.write(self.style.SUCCESS('Импорт завершён успешно!'))
