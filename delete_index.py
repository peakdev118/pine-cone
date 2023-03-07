import os
# pinecone module
import pinecone
# read env file
from dotenv import load_dotenv
#get api key of openai from .env
load_dotenv()

pine_cone_api_key = os.getenv("PINE_CONE_API_KEY")
pine_cone_environment = os.getenv("PINE_CONE_ENVIRONMENT")
print("pine_cone_api_key: ",pine_cone_api_key)
print("pine_cone_environment: ",pine_cone_environment)


pinecone.init(api_key=pine_cone_api_key, environment=pine_cone_environment)
try:
    pinecone.delete_index("podiodata")
    print('delete index')
except KeyError:
    print(KeyError)
