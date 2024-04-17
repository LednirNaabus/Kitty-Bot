import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# Supabase configs
url: str = os.environ["SUPABASE_PROJ_URL"]
key: str = os.environ["SUPABASE_API_KEY"]

class SupabaseClient:
    _instance = None

    @staticmethod
    def get_instance():
        if SupabaseClient._instance is None:
            SupabaseClient._instance = create_client(url, key)
        return SupabaseClient._instance