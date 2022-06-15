# %%
from parlai.core.agents import Agent

# %%
import torch
# %%
class RRagent(Agent):
    def __init__(self, default):
        self.id = 'transformer_generator'
        self.default = default
        self.finished = False

    def observe(self, observation):
        return observation

    def act(self, observation):
        reply = {
            'id': self.id,
            'text': self.default.respond(self.obervation['text'])
        }
        return reply
    
    def answer(self, question):
        if '[DONE]' in question:
            # let interactive know we're resetting
            raise StopIteration
        if '[EXIT]' in question:
            self.finished = True
            raise StopIteration
        
        return self.default.respond(question)
