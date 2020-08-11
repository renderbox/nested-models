from unittest import TestCase

from nestedmodels.models import NestedModel

class MyNestedTestModel(NestedModel):
    fields = ['index', 'other']
    index = None


class BasicModeTests(TestCase):

    def test_default_model(self):
        n = MyNestedTestModel()
        self.assertDictEqual(n.to_dict(), {'index':None})

    def test_pre_populated_model(self):
        n = MyNestedTestModel(index="three")
        self.assertDictEqual(n.to_dict(), {'index':"three"})

    def test_field_restrictions_model(self):
        n = MyNestedTestModel(index="three", other="more", frog="tree")
        self.assertDictEqual(n.to_dict(), {'index':"three", 'other':"more"})
