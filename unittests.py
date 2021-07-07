



import utility
import unittest



_JITA = 30000142
_AMARR = 30002187
_AMI = 30005035
_AKORA = 30000163
_REISEN = 30000160
_MAILA = 30000162
_FLIET = 30004980
_A_ZLHX = 30003305

class Tests(unittest.TestCase):
    _u = None

    @classmethod
    def setUpClass(self):
        self._u = utility.Utility()

    def test_get_all_neighbours(self):
        self.assertEqual(6, len(self._u.get_neighbours(_AMARR)))
        
    def test_ami_best_entry_to_amarr(self):
        self.assertEqual(_AMI, self._u.get_best_entry_system(_JITA, _AMARR))

    def test_akora_best_entry_to_reisen(self):
        self.assertEqual(_AKORA, self._u.get_best_entry_system(_JITA, _REISEN))

    def test_jita_is_highsec(self):
        self.assertEqual(True, self._u.get_graph().is_highsec(_JITA))

    def test_ami_is_not_highsec(self):
        self.assertEqual(False, self._u.get_graph().is_highsec(_AMI))

    def test_maila_best_when_avoiding_akora(self):
        self.assertEqual(_MAILA, self._u.get_best_entry_system(_JITA, _REISEN, [int(_AKORA)]))

    def test_ignore_cyno_without_stations(self):
        pass

    def test_get_ly_distance_jita_fliet(self):
        self.assertEqual(9.287, self._u.get_ly_distance(_JITA, _FLIET))
    
    def test_get_jump_path_jita_a_z(self):
        self.assertEqual([_FLIET, _A_ZLHX], self._u.get_jump_route(_JITA, _A_ZLHX))
        
if __name__ == '__main__':
    unittest.main()




