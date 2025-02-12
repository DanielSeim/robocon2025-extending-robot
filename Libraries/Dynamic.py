
class Dynamic():
    

    def get_keyword_names(self):
        return ['Dynamic keyword', 'Arguments']
    

    def run_keyword(self, name, args, kwargs):
        print(f"Running keyword '{name} with positional "
              f"arguments {args} and named arguments {kwargs}.")
        

    def get_keyword_arguments(self, name):
        if name == 'Arguments':
            return ['first', 'second=value']
        return []
    

    def get_keyword_source(self, name):
        return ':10'