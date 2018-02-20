class InputValidator:
    missing = []

    def validate(self, data=[], compare=[]):
        self.missing = []
        for part in compare:
            if not part in data:
                self.missing.append(part)
        if len(self.missing) > 0:
            return False
        return True
