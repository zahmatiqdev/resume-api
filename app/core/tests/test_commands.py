from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        with patch("django.db.utils.ConnectionHandler.__getitem__") as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)
    # harzaman k db natone data begire, ye saniye sabr mikone va baed dobare say mikone k data begire
    # beyne darkhast ha delay vojod dare,
    # ma inja ba estefade az in decorator mikhaim in delay ro az beyn bebarim
    # dar vaghe hadf az hazf in saniye ha, bala bordane speed test darkhast
    # chera k 5 saniye bayad sabr mikardim

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # inja mige 5 bar error neshon bede va badesh, yani dafeye 6om return_value
            # bargardon.
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            # inja ham moshakhase k , 5bar try karde k connect she error shode
            # va dafeye 6om toneste connect beshe
            # pass call_count mishe 6
            self.assertEqual(gi.call_count, 6)
