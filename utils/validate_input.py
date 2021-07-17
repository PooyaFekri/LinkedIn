class ValidateInput:
    def __init__(self):
        pass

    @staticmethod
    def is_empty(*args, **kwargs):
        for arg in args:
            if not arg:
                return True
        return False
