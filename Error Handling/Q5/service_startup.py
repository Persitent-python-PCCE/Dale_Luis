def get_json_parser():
    
    try:
        import orjson
        return orjson
    except ModuleNotFoundError as me:
        import json
        print("orjson not available -- falling back to standart json")
        return json



class ReportService:
    def __init__(self):
        self.connected=False
    def run_query(self):
        if not self.connected:
            raise RuntimeError("Database connection not established")
        return "query_result"
    
def generate_report(service):
    try:
        service.run_query()
    except RuntimeError as re:
        print(re)
        pass


get_json_parser()
generate_report(ReportService())