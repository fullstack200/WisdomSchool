from django.test import TestCase
from .models import Enquiries
from django.test import TestCase
from django.urls import reverse
from owner.models import Pictures, YearOfExam, DistinctionHolder, Announcements
from .models import Enquiries
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime

class EnquiriesModelTest(TestCase):

    def setUp(self):
        self.enquiry = Enquiries.objects.create(
            name="Master Ahmed",
            studentPhone="1234567890",
            studentEmail="ahmed@example.com",
            message="I would like to know more about the admissions process."
        )

    def test_enquiry_creation(self):
        """Test if enquiry is created with correct data"""
        self.assertEqual(self.enquiry.name, "Master Ahmed")
        self.assertEqual(self.enquiry.studentPhone, "1234567890")
        self.assertEqual(self.enquiry.studentEmail, "ahmed@example.com")
        self.assertEqual(self.enquiry.message, "I would like to know more about the admissions process.")

    def test_enquiry_str_method(self):
        """Test the __str__ method returns first 50 chars of name"""
        self.assertEqual(str(self.enquiry), "Master Ahmed")

    def test_blank_fields_allowed(self):
        """Test that null fields can be blank"""
        empty_enquiry = Enquiries.objects.create()
        self.assertIsNone(empty_enquiry.name)
        self.assertIsNone(empty_enquiry.studentPhone)
        self.assertIsNone(empty_enquiry.studentEmail)
        self.assertIsNone(empty_enquiry.message)

    def test_max_length_name(self):
        """Ensure name doesn't exceed 50 chars"""
        enquiry = Enquiries.objects.create(
            name="A" * 55,
            studentPhone="0000000000",
            studentEmail="a@example.com",
            message="Test"
        )
        self.assertEqual(enquiry.name[:50], str(enquiry))  # str() returns name[:50]

class StaticTemplateViewsTest(TestCase):
    def test_curriculum_view(self):
        response = self.client.get(reverse('curriculum'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'curriculum.html')

    def test_lifeatwisdom_view(self):
        response = self.client.get(reverse('lifeatwisdom'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lifeatwisdom.html')

    def test_gallery_view(self):
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')


class HomepageViewTest(TestCase):
    def test_homepage_view_renders(self):
        Announcements.objects.create(announcementName="Holiday", announcement="School closed tomorrow.")
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homePage.html')
        self.assertContains(response, "School closed tomorrow.")


class ContactViewTest(TestCase):
    def test_contact_form_submission(self):
        data = {
            'name': 'Ahmed',
            'studentPhone': '1234567890',
            'studentEmail': 'ahmed@example.com',
            'message': 'Admission info'
        }
        response = self.client.post(reverse('contact'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
        self.assertTrue(Enquiries.objects.filter(name='Ahmed').exists())


class YearOfExamViewTest(TestCase):
    def test_year_of_exam_view(self):
        year = YearOfExam.objects.create(year_of_exam=2022)
        DistinctionHolder.objects.create(
            toppers=year,
            name="Sara",
            marks=95,
            image=SimpleUploadedFile(name='test.jpg', content=b'', content_type='image/jpeg')
        )
        response = self.client.get(reverse('toppers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'toppers.html')
        self.assertContains(response, "Sara")


class PictureViewsTest(TestCase):
    def setUp(self):
        self.picture_map = {
            'classrooms': 'Classroom',
            'sports': 'Sports',
            'events': 'Event',
            'competitions': 'Competitions',
            'graduation': 'Graduation',
            'schooltrips': 'School Trip',
            'pe': 'PE',
        }

        for name, picture_type in self.picture_map.items():
            Pictures.objects.create(
                pictureType=picture_type,
                pictureName=f"{picture_type} Picture",
                pictureDate=datetime.date.today(),
                picture=SimpleUploadedFile(name='test.jpg', content=b'', content_type='image/jpeg')
            )

    def test_picture_type_views(self):
        for view_name in self.picture_map:
            response = self.client.get(reverse(view_name))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Picture")
