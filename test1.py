# import json
#
#
# class TextFile:
#     def read(self, file):
#         with open(file) as f:
#             return f.read()
#         pass
#
#     def write(self, file, lines):
#         pass
#
# class JSONFile:
#     def read(self, file):
#         with open(file) as f:
#             return json.load(f)
#
#         pass
#
#     def write(self, file, lines):
#         pass
#
# file_processor = JSONFile()
#
# data = file_processor.read("data.json")
# print(data)


class PlayerRecord:
    @staticmethod
    def get_top_10():
        pass

    @staticmethod
    def get_top_100():
        pass

    @staticmethod
    def add_record(record):
        pass

top_10 = PlayerRecord.get_top_100()


class Cat:
    def say(self):
        self.what_does_cat_say()

    @staticmethod
    def what_does_cat_say():
        print("myau")

Cat.what_does_cat_say()

cat1 = Cat()
cat1.what_does_cat_say()
cat1.say()