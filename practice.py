class Mobile:
    def __init__(self, m):
        self.model = m

    def show_model(self):
        print("Model : ", self.model)

realme = Mobile('Realme X')
realme.show_model()