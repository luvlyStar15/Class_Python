# [START]
class MyMatrix:
    # 문제 1 #
    def getNewMatrix(self, N):
        # parameter 예외처리: N이 정수가 아닌 경우, N이 0 혹은 1 혹은 짝수 혹은 음수인 경우 #
        if type(N) != int or N == 0 or N == 1 or N % 2 == 0 or N < 0:
            return -1

        matrix = []
        for row in range(N):
            column = list()
            for col in range(N):
                column.append(0)
            matrix.append(column)
        depth = 0
        num = N
        while num > 0:
            for row in range(num):
                for col in range(num):
                    if row == 0 or col == 0 or num - 1 in (row, col):
                        matrix[row+depth][col+depth] = pow(N, depth+1)
            depth += 1
            num -= 2
        return matrix

    # 문제 2 #
    def saveFileMatrix(self, M):
        file1 = open('./MATRIX.TXT', 'a')
        text1 = "#LENGTH:{0}#\n".format(len(M))
        text2 = "{0}\n".format((str(M).replace(' ', ''))) 
        file1.write(text1)
        file1.write(text2)
        file1.close()

        file2 = open('./MATRIX.TXT', 'r')
        data = file2.read()
        num = data.count("LENGTH")
        file2.close()    
        return num
        
    # 문제 3 #
    def readFileMatrix(self, n):
        file = open('./MATRIX.TXT', 'r')
        text = file.readlines()
        file.close()
        try: 
            l = text.index("#LENGTH:{0}#\n".format(n))
        except:
            return -1
        str_list = text[l+1]
        final_list = []
        list1 = []
        list2 = []
        for i in range(len(str_list)):
            try: 
                a = int(str_list[i])
                list1.append(a)
            except:
                if list1 != []:
                    num = int(''.join(list(map(str,list1))))
                    list2.append(num)
                    list1.clear()
                else:
                    pass
            if len(list2) == n:
                final_list.append(list2.copy())
                list2.clear()
        return final_list  

    # 문제 4 #
    def readFileMaxValue(self):
        file = open('./MATRIX.TXT', 'r')
        text = file.readlines()
        file.close()
        max_length = 0
        for i in text:
            if i.startswith('#'):
                _, temp = i.split(':')
                length = int(temp.replace('#', ''))
                if length > max_length:
                    max_length = length

        v = max_length **(max_length//2 +1)
        max_tuple = (max_length, v)
        return max_tuple

    # 문제 5 #    
    def __init__(self, N = None):
        self.N = N
        if type(self.N) != int or self.N == 0 or self.N == 1 or self.N % 2 == 0 or self.N < 0:
                self.matrix =-1

        else:
            matrix = []
            for row in range(self.N):
                column = list()
                for col in range(self.N):
                    column.append(0)
                matrix.append(column)
            depth = 0
            num = self.N
            while num > 0:
                for row in range(num):
                    for col in range(num):
                        if row == 0 or col == 0 or num - 1 in (row, col):
                            matrix[row+depth][col+depth] = pow(self.N, depth+1)
                depth += 1
                num -= 2
            self.matrix = matrix
    
    def __eq__(self, other):
        # 객체 내부 정보 비교 #
        return self.matrix == other.matrix

    # 문제 6 #
    def applyGivenFunction(self, fn):
        for row in range(self.N):
            for col in range(self.N):
                v = self.matrix[row][col]
                self.matrix[row][col] = fn(v)
        return self.matrix

    def fn(self, num):
        """
        사용자 (프로그래머) 정의 함수

        :param num: 새로운 정수 값을 만들기 위한 정수 
        :return: 입력 받은 정수 + 2

        """

        return num + 2

    # 문제 7 #
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return -1

        my_matrix = self.matrix.copy()
        for i in range(len(my_matrix)):
            for k in range(len(my_matrix)):
                my_matrix[i][k] += other.matrix[i][k]
        return my_matrix

# 문제 8 #       
class MyDerivedMatrix(MyMatrix):
    def __init__(self, N = None):
        super().__init__(N)
    
    def getMemberMatrix(self):
        return self.matrix

# [END]

print("==> CLEAR!") # Don't remove this line
