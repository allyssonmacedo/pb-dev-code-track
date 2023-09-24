class Client: 
    _clients_loaded = {} 
    _db_table = "table.sql" 
    
    def __new__(cls, client_id): 
        if (client := cls._clients_loaded.get(client_id, None)) is not None: 
            print(f"Retornando cliente existente {client_id}") 
            return client 
        
        else: 
            client = super().__new__(cls) 
            cls._clients_loaded[client_id] = client 
            client._init_from_table(client_id, cls._db_table) 
            return client 
        
    def _init_from_table(self, client_id, table): 
        self.id = client_id 
        self.email = "abc" 
        self.phone = "1234" 
        print(f"Carregando dados da {table} do {client_id}")


x = Client(0) 
y = Client(0) 
print(f"{True if x == y else False}") 
z = Client(1) 
print(f"{True if y == z else False}")