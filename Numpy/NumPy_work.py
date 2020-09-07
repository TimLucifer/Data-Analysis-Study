import numpy as np


class ClassScore:
    result_list = []

    def math_deal(self, peoples):
        name_list = peoples.dtype.names
        loop = len(name_list)
        for index in range(1, loop):
            self.formats_deal(name_list[index], peoples[:][name_list[index]])

    def formats_deal(self, name, subject):
        formats = '{} | {} | {} | {} | {}'.format(name, np.min(subject), np.max(subject), np.var(subject),
                                                  np.std(subject))
        self.result_list.append(formats)

    def make_serializer(self):
        score_type = np.dtype({
            'names': ['name', 'chinese', 'math', 'english'],
            'formats': ['S32', 'i', 'i', 'i']
        })

        peoples = np.array([('S1', 66, 30, 65), ('S2', 95, 98, 85), ('S3', 93, 92, 96), ('S4', 90, 88, 77)],
                           dtype=score_type)
        print(sorted(peoples, key=lambda x: x[1] + x[2] + x[3], reverse=True))
        self.math_deal(peoples)


ClassScore = ClassScore()

if __name__ == '__main__':
    ClassScore.make_serializer()
    print(ClassScore.result_list)
