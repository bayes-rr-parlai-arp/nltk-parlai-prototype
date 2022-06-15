# %%

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent_from_model_file
from parlai.agents.local_human.local_human import LocalHumanAgent
from agent import RRagent

# %%
def main():
    default1 = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})
    default2 = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})
    default3 = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})

    agent1 = RRagent(default1)
    agent2 = RRagent(default2)
    agent3 = RRagent(default3)

    while (not agent1.finished):
        question = input('Play with me, enter [DONE] for ending the episode, enter [EXIT] for ending the convo: \n>')
        try:
            print("agent1:{}".format(agent1.answer(question)))
            print("agent2:{}".format(agent2.answer(question)))
            print("agent3:{}".format(agent3.answer(question)))
        except StopIteration:
            if not agent1.finished:
                print("let's play again")
            else:
                print("Bye bye!")
if __name__ == '__main__':
    main()


