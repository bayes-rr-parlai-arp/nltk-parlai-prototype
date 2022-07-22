# %%

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent_from_model_file
from parlai.agents.local_human.local_human import LocalHumanAgent
from agent import RRagent
from parlai.scripts.interactive import setup_args, interactive
from projects.wizard_of_wikipedia.wizard_transformer_ranker.wizard_transformer_ranker import (
    WizardTransformerRankerAgent,
)
# %%
import torch
torch.cuda.empty_cache()

# %%
def main():
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
    #print(opt)

    default1 = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})
    default2 = create_agent_from_model_file(model_file='zoo:blender/blender_90M/model')
    default3 = create_agent_from_model_file(model_file='zoo:pretrained_transformers/model_poly/model',opt_overrides={'optimizer':'adam'})
    
    #default3 = create_agent_from_model_file(model_file='zoo:blender/blender_3B/model')
    #default3 = create_agent_from_model_file(model_file='zoo:blender/blender_400Mdistill/model')
    #default3 = create_agent_from_model_file(model_file='zoo:blended_skill_talk/ed_single_task/model',opt_overrides={'interactive_mode':True,'eval_candidates':'fixed'})
    #default3 = create_agent_from_model_file(model_file='zoo:hallucination/bart_fid_dpr/model',
    #opt_overrides={'doc_chunk_split_mode': ' word ', "eval_candidates": "vocab"})
    #default2 = create_agent_from_model_file(model_file='zoo:dialogue_unlikelihood/rep_convai2_ctxt_and_label/model')
    #default2 = create_agent_from_model_file(model_file='zoo:pretrained_transformers/poly_model_huge_wikito/model',opt_overrides={'eval_candidates':'fixed'})
    #default3 = create_agent_from_model_file(model_file='zoo:bart/bart_large/model')
    #default3 = create_agent_from_model_file(model_file='zoo:seeker/r2c2_blenderbot_400M/model')
    #default2 = create_agent_from_model_file(model_file='zoo:light/biranker_dialogue/model',
    #opt_overrides={'ignore_bad_candidates':True,'encode_candidate_vecs':True,'bert_aggregation':True,'eval_candidates':"fixed"})
    
    #default3 = create_agent_from_model_file(model_file='zoo:tutorial_transformer_generator/model',opt_overrides={'optimizer':'adam'})
    #default2 = create_agent_from_model_file(model_file='zoo:wizard_of_wikipedia/full_dialogue_retrieval_model/mode')
    #default3 = create_agent_from_model_file(model_file='zoo:hallucination/bart_fid_dpr/model')
    #opt_overrides={'doc_chunk_split_mode': ' word ', "eval_candidates": "vocab"} for poly
    

    agent1 = RRagent(default1)
    agent2 = RRagent(default2)
    agent3 = RRagent(default3)

    while (not agent1.finished):
        question = input('Play with me, enter [DONE] for ending the convo, enter [EXIT] for ending the programe: \n>')
        try:
            print("tutorial_reddit_model:{}".format(agent1.answer(question)))
            print("blender_90M:{}".format(agent2.answer(question)))
            print("polytransformer:{}".format(agent3.answer(question)))
        except StopIteration:
            if not agent1.finished:
                print("let's play again")
            else:
                print("Bye bye!")
if __name__ == '__main__':
    main()



# %%
