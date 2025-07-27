from django.test import TestCase
from .models import Pictures, YearOfExam, DistinctionHolder, Announcements
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

class PicturesModelTest(TestCase):
    def setUp(self):
        self.picture = Pictures.objects.create(
            pictureType="Event",
            pictureName="Annual Day",
            pictureDate=datetime.date(2023, 1, 15),
            picture=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        )

    def test_picture_creation(self):
        self.assertEqual(self.picture.pictureType, "Event")
        self.assertEqual(self.picture.pictureName, "Annual Day")
        self.assertEqual(self.picture.pictureDate, datetime.date(2023, 1, 15))
        self.assertTrue(self.picture.picture.name.startswith('media/'))

    def test_picture_str_method(self):
        self.assertEqual(str(self.picture), "Annual Day")


class YearOfExamModelTest(TestCase):
    def setUp(self):
        self.year = YearOfExam.objects.create(year_of_exam=2022)

    def test_year_creation(self):
        self.assertEqual(self.year.year_of_exam, 2022)

    def test_year_str_method(self):
        self.assertEqual(str(self.year), "2022")

    def test_unique_year_constraint(self):
        with self.assertRaises(Exception):  # IntegrityError may not be raised until save()
            YearOfExam.objects.create(year_of_exam=2022)


class DistinctionHolderModelTest(TestCase):
    def setUp(self):
        self.year = YearOfExam.objects.create(year_of_exam=2021)
        self.holder = DistinctionHolder.objects.create(
            toppers=self.year,
            name="Sara",
            marks=98,
            image=SimpleUploadedFile(name='sara.jpg', content=b'', content_type='image/jpeg')
        )

    def test_distinction_creation(self):
        self.assertEqual(self.holder.name, "Sara")
        self.assertEqual(self.holder.marks, 98)
        self.assertEqual(self.holder.toppers.year_of_exam, 2021)
        self.assertTrue(self.holder.image.name.startswith('media/'))

    def test_distinction_str_method(self):
        self.assertEqual(str(self.holder), "Sara (2021)")


class AnnouncementsModelTest(TestCase):
    def setUp(self):
        self.announcement = Announcements.objects.create(
            announcementName="Holiday",
            announcement="School will remain closed tomorrow due to rain."
        )

    def test_announcement_creation(self):
        self.assertEqual(self.announcement.announcementName, "Holiday")
        self.assertEqual(self.announcement.announcement, "School will remain closed tomorrow due to rain.")

    def test_announcement_str_method(self):
        self.assertEqual(str(self.announcement), "Holiday")
