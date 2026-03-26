import datetime
from django.core.management import BaseCommand
from lms.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = "Create sample payment objects"

    def handle(self, *args, **kwargs):
        Payment.objects.all().delete()

        user1, _ = User.objects.get_or_create(email="test1@sky.pro")
        user2, _ = User.objects.get_or_create(email="test2@sky.pro")

        course1, _ = Course.objects.get_or_create(name="Название курса 1")
        course2, _ = Course.objects.get_or_create(name="Название курса 2")

        lesson1, _ = Lesson.objects.get_or_create(
            name="Название урока 1", course=course1
        )
        lesson2, _ = Lesson.objects.get_or_create(
            name="Название урока 2", course=course2
        )

        Payment.objects.create(
            payer=user1,
            payment_date=datetime.datetime.now().date(),
            amount=10000,
            type="cash",
            paid_course=course1,
        )

        Payment.objects.create(
            payer=user2,
            payment_date=datetime.datetime.now().date(),
            amount=100000,
            type="bank",
            paid_lesson=lesson1,
        )

        Payment.objects.create(
            payer=user1,
            payment_date=datetime.datetime.now().date(),
            amount=50000,
            type="bank",
            paid_lesson=lesson2,
        )

        self.stdout.write(self.style.SUCCESS("Объекты оплаты успешно загружены"))
