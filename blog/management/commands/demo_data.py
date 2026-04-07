from blog.models import patients
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'This command imports demo data'

    def handle (self, *args, **kwargs):
        
        image = [
            'https://picsum.photos/0/1/200/300',
            'https://picsum.photos/1/1/200/300',
            'https://picsum.photos/2/1/200/300',
        ]

        name = [
            'Santhosh',
            'Rubesh',
            'SuraMaxi'
        ]

        age = [
            23,21,20,
        ]

        prescription = [
            'Take one tablet daily after meals',
            'Take two tablet daily after meals',
            'You are healthy and possess heavenly restrictions like lord Toji, no prescription needed',
        ]

        for image, name, age, prescription in zip(image, name, age, prescription):
            patients.objects.create(name=name, age=age, patient_img=image, prescription=prescription)

        self.stdout.write(self.style.SUCCESS('Demo data imported successfully'))
        
