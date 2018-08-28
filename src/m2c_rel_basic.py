### Re-used functions for relationship analysis
import pandas
from pandas import read_csv

###############################################################################
## Adds type to the table(so you the ID can be hashed with the type), Note, this 
## is not needed if a single term has multiple ids indicative of different types
## Used in: 'get sample for expert QC'
###############################################################################
def add_type_cols (al_data_imported):
    al_data_imported['refid1_type'] = al_data_imported['reltype'].str[:1]
    al_data_imported['refid2_type'] = al_data_imported['reltype'].str[2:]
    return(al_data_imported)



###############################################################################
## Separates out annotations submitted by test accounts
## Used in: 'get sample for expert QC'
###############################################################################
def split_out_testers(al_data_imported):
    ## Filter/handle annotations submitted by test accounts
    test_account_list = ['2', '5', '11', '13', '53', '223', '230', '338', '339', 
                     '340', '341', '342', '343', '344', '345', '346', '347', 
                     '348', '349', '350', '351', '352', '353', '354', '355', 
                     '356', '357', '358', '361', '443', '452', '492', '1204',
                     '1291','1351', '1630', '1631', '1702',
                     2, 5, 11, 13, 53, 223, 230, 338, 339, 
                     340, 341, 342, 343, 344, 345, 346, 347, 
                     348, 349, 350, 351, 352, 353, 354, 355, 
                     356, 357, 358, 361, 443, 452, 492, 1204,
                     1291, 1351, 1630, 1631, 1702
                     ]
    ## get annotations submitted only by non-test accounts
    filtered_results = al_data_imported[~al_data_imported['user_id'].isin(test_account_list)]
    ## get annotations submitted by test accounts to be thrown away later
    test_anns = al_data_imported[al_data_imported['user_id'].isin(test_account_list)]
    return(filtered_results, test_anns, test_account_list)

###############################################################################
## gets various summary stats and save the dataframes to a list of dataframes
## so that they can be called for later use. The stats are as follows:
## "unique_rel_counts" = Number of users per relation per pair of concepts PER document
## "concept_pair_counts" = Number of user votes per concept pair per document (regardless of how they voted)
## "unique_concept_pairs" = Number of unique concept pairs in the group (regardless of pmid and how they voted)
## "pmid_counts" = Number of PMIDs with submissions in this set
## "response_counts" = Count of the most frequently submitted responses based on relation type
## Used in: 'get sample for expert QC'
###############################################################################
def get_summary_stats(al_data_imported,summary_dict):
    al_data_imported.sort_values(['pmid'], ascending=[True], inplace=[True])
    unique_rel_counts = al_data_imported.groupby(['pmid','refid1','refid2','reltype',
                                                  'concept_pair','evtype']).size().reset_index(name='rel_counts')
    unique_rel_counts.sort_values(['pmid'], ascending=[True], inplace=[True])
    concept_pair_counts = al_data_imported.groupby(['pmid','concept_pair']).size().reset_index(name='user_votes')
    unique_concept_pairs = concept_pair_counts.groupby(['concept_pair']).size().reset_index(name='pmid_counts')
    unique_concept_pairs.sort_values(['pmid_counts'],ascending=[False],inplace=[True])
    pmid_counts = al_data_imported.groupby(['pmid']).size().reset_index(name='anns_per_pmid')
    response_counts = al_data_imported.groupby(['evtype','reltype']).size().reset_index(name='response_counts')
    ## Create list, dictionary of dataframes
    df_results = {'unique_rel_counts':unique_rel_counts, 
                  'concept_pair_counts':concept_pair_counts,
                  'unique_concept_pairs':unique_concept_pairs,
                  'pmid_counts':pmid_counts,
                  'response_counts':response_counts} 
    summary_dict['number of unique concept pairs']=len(unique_concept_pairs)
    summary_dict['number of pmids marked']=len(pmid_counts)
    return(df_results, summary_dict)
    

###############################################################################
## Imports the QC data
###############################################################################
def get_QC_data(savepath):
    i=0
    esample_df = pandas.DataFrame(columns=['concept_pair','counts','cpmid','pmid',
                                           'refid1','refid1_type','refid2','refid2_type',
                                           'reltype','conclusion','notes'])
    while i<4:
        esample = read_csv(savepath+'QCd samples/sample_'+str(i)+'_for_expert_ann.txt', delimiter='\t', header=0)
        esample_df = pandas.concat((esample_df,esample))
        i=i+1
    
    esample_df['pmid'] = esample_df['pmid'].astype(int)
    esample_df.drop("Unnamed: 0",axis=1,inplace=True)
    return(esample_df)    



###############################################################################
#### Import pubtator annotations to translate. Importing as objects because
#### Pandas can't do integers with NaN's, so it will convert gene ids to decimals if left as integers
#### Clean up pubtator annotation table after import
###############################################################################
def get_pub_anns(pubsource):
    print('Importing your data...')
    pubtator_tables = read_csv(pubsource, delimiter='\t', header=0, dtype=object)
    
    ## creating a column for identifier types
    pubtator_tables['id_type'] = 'no identifier'
    pubtator_tables['id_type'][pubtator_tables['identifier'].str.contains('MESH')==True] = 'MESH'
    pubtator_tables['id_type'][pubtator_tables['identifier'].str.contains("OMIM")==True] = 'OMIM'
    
    ## QC point: Checking for other identifiers in identifier column
    #tmpdf = pubtator_tables[pubtator_tables['identifier'].str.contains("MESH")==False]
    #tmpdf2 = tmpdf[tmpdf['identifier'].str.contains("OMIM")==False]
    #print(tmpdf2)
    
    ## merging all identifiers into identifier and identifier type columns
    pubtator_tables['identifier']=pubtator_tables['identifier'].str.replace('MESH:','')
    pubtator_tables['identifier']=pubtator_tables['identifier'].str.replace('OMIM:','')
    pubtator_tables['identifier'].fillna(pubtator_tables['NCBI Gene'], inplace=True)
    pubtator_tables['id_type'].loc[pandas.notnull(pubtator_tables['NCBI Gene'])] = 'EntrezGene'
    pubtator_tables['identifier'].fillna(pubtator_tables['NCBI Taxonomy'], inplace=True)
    pubtator_tables['id_type'].loc[pandas.notnull(pubtator_tables['NCBI Taxonomy'])] = 'Species'
    pubtator_tables['identifier'].fillna('no identifier', inplace=True)
    
    ## drop unnecessary columns
    del pubtator_tables['Unnamed: 0']
    del pubtator_tables['Unnamed: 0.1']
    del pubtator_tables['raw_data_index']
    
    pubtator_key = pubtator_tables[['pmid','identifier','id_type','text','type','length','offset']]
    return(pubtator_key)
