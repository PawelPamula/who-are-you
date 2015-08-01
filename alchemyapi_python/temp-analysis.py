from alchemyapi import AlchemyAPI
import json, sys, pickle

file_name = "../tmp.txt"
counter = 0
with open(file_name, "r") as ff:
    tweets = ff.readlines()
    for tw in tweets:
        print tw
        demo_text = tw

        alchemyapi = AlchemyAPI()
        
        responseEntities = alchemyapi.entities('text', demo_text, {'sentiment': 1})
        pickle.dump(responseEntities, open("response_entities_"+ str(counter), 'wb'))
        
        responseKeywords = alchemyapi.keywords('text', demo_text, {'sentiment': 1})
        pickle.dump(responseKeywords, open("response_keywords_"+ str(counter), 'wb'))
        
        responseConcepts = alchemyapi.concepts('text', demo_text)
        pickle.dump(responseConcepts, open("response_concepts_"+ str(counter), 'wb'))
        #response = alchemyapi.sentiment_targeted('text', demo_text, 'Denver')
        responseLanguage = alchemyapi.language('text', demo_text)
        pickle.dump(responseLanguage, open("response_language_"+ str(counter), 'wb'))

        responseRelations = alchemyapi.relations('text', demo_text)
        pickle.dump(responseRelations, open("response_relations_"+ str(counter), 'wb'))

        responseCategory = alchemyapi.category('text', demo_text)
        pickle.dump(responseCategory, open("response_category_"+ str(counter), 'wb'))
        
        responseTaxonomy = alchemyapi.taxonomy('text', demo_text)
        pickle.dump(responseTaxonomy, open("response_taxonomy_"+ str(counter), 'wb'))
        
        responseCombined = alchemyapi.combined('text', demo_text)
        pickle.dump(responseCombined, open("response_combined_"+ str(counter), 'wb'))
        
        counter = counter+1

