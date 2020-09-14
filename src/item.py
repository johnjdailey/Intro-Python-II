#item.py



class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def on_take(self):
        print(f"\nYou have picked up {self.name}.\n")
        raise NotImplementedError
        
    def on_drop(self):
        print(f"\nYou have dropped {self.name}\n")
        raise NotImplementedError


# Items that inherit from Item, but are also instantiated in adv.py as Items and then include 1 Item in each Room

class TensorBook(Item):
    def __init__ (self):
        super().__init__(name='Tensorbook', description='GPU laptop built for deep learning. Powered by the NVIDIA RTX 2080 Super Max-Q GPU. Pre-installed with TensorFlow, PyTorch, Keras, CUDA, and cuDNN')

class SolarPanels(Item):
    def __init__ (self):
        super().__init__(name="Solar Panels", description="This 2000 Watt portable solar array could be useful for your Tensorbook, or whatever you want to power")

class JetPack(Item):
    def __init__ (self):
        super().__init__(name="Jet Pack", description="USAF jetpack, full of fuel and ready to fly")

class LaserPickaxe(Item):
    def __init__ (self):
        super().__init__(name="Laser Pickaxe", description="A laser pickaxe designed for mining gold")

class TeslaCybertruck(Item):
    def __init__ (self):
        super().__init__(name="Tesla Cybertruck", description="Fully loaded Cybertruck, great for finding treasure!")
