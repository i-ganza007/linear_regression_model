class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls,list_objs):
        if list_objs is None:
            list_objs = []
        else:
            with open("Base.json","w") as f:
                list_dictionaries = []
                for obj in list_objs:
                    list_dictionaries.append(obj.to_dictionary())
                f.write(cls.to_json_string(list_dictionaries))

    if __name__ == "__main__":
        b1 = Base(1)
        print(b1.id)

        b2 = Base()
        print(b2.id)

