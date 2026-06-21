from supabase import create_client
url = "https://gqguqdjjikwryraiovbg.supabase.co"
key = "sb_publishable_y16KZFuk6zMgatlIN40WzA_vcoiWP45"

supabase = create_client(url, key)
dados = supabase.table("contatos").select("*").execute()

print(dados.data)