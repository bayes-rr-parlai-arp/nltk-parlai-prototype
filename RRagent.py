# %%
from parlai.core.agents import Agent
# %%
# class the agent

'''
logic:
1. get the model input from parlai agent model file
2. initialize the model with the input
3. input the user input to the model
4. get the output from the model by parlai agent's respond function
5. detect if there is [DONE] or [EXIT] or [SAVE] in the input, if so, restart the conversation or end the program or save the dialogue
6. return the output to the user

ashely 03 aug 2022
'''


class RRagent(Agent):
    def __init__(self, default):
        self.id = 'agent'
        self.default = default
        self.finished = False
        self.save = False

    # def observe(self, observation):
    #     return observation

    # def act(self, observation):
    #     reply = {
    #         'id': self.id,
    #         'text': self.default.respond(self.obervation['text'])
    #     }
    #     return reply
    
    def answer(self, question):
        if '[DONE]' in question:
            # let interactive know we're resetting
            raise StopIteration
        if '[EXIT]' in question:
            self.finished = True
            raise StopIteration
        if '[SAVE]' in question:
            # save the answer to the database
            self.save = True
            raise StopIteration
        
        return self.default.respond(question)


# %%
