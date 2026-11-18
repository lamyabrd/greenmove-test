import time
import unittest

import agent


class TestAgent(unittest.TestCase):

    def test_memoire_limitee(self):
        # On simule 8 heures de mesures
        for i in range(8 * 3600 * 10):
            agent.data_buffer.append({"x": 0, "y": 0})
        self.assertEqual(len(agent.data_buffer), 3000)

    def test_boucle_non_bloquee(self):
        # 20 tours doivent durer environ 2 secondes, même si le réseau est lent
        debut = time.time()
        agent.main_loop(nb_tours=20)
        self.assertLess(time.time() - debut, 5)


if __name__ == "__main__":
    unittest.main()