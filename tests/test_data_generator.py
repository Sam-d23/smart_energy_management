import unittest
from app import create_app, db
from app.models import EnergyUsage
from app.utils.data_generator import generate_energy_data


class TestDataGenerator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()
        if scheduler.running:
            scheduler.shutdown()

    def test_database_commit(self):
        generate_energy_data()
        # Check if data was committed to the database
        self.assertGreater(EnergyUsage.query.count(), 0)

    def test_generate_energy_data(self):
        generate_energy_data()
        # Check if data was generated correctly
        self.assertGreater(EnergyUsage.query.count(), 0)


if __name__ == '__main__':
    unittest.main()
