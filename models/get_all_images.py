import glob
from typing import List
import os

class GetAllImages:
 
    def __init__(self, path: str) -> None:
        self.path = path
        self.all_images = []
        extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg')
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith(extensions):
                  
                   self.all_images.append(os.path.join(root, file))
        
    def get_images(self) -> List[str]:
        print(len(self.all_images))
        return self.all_images