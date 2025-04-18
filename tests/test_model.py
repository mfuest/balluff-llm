import unittest
from src.model.run_model import load_model, generate_response

class TestModel(unittest.TestCase):
    def test_model_loading(self):
        # Test if model can be loaded
        model, tokenizer = load_model("models/tinyllama-finetuned/")
        self.assertIsNotNone(model)
        self.assertIsNotNone(tokenizer)

    def test_generation(self):
        # Test if model can generate responses
        model, tokenizer = load_model("models/tinyllama-finetuned/")
        response = generate_response(model, tokenizer, "What is a BALLUFF sensor?")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main() 