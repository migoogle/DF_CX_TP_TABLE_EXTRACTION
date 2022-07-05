# Dialogflow CX Training Phrases Extraction
Python code to export the training phrases of a Dialogflow Agent to a .csv file.

## To install run the following commnands in your console:

1. Clone the repository:
```sh
git clone https://github.com/migoogle/DF_CX_TP_TABLE_EXTRACTION.git
```
2. Install the dependencies:
```sh
pip install dfcx-scrapi
```
(additionaly, you can install the dependencies with `pip install -r requirements.txt`)

## Setup your agent and output file:

3. In main.py file, fill in the paths to the Dialogflow Agent and the output file, e.g:
```python
cred_path = '/credentials/serviceKey.json'
agent_id = 'projects/financial-bot-webhook/locations/global/agents/...601e-b396-48ed-b819-59a0426ed65b'
Intents_CSV_Output = '/taxonomy.csv'
```

4. Run the code
```sh
python main.py
```
