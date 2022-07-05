# Please, fill the variables with your own file paths:

cred_path = '' # Example'/content/serviceKey.json'
agent_id = '' # Example: 'projects/financial-bot-webhook/locations/global/agents/...601e-b396-48ed-b819-59a0426ed65b'
Intents_CSV_Output = '' # Example'/content/taxonomy.csv'

from dfcx_scrapi.core.intents import Intents

i = Intents(cred_path, agent_id)

# Extracts all Intents and Training Phrases into a Pandas DataFrame:

df = i.bulk_intent_to_df(agent_id,'basic')

# Exports the data from the dataframe to a .csv file: 

df.to_csv(Intents_CSV_Output,index=False)
