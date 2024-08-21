import unittest
from app import create_app, db
from app.models import EnergyUsage
from app.utils.data_generator import generate_energy_data
from datetime import datetime
import random


class TestDataGenerator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        db.session.query(EnergyUsage).delete()

    def tearDown(self):
        db.session.query(EnergyUsage).delete()
        db.session.commit()

    def test_generate_energy_data(self):
        # Run the function
        generate_energy_data()

        # Check that data was generated
        records = EnergyUsage.query.all()
        self.assertEqual(len(records), 504)

        # Verify that records have the expected attributes
        for record in records:
            self.assertIsNotNone(record.device_id)
            self.assertIsInstance(record.usage, float)
            self.assertIsInstance(record.timestamp, datetime)


if __name__ == '__main__':
    unittest.main()
