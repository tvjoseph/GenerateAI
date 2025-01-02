'''
This is the script to test the RAG process
'''

if True:
    import os
    import sys

    #import colorama
    import datetime as dt
    import enum
    import json
    import re
    import requests
    import logging
    import pandas as pd

    from typing import List, Tuple, Optional, Dict, Any  # Dict, List, Optional, Tuple, Any

    #from vertexai.preview.vision_models import ImageGenerationModel
    import vertexai.preview.vision_models as vision_models
    import vertexai.preview.generative_models as generative_models
    from vertexai.preview.generative_models import GenerativeModel, Tool
    from vertexai.preview import rag
    from vertexai.generative_models import Image
    from PIL import Image as PIL_Image
    import random
    import json
    import pickle
    import tempfile
    import os
    pass

if True:
    # from 1password  - production studio - VertexAI
    # GCP_LOCATION = xxxxx
    # GCP_PROJ_ID = xxxxx
    GCP_AUTH_FILE = "/Users/thomasjoseph/Desktop/JMJTL/Projects/Gen_ai/key1.json"

    # Set path as env var
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GCP_AUTH_FILE

    pass

# Currently supports Google first-party embedding models
EMBEDDING_MODEL = "publishers/google/models/text-embedding-004"  # @param {type:"string", isTemplate: true}
embedding_model_config = rag.EmbeddingModelConfig(publisher_model=EMBEDDING_MODEL)

rag_corpus = rag.create_corpus(
    display_name="my-rag-corpus", embedding_model_config=embedding_model_config
)

guidelineDoc = "/Users/thomasjoseph/Desktop/JMJTL/Projects/Gen_ai/Optimise/Artwork Best Practice.pdf"
rag_file = rag.upload_file(
    corpus_name=rag_corpus.name,
    path=guidelineDoc,
    display_name="Dyson_guidelineDoc.pdf",
    description="Dyson brand guidelines",
)

print(rag_file)