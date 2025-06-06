from abc import ABC, abstractmethod

class Encryptor(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass

class CaesarEncryptor(Encryptor):
    def __init__(self, shift: int = 3):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        return "".join(
            chr((ord(c) - ord("a") + self.shift) % 26 + ord("a")) if c.islower() else
            chr((ord(c) - ord("A") + self.shift) % 26 + ord("A")) if c.isupper() else c
            for c in text
        )
    
class EncryptionManager:
    def __init__(self, encryptor: Encryptor):
        self.encryptor = encryptor
    def process(self, text: str) -> str:
        return self.encryptor.encrypt(text)

text = "Hello, I'm Nick!"
encryptor = EncryptionManager(CaesarEncryptor(shift=3))
print("Исходный код:", text)
print("Зашифрованный текст:", encryptor.process(text))
