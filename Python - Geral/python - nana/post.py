class Post:
    def __init__(self, message, autor):
        self.message = message
        self.autor = autor
    
    def get_post_info(self):
        print(f"Post: {self.message} escrito por {self.autor}")