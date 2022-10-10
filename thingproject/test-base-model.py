"""Tests for the solution of your exercise."""
"""DO NOT CHANGE THIS FILE!"""

from django.core.exceptions import ValidationError
from django.test import TestCase
from things.models import thing

class BaseModelTest(TestCase):
    def setUp(self):
        self.thing = thing(name="Foobar", description="Foobar thing", quantity=2)

    def test_valid_thing(self):
        self._assert_thing_is_valid("It was not possible to create a thing with the required attributes.")

    def _assert_thing_is_valid(self, message="A valid thing was rejected"):
        try:
            self.thing.full_clean()
        except ValidationError:
            self.fail(message)
