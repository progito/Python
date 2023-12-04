import random 
import logging 


class MemoryAddress:
    def __init__(self, default_value: str) -> None:
        self.value = default_value
    # другие методы класса
    
    
class WA:
    def __init__(self, address: str) -> None:
        pass
    # другие методы класса


if __name__ == '__main__':
    obj = WA("\x501\x51\x52\x5344\x54\x55\x5655\x57\x59\x67")
    print(obj.get_address())
    # Change the address
    obj.set_address("\x60\x61\x62\x63\x64\x65")
    print(obj.get_address())
    # Call ssvalue method
    obj.ssvalue()
