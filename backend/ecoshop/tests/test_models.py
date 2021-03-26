from django.test import TestCase

from ecoshop.models import Shop


class ShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Shop.objects.create(name="사랑이 자라는 가게", address="대전광역시 유성구 장동76",
                            content="친환경 비누 판매", heart_cnt=4, heart=True)

    def test_name_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_address_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_content_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_name_max_length(self):
        shop = Shop.objects.get(id=1)
        max_length = shop._meta.get_field('name').max_length
        self.assertEquals(max_length, 45)

    def test_address_max_length(self):
        shop = Shop.objects.get(id=1)
        max_length = shop._meta.get_field('address').max_length
        self.assertEquals(max_length, 100)

    def test_content_max_length(self):
        shop = Shop.objects.get(id=1)
        max_length = shop._meta.get_field('content').max_length
        self.assertEquals(max_length, 200)
