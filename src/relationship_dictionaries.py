"""
Dictionaries for translating/transforming relationship hash data
"""

    
###############################################################################
## Dictionaries for mapping relationships
###############################################################################


def load_RE_dictionaries():   
    rel_hash_dict = {
    "zl4RlTGwZM9Ud3CCXpU2VZa7eQVnJj0MdbsRBMGy":"c_1_broken",
    "RdKIrcaEOnM4DRk25g5jAfeNC6HSpsFZaiIPqZer":"c_2_broken",
    "8qota4u8hwtcyp65kz9zm0vjyuxwjt12sko084sn":"drug relates to disease",
    "72zuw4bgzz5dniepb3rmls23nsltwocbk274c98m":"drug (may) exacerbate(s) disease",
    "jilhvc5p2cy0atls8659a1fggjvvkmahwuspy2kr":"drug (may) treat(s) disease",
    "yrrb92b8vtjmcagjj4nx43sbj8wey2moqagk9ea5":"drug (may) increase(s) risk of disease",
    "jyiczzhhupcp7cmebl422ax5dxe1jkwuq647oaw2":"drug (may) cause(s) disease",
    "lt18qfxd1ehj7ymxb29wrv6qa41mocwe6eor9dna":"drug (may) prevent(s) disease",
    "nircjx48im90gy5uzqzc79gk3eagg7m36pti8oqi":"drug other relation, or relation unclear to disease",
    "4mzrh5ub3nla6b1ostx7qdparjl3lrd9o567ubif":"drug has no relation to disease",
    "ac1m2h0vxye2vuzv6cljr7be12o0d9oclir0kmr8":"drug relation to disease cannot be determined",
    "qq84lkjfh46gmx4a9n1jpwxwrmbajsy1qctb9u8j":"gene relates to disease",
    "u0q779rcrevnu6aki694dqka4fnfwvwqgpl06ybl":"gene altered expression is/may be associated with disease",
    "04110gzdcxz8niuv83ev08ut7lv0xep4iym5sxm5":"gene mutation is/may be associated with disease",
    "rhkmksv5jh0vn7p47uk3fwdior6mlgaubwh1l6ow":"gene and post-translational modifications are/may be associated with disease",
    "a86ujdunjj2gt0yeyyl027pp4yqbabotvmu0flwt":"gene other relation, or relation unclear to disease",
    "7aqs9bklotxhbq3r5dcofvsskiefb1yn2nkt1y4a":"gene has no relation to disease",
    "52d80rv4t0h0g14gb83oamjfm8h9rz19zl1ubzku":"gene relationship to disease cannot be determined",
    "txh8mu2mrnrffik893gr5h0ir7b1y7plgw94n4j7":"gene relates to drug",
    "am1wc2yvdcvwcb3yi298xesplbdktzku6wis49iw":"gene (may) affect(s) drug",
    "5ex6vuro19zeneiwlc8yze6dsq1coxvlpojolwgy":"gene is/may be affected by drug",
    "xdnolju6wacvakqnmz6237zwbh0ta3ftw8mdcp50":"gene other relation, or relation unclear to drug",
    "5mgmlk7rnbbd8q6amuapd3elwjpnbho0raegv59c":"gene has no relation to drug",
    "ytbg2u85xp0hayhv1sh6kjlonaag1n4kfgidp1o1":"gene relation to drug cannot be determined"
    }
    
    redundant_response_dict = {
    "drug other relation, or relation unclear to disease": "drug relates to disease",
    "drug relation to disease cannot be determined":"drug has no relation to disease",
    "gene other relation, or relation unclear to disease":"gene relates to disease",
    "gene relationship to disease cannot be determined":"gene has no relation to disease",
    "gene other relation, or relation unclear to drug": "gene relates to drug",
    "gene relation to drug cannot be determined":"gene has no relation to drug"
    }
    
    abbreviated_rels_dict = {
    'c_1_broken':'c1 broken', 
    'c_2_broken':'c2 broken', 
    'gene has no relation to disease':'g unrelated d', 
    'gene relates to disease':'g related d', 
    'gene and post-translational modifications are/may be associated with disease':'g post_trans d', 
    'gene mutation is/may be associated with disease':'g mutation d',
    'gene altered expression is/may be associated with disease':'g expression d', 
    'drug has no relation to disease':'c unrelated d', 
    'drug relates to disease':'c related d', 
    'drug (may) exacerbate(s) disease':'c exacerbate d', 
    'drug (may) treat(s) disease':'c treats d',
    'drug (may) increase(s) risk of disease':'c ups risk d',
    'drug (may) cause(s) disease':'c causes d',
    'drug (may) prevent(s) disease':'c prevents d',
    'gene has no relation to drug':'g unrelated c', 
    'gene relates to drug':'g related c',
    'gene (may) affect(s) drug':'g affects c',
    'gene is/may be affected by drug':'g affected by c'
    }
    
    
    abbreviated_rels_dict_4_hash = {
    'c_1_broken':'c1_broken', 
    'c_2_broken':'c2_broken', 
    'gene has no relation to disease':'g_unrelated_d', 
    'gene relates to disease':'g_related_d', 
    'gene and post-translational modifications are/may be associated with disease':'g_post_trans_d', 
    'gene mutation is/may be associated with disease':'g_mutation_d',
    'gene altered expression is/may be associated with disease':'g_expression_d', 
    'drug has no relation to disease':'c_unrelated_d', 
    'drug relates to disease':'c_related_d', 
    'drug (may) exacerbate(s) disease':'c_exacerbate_d', 
    'drug (may) treat(s) disease':'c_treats_d',
    'drug (may) increase(s) risk of disease':'c_ups_risk_d',
    'drug (may) cause(s) disease':'c_causes_d',
    'drug (may) prevent(s) disease':'c_prevents_d',
    'gene has no relation to drug':'g_unrelated_c', 
    'gene relates to drug':'g_related_c',
    'gene (may) affect(s) drug':'g_affects_c',
    'gene is/may be affected by drug':'g_affected_by_c'
    }
    
    concept_broken_dict = {
    'c_1_broken':'concept_broken', 
    'c_2_broken':'concept_broken',
    'zl4RlTGwZM9Ud3CCXpU2VZa7eQVnJj0MdbsRBMGy':'concept_broken',
    'RdKIrcaEOnM4DRk25g5jAfeNC6HSpsFZaiIPqZer':'concept_broken',
    'c1 broken':'concept_broken',
    'c2 broken':'concept_broken',
    'c1_broken':'concept_broken', 
    'c2_broken':'concept_broken'
    
    }
    
    concept_not_broken_dict = {
    'g_unrelated_d':'not_broken', 
    'g_related_d':'not_broken', 
    'g_post_trans_d':'not_broken', 
    'g_mutation_d':'not_broken',
    'g_expression_d':'not_broken', 
    'c_unrelated_d':'not_broken', 
    'c_related_d':'not_broken', 
    'c_exacerbate_d':'not_broken', 
    'c_treats_d':'not_broken',
    'c_ups_risk_d':'not_broken',
    'c_causes_d':'not_broken',
    'c_prevents_d':'not_broken',
    'g_unrelated_c':'not_broken', 
    'g_related_c':'not_broken',
    'g_affects_c':'not_broken',
    'g_affected_by_c':'not_broken'
    }
    
    return(rel_hash_dict,redundant_response_dict,abbreviated_rels_dict,abbreviated_rels_dict_4_hash,concept_broken_dict,concept_not_broken_dict)