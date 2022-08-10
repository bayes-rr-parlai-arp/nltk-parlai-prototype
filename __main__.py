# %% import libraries

from parlai.core.agents import create_agent_from_model_file
# from projects.wizard_of_wikipedia.wizard_transformer_ranker.wizard_transformer_ranker import (
#     WizardTransformerRankerAgent,
# )
from RRagent import RRagent
from verbdetect import get_noun_and_verb, spacy_pos_tag
from pymongo import MongoClient
import datetime
# %% clean pytorch cache
import torch
torch.cuda.empty_cache()

# %%
'''
prototype ver 1.0

important version info:
python 3.8.13
ubuntu 22.04
pytorch 1.12.0
cuda 11.3
cudnn 8.3.2_0
parlai 1.6.0
pymongo 4.2.0

logic:
this prototype is devided into 3 parts:
__main__.py: interactive with 3 models, getting user input and output the response
RRagent.py: the agent class, which is used to respond the question and detect the conversation condition
verbdetect.py: the verb and noun detection function, which is used to detect the verb and noun in the user input

ashely 08 aug 2022

'''

# %% create the database
# let's connect to the localhost
client = MongoClient()

# # let's create a database 
db = client.parlaianswers

# collection for git issues
answers = db.answers

# print connection
print("""
Database
==========
{}

Collection
==========
{}
""".format(db, answers), flush=True
)
# %% main script
def main():
    

    ##### opt for wizarf of wikipedia model #####
    # parser = setup_args()
    # WizardTransformerRankerAgent.add_cmdline_args(parser, partial_opt=None)
    # parser.set_params(
    #     task='wizard_of_wikipedia',
    #     model='projects:wizard_of_wikipedia:wizard_transformer_ranker',
    #     model_file='models:wizard_of_wikipedia/full_dialogue_retrieval_model/model',
    #     datatype='test',
    #     n_heads=6,
    #     ffn_size=1200,
    #     embeddings_scale=False,
    #     delimiter=' __SOC__ ',
    #     n_positions=1000,
    #     legacy=True,
    #     eval_candidates='fixed',
    #     interactive_mode=True,
    # )
    # opt = parser.parse_args()
    # print(opt)

    # create agent from model file
    default1 = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})
    default2 = create_agent_from_model_file(model_file='zoo:blender/blender_90M/model')
    default3 = create_agent_from_model_file(model_file='zoo:pretrained_transformers/model_bi/model')

    ##### model test #####
    #default3 = create_agent_from_model_file(model_file='zoo:pretrained_transformers/model_poly/model',opt_overrides={'optimizer':'adam'})
    #default3 = create_agent_from_model_file(model_file='zoo:blender/blender_400Mdistill/model')
    #default3 = create_agent_from_model_file(model_file='zoo:blended_skill_talk/ed_single_task/model',opt_overrides={'interactive_mode':True,'eval_candidates':'fixed'})
    #default2 = create_agent_from_model_file(model_file='zoo:dialogue_unlikelihood/rep_convai2_ctxt_and_label/model')
    #default2 = create_agent_from_model_file(model_file='zoo:pretrained_transformers/poly_model_huge_wikito/model',opt_overrides={'eval_candidates':'fixed'})
    #default3 = create_agent_from_model_file(model_file='zoo:bart/bart_large/model')
    #default2 = create_agent_from_model_file(model_file='zoo:light/biranker_dialogue/model',
    #opt_overrides={'ignore_bad_candidates':True,'encode_candidate_vecs':True,'bert_aggregation':True,'eval_candidates':"fixed"})
    #default3 = create_agent_from_model_file(model_file='zoo:hallucination/bart_fid_dpr/model')
    #opt_overrides={'doc_chunk_split_mode': ' word ', "eval_candidates": "vocab"} for poly
    #defalut4 = create_agent_from_model_file(model_file='zoo:wizard_of_wikipedia/full_dialogue_retrieval_model/model', opt_overrides=opt)
    #default5 = create_agent_from_model_file(model_file='zoo:hallucination/bart_fid_dpr/model')
    #default7 = create_agent_from_model_file(model_file='zoo:blender/blender_400Mdistill/model')


    # load model
    agent1 = RRagent(default1)
    agent2 = RRagent(default2)
    agent3 = RRagent(default3)

    dialogue = {}
    i = 1
    # interactive
    while (not agent1.finished):
        # input question
        question = input('Play with me, enter [DONE] for ending the convo, enter [EXIT] for ending the programe, enter [SAVE] if you want to save the dialogue to the database: \n>')
        strattime = datetime.datetime.now()
        # answer question and process the answer by noun verb detection
        try:

                answer1 = agent1.answer(question)
                time1 = datetime.datetime.now()
                print("\n1 - tutorial_reddit_model: {}".format(answer1))
                noun, verb, adj = spacy_pos_tag(answer1)
                print("noun: {}".format(noun))
                print("verb: {}".format(verb))
                print("adj: {}\n".format(adj))

                answer2 = agent2.answer(question)
                time2 = datetime.datetime.now()
                print("2 - blender_90M: {}".format(answer2))
                noun, verb, adj = spacy_pos_tag(answer2)
                print("noun: {}".format(noun))
                print("verb: {}".format(verb))
                print("adj: {}\n".format(adj))

                answer3 = agent3.answer(question)
                time3 = datetime.datetime.now()
                print("3 - biencodertransformer: {}".format(answer3))
                noun, verb, adj = spacy_pos_tag(answer3)
                print("noun: {}".format(noun))
                print("verb: {}".format(verb))
                print("adj: {}\n".format(adj))
                
                selection = input('Please select the answer by 1, 2 or 3: \n>')
                # once the user input is done, record the time
                endtime = datetime.datetime.now()

                temp = {
                    "sequence":i,
                    "question": question,
                    "answer": {
                        "tutorial_reddit_model": answer1,
                        "blender_90M": answer2,
                        "biencodertransformer": answer3
                    },
                    "start_time": strattime,
                    "model_response_time": {
                        "tutorial_reddit_model": time1,
                        "blender_90M": time2,
                        "biencodertransformer": time3
                    },
                    "user_selection": selection,
                    "user_response_time":endtime
                }
                dialogue["question{}".format(i)] = temp
                i=i+1

        # manipulate the conversation
        except StopIteration:
            if not agent1.finished and not agent1.save:
                print("let's play again")
            # save the conversation to the database
            elif agent1.save and not agent1.finished:
                answers.insert_one(dialogue)
                agent1.save = False
                print("data saved")
            else:
                print("Bye bye!")


if __name__ == '__main__':
    main()


