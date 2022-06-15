# %%

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent_from_model_file
from parlai.agents.local_human.local_human import LocalHumanAgent
from agent import RRagent

# %%
def main():
    default = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})

    agent = RRagent(default)

    while (not agent.finished):
        question = input('Play with me, enter [DONE] for ending the episode, enter [EXIT] for ending the convo: \n>')
        print("agent:{}".format(agent.answer(question)))

if __name__ == '__main__':
    main()


