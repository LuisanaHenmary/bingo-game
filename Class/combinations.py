class Combinations:

    __combinations = []

    def __init__(self) -> None:
        self.generate_combinations()

    def generate_combinations(self):

        minor = 1
        major = 15

        for letter in ["B", "I", "N", "G", "O"]:
            for x in range(minor, major+1):
                self.__combinations.append({
                    "column": letter,
                    "number": x
                })
            minor+=15
            major+=15

    def get_combination(self,index):
        mov = self.__combinations.pop(index)

        letter = mov["column"]
        number = mov["number"]

        return (letter, number)

    def reboot(self):
        self.__combinations.clear()
        self.generate_combinations()

    def get_num_available(self):
        return len(self.__combinations)
