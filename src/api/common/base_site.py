import dataclasses
import playwright

@dataclasses.dataclass
class site():
    def _post_init_(self):
        pass
    
    def _access_page(self, url:str):
        pass

    def search(self, keyword:list[str]):
        
