import copy

from democritus.exceptions import InvalidValueInSpecification
from democritus.messages import MessagesFactory
from democritus.states import StatesFactory


class GameFactory(object):
    @staticmethod
    def create(spec):
        spec_type = spec.get('type') or 'sim-max'
        if spec_type == 'sim-max':
            states_spec = spec.get_or_fail('states')
            messages_spec = spec.get_or_fail('messages')
            # utility_spec = spec.get('utility') or Specification.from_dict({})
            states = StatesFactory.create(states_spec)
            messages = MessagesFactory.create(messages_spec)
            return SimMaxGame(states, messages)
        else:
            raise InvalidValueInSpecification(spec, 'type', spec_type)


class Game(object):
    def __init__(self, states, messages, actions):
        self.states = states
        self.messages = messages
        self.actions = actions


class SimMaxGame(Game):
    def __init__(self, states, messages):
        actions = copy.deepcopy(states)
        Game.__init__(self, states, messages, actions)