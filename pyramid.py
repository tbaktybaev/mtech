class Pyramid:
    def __init__(self, input_str: str):
        """
        Инициализирует объект пирамиды.

        :param input_str: Строка с элементами пирамиды.
        """
        self.pyramid = sorted(list(input_str))
        self.levels = len(input_str)

    def compress(self):
        """
        Сжимает пирамиду до самого маленького размера.
        """
        while self.levels > 4:
            self.compress_one_level()
            self.levels //= 4

    def compress_one_level(self):
        """
        Сжимает один уровень пирамиды.
        """
        new_pyramid = []
        for i in range(0, len(self.pyramid), 4):
            sub_pyramid = self.pyramid[i:i + 4]
            if len(set(sub_pyramid)) == 1:
                new_pyramid.append(sub_pyramid[0])
            else:
                new_pyramid.extend(sub_pyramid)
        self.pyramid = new_pyramid

    def get_result_string(self):
        """
        Возвращает строковое представление результата сжатия.
        """
        return ''.join(self.pyramid)

    def save_result_to_file(self, output_file: str):
        """
        Записывает результат сжатия в файл.

        :param output_file: Имя файла для записи результата.
        """
        with open(output_file, 'w') as file:
            file.write(self.get_result_string())

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_str = file.read().strip()
    pyramid = Pyramid(input_str)
    pyramid.compress()
    pyramid.save_result_to_file('output.txt')
