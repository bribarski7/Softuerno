from django.test import TestCase
from polls.api import TemperatureApi

class TestTemperatureApi(TestCase):
    def testMin(self):
        self.assertEqual(TemperatureApi.minT(), 3)

    def testMax(self):
        self.assertEqual(TemperatureApi.maxT(), 8)

    def testAverage(self):
        self.assertEqual(TemperatureApi.averageT(), 5)