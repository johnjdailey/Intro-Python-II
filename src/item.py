#item.py



class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self):
        print(f"\nYou picked up the {self.name}.\n")
        
    def on_drop(self):
        print(f"\nYou dropped the {self.name}\n")

class TensorBook(Item):
    def __init__ (self):
        super().__init__(name='Tensorbook', description='GPU laptop built for deep learning. Powered by the NVIDIA RTX 2080 Super Max-Q GPU. Pre-installed with TensorFlow, PyTorch, Keras, CUDA, and cuDNN')
