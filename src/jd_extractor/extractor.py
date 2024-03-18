class JDExtractor:
    def __init__(self, jd_path):
        self.jd_path = jd_path

    def extract(self):
        with open(self.jd_path, 'r') as file:
            jd = file.read()
        return jd