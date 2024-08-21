import unittest
from datetime import datetime

from app import create_app, db
from app.models import EnergyUsage


class EnergyUsageTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_usage(self):
        usage = EnergyUsage(
                device_id=1234,
                usage=2.5,
                timestamp=datetime.now()
        )
        db.session.add(usage)
        db.session.commit()
        self.assertEqual(EnergyUsage.query.count(), 1)


if __name__ == '__main__':
    unittest.main()
