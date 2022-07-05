# Please, fill the variables with your own file paths:

cred_path = '/Users/miguens/DF_CX_TP_TABLE_EXTRACTION/credentials/financial-bot-webhook-b102e840a0a5.json' # Example'/credentials/serviceKey.json'
agent_id = 'projects/financial-bot-webhook/locations/global/agents/09f8fbf8-c100-48f7-abf3-eb9aca933779' # Example: 'projects/financial-bot-webhook/locations/global/agents/...601e-b396-48ed-b819-59a0426ed65b'
Intents_CSV_Output = 'taxonomy.csv' # Example'/taxonomy.csv'

from dfcx_scrapi.core.intents import Intents

i = Intents(cred_path, agent_id)

# Extracts all Intents and Training Phrases into a Pandas DataFrame:

df = i.bulk_intent_to_df(agent_id,'basic')

# Exports the data from the dataframe to a .csv file: 

df.to_csv(Intents_CSV_Output,index=False)
