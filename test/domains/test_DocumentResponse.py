import unittest
from src.enums.MimeType import MimeType
from src.enums.DocumentType import DocumentType
from src.domains.DocumentResponse import DocumentResponse


class TestDocumentResponse(unittest.TestCase):

    def test_from_json(self):
        json = '''{
            "type": "SELF",
            "mime_type": "image_jpeg",
            "name": "Sales",
            "url": "URL:http://"
        }'''
        obj = DocumentResponse.from_json(json)
        self.assertIsNotNone(obj)

    def test_to_json(self):
        orig = DocumentResponse.create(
            type=DocumentType.SELF, mime_type=MimeType.image_jpeg, name="Sales", url="URL:http://")
        json = orig.to_json()
        self.assertIsNotNone(json)

    def test_both(self):
        orig = DocumentResponse.create(
            type=DocumentType.SELF, mime_type=MimeType.image_jpeg, name="Sales", url="URL:http://")
        json = orig.to_json()
        dest = DocumentResponse.from_json(json)
        self.assertEqual(orig.__dict__, dest.__dict__)
