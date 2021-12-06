from csv import DictReader
import os
from typing import Sequence

from IPython.display import Javascript, display



pred_true_comparator_dir_path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(pred_true_comparator_dir_path, "PredTrueComparator.js")) as jsfile:
    pred_true_comparator_js_content = jsfile.read()
with open(os.path.join(pred_true_comparator_dir_path, "PredTrueComparator.css")) as jsfile:
    pred_true_comparator_css_content = jsfile.read().replace("\n", "")
css_string_var_declaration = f"var CSS_AS_STRING = '{pred_true_comparator_css_content}'\n\n" 

def clef_hipe_load_conllu_tsv_to_dict(filepath):
    with open(filepath) as csvfile:
        conllu_tsv = [r for r in DictReader(csvfile, delimiter="\t")]
    conllu_tsv = [r for r in conllu_tsv if len(r["TOKEN"])!=0 and not r["TOKEN"].startswith("#")]
    return conllu_tsv



def compare_pred_true(
    pred_data:Sequence[dict],      # prediction as a list of tokens, each token is a dict
    true_data:Sequence[dict],      # ground truth as a list of tokens, each token is a dict
    text_property:str,               # the entry of the token dict containing its text content
    compare_property:str,            # the entry containing the prediction/ground truth to compare
    separatorsProperty:str = "MISC", # the entry for line separators, which contains any combination of: EndOfLine, EndOfParagraph, NoSpaceAfter
    properties_to_display:Sequence[str] =[] # additional properties to display in additon to the pred-true comparison
):
    for p in pred_data:
        p["text"] = p[text_property]
    for t in true_data:
        t["text"] = t[text_property]
    predstr = str(pred_data).replace("\n", "")
    truestr = str(true_data).replace("\n", "")
    properties_to_display_str = str(properties_to_display).replace("\n", "")
    jsCode = css_string_var_declaration+pred_true_comparator_js_content+f'''
    element.append(visualizePredTrueComparison({predstr}, {truestr}, "{compare_property}", "{separatorsProperty}", {properties_to_display_str}))'''
    display(Javascript(
        jsCode
    ))
