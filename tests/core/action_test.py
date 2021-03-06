from testify import setup, run
from testify import TestCase, assert_equal
from testify.utils import turtle

from tron.core import action

class TestAction(TestCase):

    @setup
    def setup_action(self):
        self.nodes = turtle.Turtle()
        self.action = action.Action("my_action", "doit", self.nodes)

    def test_from_config(self):
        config = turtle.Turtle(
            name="ted",
            command="do something",
            node="first")
        new_action = action.Action.from_config(config, dict(first={}))
        assert_equal(new_action.name, config.name)
        assert_equal(new_action.command, config.command)
        assert_equal(new_action.node_pool, {})
        assert_equal(new_action.required_actions, [])

    def test__eq__(self):
        new_action = action.Action(
            self.action.name, self.action.command, self.nodes)
        assert_equal(new_action, self.action)


if __name__ == '__main__':
    run()
