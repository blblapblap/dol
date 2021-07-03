from app import app
import unittest

class Test(unittest.Testcase):
    def setup(self):
        self.app = app.test_client()

    def testReq(self):
        result = self.app.get("/")
        self.assertEqual(result.status_code, 200)

    def testContent(self):
        result = self.app.get("/")
        self.assertRegex(result.data.decode(), "Devops Laboratory")

if __name__ == "__main__":
    print("Initializing tests.")
    unittest.main(verbosity = 2)
