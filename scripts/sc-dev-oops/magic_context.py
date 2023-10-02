class A:
    def __init__(self, file_name) -> None:
        self.file = file_name
    
    def __enter__(self):
        self.open_file = open(self.file, "w")
        return self.open_file

    def __exit__(self, exception_type, exception_value, traceback):
        self.open_file.close()
        del self.open_file

with A('test.txt') as f:
    f.write('test')