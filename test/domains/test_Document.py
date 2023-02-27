import unittest
from src.enums.DocumentType import DocumentType
from src.enums.MimeType import MimeType
from src.domains.Document import Document


class TestDocument(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "SELF",
            "mimeType": "image_jpeg",
            "name": "Sales",
            "base64": "123456789"
        }'''
        obj = Document.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = Document.create(
            type=DocumentType.SELF, mimeType=MimeType.image_jpeg, name="Sales", base64="123456789")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = Document.create(
            type=DocumentType.SELF, mimeType=MimeType.image_jpeg, name="Sales", base64="123456789")
        json = orig.to_json()
        dest = Document.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
