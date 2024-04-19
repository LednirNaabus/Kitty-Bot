from config.supabase_config import SupabaseClient

sbclient = SupabaseClient.get_instance()

list_files = sbclient.storage.from_('images').list('cats')
file_names = [file['name'] for file in list_files]
get_public_urls = [sbclient.storage.from_('images').get_public_url(f'cats/{url}') for url in file_names]

print("INSERTING DATA INTO TEST_TABLE...")
for i in range(len(list_files)):
    data = sbclient.table('cat_pics').insert({
        "id" : i+1,
        "file_name" : f"{i+1}.jpg",
        "image_url" : f"{get_public_urls[i]}"
    }).execute()
response = sbclient.table('cat_pics').select('*').execute()
print(f"DATA INSERTED! {response}")