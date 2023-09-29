#pip install azure-ai-textanalytics
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

credential = AzureKeyCredential("fbb193734ba24fc5abbaca0cc3dca6")
text_analytics_client = TextAnalyticsClient(endpoint="https://consultoria-analisis-texto.cognitiveservices.azure.com/", credential=credential)

documents = ["no entiendo lo que pasa aqui lo odio ", "XXXXXXXXXesta bien esto es genial lo que sea","esto  esta bien"]

response = text_analytics_client.analyze_sentiment(documents)

successful_responses = [doc for doc in response if not doc.is_error]

for result in successful_responses:
    print(result['confidence_scores'])


