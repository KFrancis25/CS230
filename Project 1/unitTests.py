import URL_short
import unittest

class testProject1(unittest.TestCase):
    def testshortenURL(self):
        long_url = "ttps://www.youtube.com/watch?v=POH-vORSt2s&ab_channel=TheTromboneClips"
        temp = URL_short.shorten_url(long_url, URL_short.data)
        self.assertEqual(temp, "Invalid URL. Please enter a valid URL.")

if __name__ == "__main__":
    unittest.main()
