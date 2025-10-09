import random
import copy

####### Cube;
class Cube:
    def __init__(self, faces="None"):
        self.orientation=[[5, 1, 4, 3], [5, 2, 4, 0], [5, 3, 4, 1], [5, 0, 4, 2], [0, 1, 2, 3], [2, 1, 0, 3]]
        self.rotmap=[[[2, 0], [2, 1], [2, 2], [0, 0], [1, 0], [2, 0], [0, 2], [0, 1], [0, 0], [2, 2], [1, 2], [0, 2]], [[2, 2], [1, 2], [0, 2], [0, 0], [1, 0], [2, 0], [2, 2], [1, 2], [0, 2], [2, 2], [1, 2], [0, 2]], [[0, 2], [0, 1], [0, 0], [0, 0], [1, 0], [2, 0], [2, 0], [2, 1], [2, 2], [2, 2], [1, 2], [0, 2]], [[0, 0], [1, 0], [2, 0], [0, 0], [1, 0], [2, 0], [0, 0], [1, 0], [2, 0], [2, 2], [1, 2], [0, 2]], [[2, 0], [2, 1], [2, 2], [2, 0], [2, 1], [2, 2], [2, 0], [2, 1], [2, 2], [2, 0], [2, 1], [2, 2]], [[0, 2], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0], [0, 2], [0, 1], [0, 0]]]
        self.sideTocmap=["G", "O", "B", "R", "W", "Y"]
        if(faces == "None"):
            self.cube=[[[self.sideTocmap[c]] * 3 for _ in range(3)] for c in range(6)]
        else:
            self.cube=faces

    def __str__(self):
        pstr=""
        for i in range(3):
            pstr += "    "
            for j in range(3):
                pstr += self.cube[5][i][j]
            pstr += "\n"
        for i in range(3):
            for j in range(3):
                pstr += self.cube[3][i][j]
            pstr += " "
            for j in range(3):
                pstr += self.cube[0][i][j]
            pstr += " "
            for j in range(3):
                pstr += self.cube[1][i][j]
            pstr += " "
            for j in range(3):
                pstr += self.cube[2][i][j]
            pstr += "\n"
        for i in range(3):
            pstr += "    "
            for j in range(3):
                pstr += self.cube[4][i][j]
            if(i != 2):
                pstr += "\n"
        return pstr

    def __rotateClock(self, side):
        temp=[self.cube[side][0][1], self.cube[side][0][2]]
        self.cube[side][0][1]=self.cube[side][1][0]
        self.cube[side][0][2]=self.cube[side][0][0]
        self.cube[side][0][0]=self.cube[side][2][0]
        self.cube[side][1][0]=self.cube[side][2][1]
        self.cube[side][2][0]=self.cube[side][2][2]
        self.cube[side][2][1]=self.cube[side][1][2]
        self.cube[side][1][2]=temp[0]
        self.cube[side][2][2]=temp[1]
        temp=[self.cube[self.orientation[side][0]][self.rotmap[side][0][0]][self.rotmap[side][0][1]], self.cube[self.orientation[side][0]][self.rotmap[side][1][0]][self.rotmap[side][1][1]], self.cube[self.orientation[side][0]][self.rotmap[side][2][0]][self.rotmap[side][2][1]]]
        for i in range(3):
            self.cube[self.orientation[side][0]][self.rotmap[side][0 + i][0]][self.rotmap[side][0 + i][1]]=self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]]
            self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]]=self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]]
            self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]]=self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]]
            self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]]=temp[0 + i]

    def __rotateAntiClock(self, side):
        temp=[self.cube[side][0][1], self.cube[side][0][2]]
        self.cube[side][0][1]=self.cube[side][1][2]
        self.cube[side][0][2]=self.cube[side][2][2]
        self.cube[side][1][2]=self.cube[side][2][1]
        self.cube[side][2][2]=self.cube[side][2][0]
        self.cube[side][2][0]=self.cube[side][0][0]
        self.cube[side][2][1]=self.cube[side][1][0]
        self.cube[side][0][0]=temp[1]
        self.cube[side][1][0]=temp[0]
        temp=[self.cube[self.orientation[side][0]][self.rotmap[side][0][0]][self.rotmap[side][0][1]], self.cube[self.orientation[side][0]][self.rotmap[side][1][0]][self.rotmap[side][1][1]], self.cube[self.orientation[side][0]][self.rotmap[side][2][0]][self.rotmap[side][2][1]]]
        for i in range(3):
            self.cube[self.orientation[side][0]][self.rotmap[side][0 + i][0]][self.rotmap[side][0 + i][1]]=self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]]
            self.cube[self.orientation[side][1]][self.rotmap[side][3 + i][0]][self.rotmap[side][3 + i][1]]=self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]]
            self.cube[self.orientation[side][2]][self.rotmap[side][6 + i][0]][self.rotmap[side][6 + i][1]]=self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]]
            self.cube[self.orientation[side][3]][self.rotmap[side][9 + i][0]][self.rotmap[side][9 + i][1]]=temp[0 + i]

    def __rotateMidClock(self, type):
        if(type == 'E'):
            temp=[self.cube[0][1][0], self.cube[0][1][1], self.cube[0][1][2]]
            for i in range(3):
                self.cube[0][1][0 + i]=self.cube[3][1][0 + i]
                self.cube[3][1][0 + i]=self.cube[2][1][0 + i]
                self.cube[2][1][0 + i]=self.cube[1][1][0 + i]
                self.cube[1][1][0 + i]=temp[0 + i]
        elif(type == 'M'):
            temp=[self.cube[0][0][1], self.cube[0][1][1], self.cube[0][2][1]]
            for i in range(3):
                self.cube[0][0 + i][1]=self.cube[5][0 + i][1]
                self.cube[5][0 + i][1]=self.cube[2][2 - i][1]
                self.cube[2][2 - i][1]=self.cube[4][0 + i][1]
                self.cube[4][0 + i][1]=temp[0 + i]
        elif(type == 'S'):
            temp=[self.cube[5][1][0], self.cube[5][1][1], self.cube[5][1][2]]
            for i in range(3):
                self.cube[5][1][0 + i]=self.cube[3][2 - i][1]
                self.cube[3][2 - i][1]=self.cube[4][1][2 - i]
                self.cube[4][1][2 - i]=self.cube[1][0 + i][1]
                self.cube[1][0 + i][1]=temp[0 + i]

    def __rotateMidAntiClock(self, type):
        if(type == 'E'):
            temp=[self.cube[0][1][0], self.cube[0][1][1], self.cube[0][1][2]]
            for i in range(3):
                self.cube[0][1][0 + i]=self.cube[1][1][0 + i]
                self.cube[1][1][0 + i]=self.cube[2][1][0 + i]
                self.cube[2][1][0 + i]=self.cube[3][1][0 + i]
                self.cube[3][1][0 + i]=temp[0 + i]
        elif(type == 'M'):
            temp=[self.cube[0][0][1], self.cube[0][1][1], self.cube[0][2][1]]
            for i in range(3):
                self.cube[0][0 + i][1]=self.cube[4][0 + i][1]
                self.cube[4][0 + i][1]=self.cube[2][2 - i][1]
                self.cube[2][2 - i][1]=self.cube[5][0 + i][1]
                self.cube[5][0 + i][1]=temp[0 + i]
        elif(type == 'S'):
            temp=[self.cube[5][1][0], self.cube[5][1][1], self.cube[5][1][2]]
            for i in range(3):
                self.cube[5][1][0 + i]=self.cube[1][0 + i][1]
                self.cube[1][0 + i][1]=self.cube[4][1][2 - i]
                self.cube[4][1][2 - i]=self.cube[3][2 - i][1]
                self.cube[3][2 - i][1]=temp[0 + i]
    
    def __move(self, type):
        if(type == 'U'):
            self.__rotateClock(5)
        elif(type == 'UP'):
            self.__rotateAntiClock(5)
        elif(type == 'D'):
            self.__rotateClock(4)
        elif(type == 'DP'):
            self.__rotateAntiClock(4)
        elif(type == 'R'):
            self.__rotateClock(1)
        elif(type == 'RP'):
            self.__rotateAntiClock(1)
        elif(type == 'L'):
            self.__rotateClock(3)
        elif(type == 'LP'):
            self.__rotateAntiClock(3)
        elif(type == 'F'):
            self.__rotateClock(0)
        elif(type == 'FP'):
            self.__rotateAntiClock(0)
        elif(type == 'B'):
            self.__rotateClock(2)
        elif(type == 'BP'):
            self.__rotateAntiClock(2)
        elif(type == 'E'):
            self.__rotateMidClock('E')
        elif(type == 'EP'):
            self.__rotateMidAntiClock('E')
        elif(type == 'M'):
            self.__rotateMidClock('M')
        elif(type == 'MP'):
            self.__rotateMidAntiClock('M')
        elif(type == 'S'):
            self.__rotateMidClock('S')
        elif(type == 'SP'):
            self.__rotateMidAntiClock('S')
        elif(type == 'x'):
            self.__move('LP')
            self.__move('MP')
            self.__move('R')
        elif(type == 'xP'):
            self.__move('L')
            self.__move('M')
            self.__move('RP')
        elif(type == 'y'):
            self.__move('U')
            self.__move('EP')
            self.__move('DP')
        elif(type == 'yP'):
            self.__move('UP')
            self.__move('E')
            self.__move('D')
        elif(type == 'z'):
            self.__move('F')
            self.__move('S')
            self.__move('BP')
        elif(type == 'zP'):
            self.__move('FP')
            self.__move('SP')
            self.__move('B')
        elif(type == 'u'):
            self.__move('U')
            self.__move('EP')
        elif(type == 'uP'):
            self.__move('UP')
            self.__move('E')
        elif(type == 'd'):
            self.__move('D')
            self.__move('E')
        elif(type == 'dP'):
            self.__move('DP')
            self.__move('EP')
        elif(type == 'r'):
            self.__move('R')
            self.__move('MP')
        elif(type == 'rP'):
            self.__move('RP')
            self.__move('M')
        elif(type == 'l'):
            self.__move('L')
            self.__move('M')
        elif(type == 'lP'):
            self.__move('LP')
            self.__move('MP')
        elif(type == 'f'):
            self.__move('F')
            self.__move('S')
        elif(type == 'fP'):
            self.__move('FP')
            self.__move('SP')
        elif(type == 'b'):
            self.__move('B')
            self.__move('SP')
        elif(type == 'bP'):
            self.__move('BP')
            self.__move('S')

    def doMoves(self, moves):
        # moves is sent to parseFormula() to get the object understandable instructions
        moves=parseFormula(moves)
        for m in moves:
            self.__move(m)

    def getFaces(self):
        return copy.deepcopy(self.cube)

####### SolverData;
# local perspective (for 0 - 3) moves to global moves
movedata={
    "R": ["R", "B", "L", "F", "R", "R"],
    "R'": ["R'", "B'", "L'", "F'", "R'", "R'"],
    "U": ["U", "U", "U", "U", "F", "B"],
    "U'": ["U'", "U'", "U'", "U'", "F'", "B'"],
    "L": ["L", "F", "R", "B", "L", "L"],
    "L'": ["L'", "F'", "R'", "B'", "L'", "L'"],
    "D": ["D", "D", "D", "D", "B", "F"],
    "D'": ["D'", "D'", "D'", "D'", "B'", "F'"],
    "F": ["F", "R", "B", "L", "D", "U"],
    "F'": ["F'", "R'", "B'", "L'", "D'", "U'"],
    "B": ["B", "L", "F", "R", "U", "D"],
    "B'": ["B'", "L'", "F'", "R'", "U'", "D'"],
    "M": ["M", "S", "M'", "S'", "M", "M"],
    "M'": ["M'", "S'", "M", "S", "M'", "M'"],
    "S": ["S", "M'", "S'", "M", "E", "E'"],
    "S'": ["S'", "M", "S", "M'", "E'", "E"]
}

move_pole_perspective={
    "R": ["R", "B", "L", "F", "R", "B", "L", "F"],
    "R'": ["R'", "B'", "L'", "F'", "R'", "B'", "L'", "F'"],
    "U": ["F", "R", "B", "L", "B", "L", "F", "R"],
    "U'": ["F'", "R'", "B'", "L'", "B'", "L'", "F'", "R'"],
    "L": ["L", "F", "R", "B", "L", "F", "R", "B"],
    "L'": ["L'", "F'", "R'", "B'", "L'", "F'", "R'", "B'"],
    "D": ["B", "L", "F", "R", "F", "R", "B", "L"],
    "D'": ["B'", "L'", "F'", "R'", "F'", "R'", "B'", "L'"],
    "F": ["D", "D", "D", "D", "U", "U", "U", "U"],
    "F'": ["D'", "D'", "D'", "D'", "U'", "U'", "U'", "U'"],
    "B": ["U", "U", "U", "U", "D", "D", "D", "D"],
    "B'": ["U'", "U'", "U'", "U'", "D'", "D'", "D'", "D'"],
    "M": ["M", "S", "M'", "S'", "M", "S", "M'", "S'"],
    "M'": ["M'", "S'", "M", "S", "M'", "S'", "M", "S"],
    "S": ["E", "E", "E", "E", "E'", "E'", "E'", "E'"],
    "S'": ["E'", "E'", "E'", "E'", "E", "E", "E", "E"]
}

# local perspective (for 0 - 3) positions to global positions
positionTransformData=[
    # target
    [
        # sides
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(4, 0, 0), (4, 0, 1), (4, 0, 2)], [(4, 1, 0), (4, 1, 1), (4, 1, 2)], [(4, 2, 0), (4, 2, 1), (4, 2, 2)]],
        [[(5, 0, 0), (5, 0, 1), (5, 0, 2)], [(5, 1, 0), (5, 1, 1), (5, 1, 2)], [(5, 2, 0), (5, 2, 1), (5, 2, 2)]]
    ],
    [
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(4, 0, 2), (4, 1, 2), (4, 2, 2)], [(4, 0, 1), (4, 1, 1), (4, 2, 1)], [(4, 0, 0), (4, 1, 0), (4, 2, 0)]],
        [[(5, 2, 0), (5, 1, 0), (5, 0, 0)], [(5, 2, 1), (5, 1, 1), (5, 0, 1)], [(5, 2, 2), (5, 1, 2), (5, 0, 2)]]
    ],
    [
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(4, 2, 2), (4, 2, 1), (4, 2, 0)], [(4, 1, 2), (4, 1, 1), (4, 1, 0)], [(4, 0, 2), (4, 0, 1), (4, 0, 0)]],
        [[(5, 2, 2), (5, 2, 1), (5, 2, 0)], [(5, 1, 2), (5, 1, 1), (5, 1, 0)], [(5, 0, 2), (5, 0, 1), (5, 0, 0)]]
    ],
    [
        [[(3, 0, 0), (3, 0, 1), (3, 0, 2)], [(3, 1, 0), (3, 1, 1), (3, 1, 2)], [(3, 2, 0), (3, 2, 1), (3, 2, 2)]],
        [[(0, 0, 0), (0, 0, 1), (0, 0, 2)], [(0, 1, 0), (0, 1, 1), (0, 1, 2)], [(0, 2, 0), (0, 2, 1), (0, 2, 2)]],
        [[(1, 0, 0), (1, 0, 1), (1, 0, 2)], [(1, 1, 0), (1, 1, 1), (1, 1, 2)], [(1, 2, 0), (1, 2, 1), (1, 2, 2)]],
        [[(2, 0, 0), (2, 0, 1), (2, 0, 2)], [(2, 1, 0), (2, 1, 1), (2, 1, 2)], [(2, 2, 0), (2, 2, 1), (2, 2, 2)]],
        [[(4, 2, 0), (4, 1, 0), (4, 0, 0)], [(4, 2, 1), (4, 1, 1), (4, 0, 1)], [(4, 2, 2), (4, 1, 2), (4, 0, 2)]],
        [[(5, 0, 2), (5, 1, 2), (5, 2, 2)], [(5, 0, 1), (5, 1, 1), (5, 2, 1)], [(5, 0, 0), (5, 1, 0), (5, 2, 0)]]
    ]
]

# white edge - other color pairs
whiteEdgePairs={
    (0, 0, 1): (5, 2, 1),
    (0, 1, 2): (1, 1, 0),
    (0, 2, 1): (4, 0, 1),
    (0, 1, 0): (3, 1, 2),
    (5, 0, 1): (2, 0, 1),
    (5, 1, 2): (1, 0, 1),
    (5, 2, 1): (0, 0, 1),
    (5, 1, 0): (3, 0, 1)
}

# moves for aligning the identified white edge to the correct global slot (if position is global), else local slot (if position is local) 
# as long as the relative orientation is matching
# more efficient than the proper version as i removed redundant "Dx" moves in the end
whiteEdgeDirectMoves={
    (0, 0, 1): ["FDR'", "FR'F'", "DF'LF", "F'LF"],
    (0, 1, 2): ["DR'", "R'", "D'R'", "F2LF2"],
    (0, 2, 1): ["F'DR'", "F'R'", "F'D'R'", "FL"],
    (0, 1, 0): ["D'L", "F2R'F2", "DL", "L"],
    (5, 0, 1): ["U2F2", "UR2", "B2", "U'L2"],
    (5, 1, 2): ["UF2", "R2", "U'B2", "U2L2"],
    (5, 2, 1): ["F2", "U'R2", "U2B2", "UL2"],
    (5, 1, 0): ["U'F2", "U2R2", "UB2", "L2"]
}

# proper moves for the alignment (without removal of any redundant "Dx"s)
whiteEdgeDirectMovesProper={
    (0, 0, 1): ["FDR'D'", "FR'F'", "DF'LFD'", "F'LF"],
    (0, 1, 2): ["DR'D'", "R'", "D'R'D", "F2LF2"],
    (0, 2, 1): ["F'DR'D'", "F'R'", "F'D'R'D", "FL"],
    (0, 1, 0): ["D'LD", "F2R'F2", "DLD'", "L"],
    (5, 0, 1): ["U2F2", "UR2", "B2", "U'L2"],
    (5, 1, 2): ["UF2", "R2", "U'B2", "U2L2"],
    (5, 2, 1): ["F2", "U'R2", "U2B2", "UL2"],
    (5, 1, 0): ["U'F2", "U2R2", "UB2", "L2"]
}

LyreLookUpSystem={
    "corners": [
        ((5, 0, 0), (3, 0, 0), (2, 0, 2), 1),
        ((5, 0, 2), (2, 0, 0), (1, 0, 2), 3),
        ((5, 2, 2), (1, 0, 0), (0, 0, 2), 5),
        ((5, 2, 0), (0, 0, 0), (3, 0, 2), 7)
    ],
    "corners-down": [
        ((4, 2, 0), (2, 2, 2), (3, 2, 0), 1),
        ((4, 2, 2), (1, 2, 2), (2, 2, 0), 3),
        ((4, 0, 2), (0, 2, 2), (1, 2, 0), 5),
        ((4, 0, 0), (3, 2, 2), (0, 2, 0), 7),
    ],
    "edges": [
        ((5, 0, 1), (2, 0, 1), 2),
        ((5, 1, 2), (1, 0, 1), 4),
        ((5, 2, 1), (0, 0, 1), 6),
        ((5, 1, 0), (3, 0, 1), 8)
    ],
    "edges-mid": [
        ((3, 1, 2), (0, 1, 0)),
        ((0, 1, 2), (1, 1, 0)),
        ((1, 1, 2), (2, 1, 0)),
        ((2, 1, 2), (3, 1, 0))
    ],
    "f2ldb": [
        ["1a", "U", "E", 1, 3, "U2RUR'URU'R'"],
        ["1a", "U", "E", 0, 3, "URU2R'URU'R'"],
        ["1a", "U", "X", 1, 3, "yU'L'U2LU'L'ULy'"],
        ["1a", "U", "X", 0, 3, "yU2L'U'LU'L'ULy'"],
        ["1a", "U", "E", 1, 1, "UFR'F'RURUR'"],
        ["1a", "U", "E", 0, 1, "RU2R'U'RUR'"],
        ["1a", "U", "X", 1, 1, "yL'U2LUL'U'Ly'"],
        ["1a", "U", "X", 0, 1, "FURU'R'F'RU'R'"],

        ["1a", "L", "E", 1, 3, "yUL'U'LU2L'ULy'"],
        ["1a", "L", "E", 0, 3, "yUL'U2LU2L'ULy'"],
        ["1a", "L", "X", 1, 3, "U'RUR'URUR'"],
        ["1a", "L", "X", 0, 3, "RUR'"],
        ["1a", "L", "E", 1, 1, "yU'L'ULy'"],
        ["1a", "L", "E", 0, 1, "RU'R'U2yL'U'Ly'"],
        ["1a", "L", "X", 1, 1, "R'U2R2UR'2UR"],
        ["1a", "L", "X", 0, 1, "U'RU'R'URUR'"],

        ["1a", "R", "E", 1, 3, "U'RU2R'U2RU'R'"],
        ["1a", "R", "E", 0, 3, "U'RUR'U2RU'R'"],
        ["1a", "R", "X", 1, 3, "yL'U'Ly'"],
        ["1a", "R", "X", 0, 3, "yUL'U'LU'L'U'Ly'"],
        ["1a", "R", "E", 1, 1, "UR'FRF'URUR'"],
        ["1a", "R", "E", 0, 1, "URU'R'"],
        ["1a", "R", "X", 1, 1, "yUL'ULU'L'U'Ly'"],
        ["1a", "R", "X", 0, 1, "yLU2L'2U'L2U'L'y'"],


        ["1b1", "U", "E", "URU'R'URU'R'URU'R'"],
        ["1b1", "U", "X", "U'R'FRF'RU'R'"],

        ["1b1", "L", "E", "URUR'U2RUR'"],
        ["1b1", "L", "X", "UF'U'FU'RUR'"],
        
        ["1b1", "R", "E", "U'RU'R'U2RU'R'"],
        ["1b1", "R", "X", "U'RUR'UyL'ULy'"],

        ["1b2", "D", "R", "U'R'FRF'RUR'"],
        ["1b2", "D", "L", "URU'R'U'yL'ULy'"],

        ["1b2", "L", "R", "RUR'U'RUR'"],
        ["1b2", "L", "L", "yL'ULU'L'ULy'"],

        ["1b2", "R", "R", "RU'R'URU'R'"],
        ["1b2", "R", "L", "yL'U'LUL'U'Ly'"],
    ]
}

ScythePatternMatcher={
    "target": [
        (2, 0, 2), (2, 0, 1), (2, 0, 0),
        (3, 0, 0), (5, 0, 0), (5, 0, 1), (5, 0, 2), (1, 0, 2),
        (3, 0, 1), (5, 1, 0), (5, 1, 1), (5, 1, 2), (1, 0, 1),
        (3, 0, 2), (5, 2, 0), (5, 2, 1), (5, 2, 2), (1, 0, 0),
        (0, 0, 0), (0, 0, 1), (0, 0, 2)
    ],
    # corners oriented
    "xyx-xyxyx-yxyyx-xyyyx-xxx": "M'UMU2M'UM",
    "xyx-xyxyx-xyyyx-xyxyx-xyx": "RUR'U'M'URU'Rw'",
    # cross
    "yxy-xxyxx-xyyyx-xxyxx-yxy": "RU2R'U'RUR'U'RU'R'",
    "xxy-yxyxx-xyyyx-yxyxx-xxy": "RU2R2U'R2U'R2U2R",
    "yxy-xxyxx-xyyyx-xyyyx-xxx": "R2D'RU2R'DRU2R",
    "yxx-xxyyx-xyyyx-xxyyx-yxx": "RwUR'U'Rw'FRF'",
    "xxx-yxyyx-xyyyx-xyyxx-xxy": "F'RwUR'U'Rw'FR",
    "xxx-yxyyx-xyyyx-xxyxy-yxx": "RU2R'U'RU'R'",
    "yxx-xxyxy-xyyyx-xyyxx-xxy": "RUR'URU2R'",
    # dot
    "xyx-xyxyx-yxyxy-xyxyx-xyx": "Rw'RURUR'U'Rw2R'2URU'Rw'",
    "yyx-xxxxy-yxyxy-yxxyx-xyx": "FwRUR'U'Fw'U'FRUR'U'F'",
    "xyx-yxxyx-yxyxy-xxxxy-yyx": "FwRUR'U'Fw'UFRUR'U'F'",
    "xyy-xyxxx-yxyxy-yxxyx-xyx": "RUR'UR'FRF'U2R'FRF'",
    "xyx-xyxyx-yxyxy-yxxxy-xyx": "Rw'RURUR'U'RwxR'2URU'x'",
    "yyy-xxxxx-yxyxy-xyxyx-xyx": "FRUR'Uy'R'U2R'FRF'",
    "xyy-yxxxx-yxyxy-yxxxx-xyy": "FRUR'U'SRUR'U'Fw'",
    "xyx-yxxxy-yxyxy-yxxxy-xyx": "RU2R'2FRF'U'2R'FRF'",
    # T
    "yyx-xxxyx-xyyyx-xxxyx-yyx": "RUR'U'R'FRF'",
    "xyx-yxxyx-xyyyx-yxxyx-xyx": "FRUR'U'F'",
    # P
    "xyx-yxxyx-yxyyx-yxyyx-xxx": "FwRUR'U'Fw'",
    "xyx-xyxxy-xyyxy-xyyxy-xxx": "Fw'L'U'LUFw",
    "yyx-xxxyx-yxyyx-xxyyx-yxx": "RDwL'Dw'R'ULwULw'",
    "yxx-xxyyx-yxyyx-xxxyx-yyx": "R'U'FURU'R'F'R",
    # W
    "yxx-xxyyx-xyyxy-xyxxy-xyx": "RUR'URU'R'U'R'FRF'",
    "xxy-xyyxx-yxyyx-yxxyx-xyx": "L'U'LU'L'ULULF'L'F",
    # L
    "xxx-yxyxy-yxyyx-yxxxy-xyx": "RwUR'URU'R'URU'2Rw'",
    "xyx-yxxxy-yxyyx-yxyxy-xxx": "Rw'U'RU'R'URU'R'U2Rw",
    "xyy-yxxxx-yxyyx-yxyxx-xxy": "RB'RBR'2U2FR'F'R",
    "xxy-yxyxx-yxyyx-yxxxx-xyy": "R'FR'F'R2U2yR'FRF'",
    "xxy-yxyxx-xyyxy-yxxxx-xyy": "FRUR'U'RUR'U'F'",
    "yxx-xxyxy-yxyyx-xxxxy-yyx": "F'L'U'LUL'U'LUF",
    # big lightning bolts
    "yyx-xxxyx-xyyyx-xyxxy-xyx": "LF'L'U'LUFU'L'",
    "xyy-xyxxx-xyyyx-yxxyx-xyx": "R'FRUR'U'F'UR",
    # C
    "xyx-yxxxy-xyyyx-xyxyx-xyx": "RUR'2U'R'FRURU'F'",
    "xxx-xyyxy-yxyxy-xyyxy-xxx": "R'U'R'FRF'UR",
    # Squares
    "yyx-xxxxy-yxyyx-yxyyx-xxx": "Rw'U2RUR'URw",
    "xxx-yxyyx-yxyyx-xxxxy-yyx": "RwU2R'U'RU'Rw'",
    # small lightning bolts
    "yxx-xxyxy-xyyxy-xyxxx-xyy": "RwUR'URU2Rw'",
    "xyy-yxxxx-xyyxy-xxyyx-yxx": "MU2R'U'RU'R'U2RUM'",
    "xyy-xyxxx-xyyxy-xxyxy-yxx": "Rw'U'RU'R'U2Rw",
    "yyx-xxxxy-yxyyx-xyyxx-xxy": "Rw'R2UR'URU2R'UM'",
    # fish
    "xxx-xyyxy-xyyxy-xxxyx-yyx": "FRU'R'U'RUR'F'",
    "xyx-xyxxy-yxyyx-xxyyx-yxx": "RU2R2FRF'RU2R'",
    "yyx-xxxyx-xyyxy-yxyxx-xxy": "RUR'UR'FRF'RU2R'",
    "xxy-yxyxx-xyyxy-xxxyx-yyx": "RUR'U'R'FR2UR'U'F'",
    # I
    "xyy-yxxxx-xyyyx-yxxxx-xyy": "FwRUR'U'RUR'U'Fw'",
    "yxx-xxyxy-yxyxy-xxyxy-yxx": "RUR'URDw'RU'R'F'",
    "yxy-xxyxx-yxyxy-xxyxx-yxy": "FwRUR'U'Fw'FRUR'U'RUR'U'F'",
    "xxx-yxyxy-yxyxy-yxyxy-xxx": "RU2R2U'RU'R'U2FRF'",
    # knight moves
    "yyx-xxxxy-xyyyx-xyxxx-xyy": "RwU'Rw'U'RwURw'y'R'UR",
    "xyx-yxxyx-xyyyx-xxxxy-yyx": "RwURw'RUR'U'RwU'Rw'",
    "xyy-yxxxx-xyyyx-xxxyx-yyx": "R'FRUR'F'Ry'RU'R'",
    "xyx-xyxxy-xyyyx-yxxxx-xyy": "Lw'U'LwL'U'LULw'ULw",
    # awkward
    "xyx-xyxyx-yxyyx-xxyxx-yxy": "RU'R'U2RUyRU'R'U'F'",
    "xyx-xyxyx-yxyyx-yxyxy-xxx": "R'2UR'B'RU'R'2ULwULw'",
    "xyx-xyxyx-xyyxy-xxyxx-yxy": "L'ULU'2L'U'y'L'ULUF",
    "xyx-xyxyx-xyyxy-yxyxy-xxx": "L2U'LBL'UL2U'Rw'U'Rw"
}

RunePatternMatcher={
    "shufflemap": [
        {"G": "G", "O": "O", "B": "B", "R": "R"},
        {"G": "G", "O": "O", "B": "R", "R": "B"},
        {"G": "G", "O": "B", "B": "O", "R": "R"},
        {"G": "G", "O": "B", "B": "R", "R": "O"},
        {"G": "G", "O": "R", "B": "O", "R": "B"},
        {"G": "G", "O": "R", "B": "B", "R": "O"},
        {"G": "O", "O": "G", "B": "B", "R": "R"},
        {"G": "O", "O": "G", "B": "R", "R": "B"},
        {"G": "O", "O": "B", "B": "G", "R": "R"},
        {"G": "O", "O": "B", "B": "R", "R": "G"},
        {"G": "O", "O": "R", "B": "G", "R": "B"},
        {"G": "O", "O": "R", "B": "B", "R": "G"},
        {"G": "B", "O": "G", "B": "O", "R": "R"},
        {"G": "B", "O": "G", "B": "R", "R": "O"},
        {"G": "B", "O": "O", "B": "G", "R": "R"},
        {"G": "B", "O": "O", "B": "R", "R": "G"},
        {"G": "B", "O": "R", "B": "G", "R": "O"},
        {"G": "B", "O": "R", "B": "O", "R": "G"},
        {"G": "R", "O": "G", "B": "O", "R": "B"},
        {"G": "R", "O": "G", "B": "B", "R": "O"},
        {"G": "R", "O": "O", "B": "G", "R": "B"},
        {"G": "R", "O": "O", "B": "B", "R": "G"},
        {"G": "R", "O": "B", "B": "G", "R": "O"},
        {"G": "R", "O": "B", "B": "O", "R": "G"}
    ],
    "target": [
        (2, 0, 2), (2, 0, 1), (2, 0, 0),
        (1, 0, 2), (1, 0, 1), (1, 0, 0),
        (0, 0, 2), (0, 0, 1), (0, 0, 0),
        (3, 0, 2), (3, 0, 1), (3, 0, 0)
    ],
    # permutations of edges only
    "BBBOGOGRGROR": "R2URUR'U'R'U'R'UR'",
    "BRBOGOGOGRBR": "M'2UM'2UM'U2M'2U2M'",
    "BBBOROGOGRGR": "RU'RURURU'R'U'R2",
    "OROGBGRORBGB": "M'2UM'2U2M'2UM'2",
    # permutations of corners only
    "GOGRGBORRBBO": "xR'UR'D2RU'R'D2R2x'",
    "BOGRGOGRBOBR": "x'RU'R'DRUR'D'RUR'DRU'R'D'x",
    "ROBOGOGRRBBG": "xR'2D2RUR'D2RU'Rx'",
    # swap one set of adjacent corners
    "BROGOBOGGRBR": "RU'R'U'RURDR'U'RD'R'U2R'",
    "ORRBOOGGGRBB": "R'UL'U2RU'R'U2RL",
    "OOGRBOGRRBGB": "RUR'U'R'FR2U'R'U'RUR'F'",
    "GOBORGRGRBBO": "R'U2RU'2R'FRUR'U'R'F'R2",
    "OOGRROGGRBBB": "RUR'F'RUR'U'R'FR2U'R'",
    "BGOGOBOBGRRR": "R'U'F'RUR'U'R'FR2U'R'U'RUR'UR",
    # swap one set of diagonal corners
    "RGOGOBORRBBG": "R'UR'U'yR'F'R2U'R'UR'FRF",
    "OORBBGRROGGB": "RUR'URUR'F'RUR'U'R'FR2U'R'U2RU'R'",
    "RBOGGBORRBOG": "FRU'R'U'RUR'F'RUR'U'R'FRF'",
    "ROOGBBORRBGG": "R'URU'R'F'U'FRUR'FR'F'RU'R",
    # G permutations (double cycles)
    "GBRBOGRRBOGO": "R2UR'UR'U'RU'R2DU'R'URD'",
    "GRRBOGRGBOBO": "R2U'RU'RUR'UR2D'URU'R'D",
    "OROGORBBGRGB": "F'U'FR2UwR'URU'RUw'R'2",
    "GBRBGGROBORO": "D'RUR'U'DR2U'RU'R'UR'UR2",
}

####### Helper;
def getScramble(length):
    vMoves = ['U', 'D', 'R', 'L', 'F', 'B'] # 'Uw', 'Dw', 'Rw', 'Lw', 'Fw', 'Bw', 'E', 'M', 'S', 'x', 'y', 'z']
    scr = ""
    for _ in range(length):
        scr += vMoves[int(random.random() * len(vMoves))]
        if(random.random() > 0.7):
            scr += '\''
    scr = condenseFormula(scr)
    return scr

def condenseFormula(form, advanced=True):
    if(not isValid(form)):
        return "ERROR"
    if(not advanced):
        return rawCondense(form)
    ans = ""
    tmp = ""
    for ch in form:
        if(ch == '(' or ch == ')'):
            if(len(tmp) > 0):
                ans += rawCondense(tmp)
            tmp = ""
            ans += ch
        else:
            tmp += ch
    if(len(tmp) > 0):
        ans += rawCondense(tmp)
    maxlevel = getMaxLevel(ans)
    for level in range(maxlevel, 0, -1):
        ans = parCondense(ans, level)
    return ans

def isValid(form):
    level = 0
    valid = True
    validAlpha = ['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b', 'w']
    boolAlpha = False
    boolPrime = False
    boolDec = False
    for ch in form:
        if(ch == '('):
            level += 1
            boolAlpha = False
            boolPrime = False
            boolDec = False
        elif(ch == ')'):
            if(level > 0):
                level -= 1
            else:
                valid = False
            boolAlpha = True
            boolPrime = False
            boolDec = False
        else:
            if(ch in validAlpha):
                boolAlpha = True
                boolPrime = False
                boolDec = False
            elif((ch == '\'' or ch == 'P') and boolAlpha and not boolPrime and not boolDec):
                if(boolDec):
                    boolAlpha = False
                    boolDec = False
                else:
                    boolPrime = True
            elif(ch.isdigit() and boolAlpha):
                boolDec = True
            else:
                valid = False
    if(level != 0):
        valid = False
    return valid

def getMaxLevel(form):
    level = 0
    maxlevel = 0
    for ch in form:
        if(ch == '('):
            level += 1
            if(level > maxlevel):
                maxlevel = level
        elif(ch == ')'):
            level -= 1
    return maxlevel

def parCondense(form, tar):
    form += '@'
    ans = ""
    temp = ""
    ref = ""
    refctr = 0
    ctr = 0
    for ch in form:
        if(ch == '('):
            ctr += 1
        if(ctr >= tar):
            temp += ch
        else:
            if(len(ref) > 0):
                ans += ref
                ans += str(refctr) if refctr > 1 else ""
                ref = ""
                refctr = 0
            ans += ch
        if(ch == ')'):
            if(ctr == tar):
                if(temp == ref):
                    refctr += 1
                else:
                    ans += ref
                    ans += str(refctr) if refctr > 1 else ""
                    ref = temp
                    refctr = 1
                temp = ""
            ctr -= 1
    ans = ans[:-1]
    return ans

def rawCondense(form):
    if(form.isdigit()):
        return form
    # string to 2d count array
    temp = []
    for i, item in enumerate(form):
        if(form[i].isalpha() and not form[i] == 'P' and not form[i] == 'w'):
            temp.append([form[i], ""])
        else:
            if(form[i].isdigit()):
                temp[-1][1] += form[i]
            else:
                temp[-1][0] += form[i]
    # int() of count
    for i, item in enumerate(temp):
        if(temp[i][1] == ""):
            temp[i][1] = 1
        else:
            temp[i][1] = int(temp[i][1])
    # removing anti moves and combining same moves
    while True:
        isChange = False
        for i in range(len(temp) - 1):
            if(isPrimePair(temp[i][0], temp[i + 1][0])):
                minv = min(temp[i][1], temp[i + 1][1])
                temp[i][1] -= minv
                temp[i + 1][1] -= minv
                if(temp[i + 1][1] == 0):
                    temp.pop(i + 1)
                if(temp[i][1] == 0):
                    temp.pop(i)
                isChange = True
                break
            elif(temp[i][0] == temp[i + 1][0]):
                temp[i][1] += temp[i + 1][1]
                temp.pop(i + 1)
                isChange = True
                break
            elif(temp[i][1] % 4 == 0):
                temp.pop(i)
                isChange = True
                break
        if(not isChange):
            break
    # limit count to 2 and inverse moves for 3
    for i, item in enumerate(temp):
        temp[i][1] = ((temp[i][1] - 1) % 4) + 1
        if(temp[i][1] == 3):
            if(temp[i][0][-1] == "\'"):
                temp[i][0] = temp[i][0][:-1]
            else:
                temp[i][0] += "\'"
            temp[i][1] = 1
        elif(temp[i][1] == 4):
            temp[i][1] = 0
    # 2d count array to string
    cform = ""
    for i, item in enumerate(temp):
        if(temp[i][1] > 0):
            cform += temp[i][0]
            if(temp[i][1] == 2):
                cform += '2'
    return cform

def isPrimePair(s1, s2):
    if(len(s1) >= len(s2)):
        a = s1
        b = s2
    else:
        a = s2
        b = s1
    if(len(a) - len(b) == 1):
        if(a[:len(b)] == b and a[-1] == "\'"):
            return True
    return False

def parseFormula(form, condense = True):
    if(not isValid(form)):
        return []
    if(condense):
        form = condenseFormula(form)
    moves = [ch for ch in form]
    vwMoves = ['U', 'D', 'R', 'L', 'F', 'B']
    # Convert w moves to base moves
    for i, item in enumerate(moves):
        if(moves[i] == 'w'):
            moves.pop(i)
            if(i > 0 and moves[i - 1] in vwMoves):
                moves[i - 1] = moves[i - 1].lower()
    # Convert outprimes to base moves
    vMoves = ['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b']
    cvm = -1
    for i, item in enumerate(moves):
        if(moves[i] in vMoves):
            cvm = i
        if(moves[i] == '\'' or moves[i] == 'P'):
            moves.pop(i)
            if(cvm >= 0):
                moves.insert(cvm + 1, "P")
                cvm = -1
    # Converting the characters into move blocks
    ans = []
    for i, item in enumerate(moves):
        if(moves[i] in vMoves):
            cm = moves[i]
            ctr = 1
            if(i + 1 < len(moves) and moves[i + 1] == 'P'):
                cm += 'P'
                ctr = 2
            cnt = 1
            if(i + ctr < len(moves) and moves[i + ctr] >= '0' and moves[i + ctr] <= '9'):
                cnt = int(moves[i + ctr])
            for _ in range(cnt):
                ans.append(cm)
    return ans

class Solver():
    def __init__(self, cube):
        self.cube=Cube(faces=cube.getFaces())
        self.__faces=self.cube.cube
        self.__forms=[]

    def solveCube(self, debug=False, optimize=False):
        # applying each part of the algorithm step by step
        # if debug is set to True, it prints the cube before and after applying the algorithm
        self.optimize=optimize
        if(debug):
            print("Before:")
            print(self.cube)
        try:
            self.__forms.append("--align--")
            self.__alignFaces()
            self.__forms.append("--base--")
            self.__baseCross()
            self.__forms.append("--first--")
            self.__firstLayer()
            self.__forms.append("--oll--")
            self.__oll()
            self.__forms.append("--pll--")
            self.__pll()
        except Exception as exception:
            print(exception.__class__.__name__ + " raised in the program (looks like something is broken...)")
        self.__checkComplete()
        if(debug):
            print("After:")
            print(self.cube)
    
    def getMoves(self, decorated=False):
        # get the moves that have been applied till now
        if(decorated):
            current=-1
            alignmentMoves=""
            baseCrossMoves=""
            firstLayerMoves=""
            ollMoves=""
            pllMoves=""
            for form in self.__forms:
                if(form == "--align--"):
                    current=0
                elif(form == "--base--"):
                    current=1
                elif(form == "--first--"):
                    current=2
                elif(form == "--oll--"):
                    current=3
                elif(form == "--pll--"):
                    current=4
                else:
                    if(current == 0):
                        alignmentMoves += form
                    elif(current == 1):
                        baseCrossMoves += form
                    elif(current == 2):
                        firstLayerMoves += form
                    elif(current == 3):
                        ollMoves += form
                    elif(current == 4):
                        pllMoves += form
            moves=f"{rawCondense(alignmentMoves)}{rawCondense(baseCrossMoves)}{rawCondense(firstLayerMoves)}{rawCondense(ollMoves)}{rawCondense(pllMoves)}"
            #if(bool(alignmentMoves)):
            #    moves += "For Alignment: " + rawCondense(alignmentMoves) + "\n"
            #if(bool(baseCrossMoves)):
            #    moves += "For Cross: " + rawCondense(baseCrossMoves) + "\n"
            #if(bool(firstLayerMoves)):
            #    moves += "For F2L: " + rawCondense(firstLayerMoves) + "\n"
            #if(bool(ollMoves)):
            #    moves += "For OLL: " + rawCondense(ollMoves) + "\n"
            #if(bool(pllMoves)):
            #    moves += "For PLL: " + rawCondense(pllMoves) + "\n"
            #moves=moves.strip()
            return moves
        else:
            moves=""
            for form in self.__forms:
                if(form != "--align--" and form != "--base--" and form != "--first--" and form != "--oll--" and form != "--pll--"):
                    moves += form + "\n"
            moves=moves.strip()
            return moves
    
    def isSolved(self):
        is_solved=True
        for i in range(6):
            tar=self.__faces[i][0][0]
            for row in range(3):
                for col in range(3):
                    if(tar != self.__faces[i][row][col]):
                        is_solved=False
        return is_solved
    
    def __checkComplete(self):
        # checks the completion of the cube solve
        isDone=True
        for i in range(6):
            tar=self.__faces[i][0][0]
            for row in range(3):
                for col in range(3):
                    if(tar != self.__faces[i][row][col]):
                        isDone=False
        if(not isDone):
            print("<<<ERROR>>>")
            print("The program was not able to solve the cube")
            print("Please contact me (saiakarsh193@gmail.com) and send the scramble used in order fix it")

    def __moveMapper(self, side, form, handle_x=False):
        # flexible moves-mapper from local perspective to global perspective
        moves=[]
        for ch in form:
            if(ch.isalpha() or ch.isdigit()):
                moves.append(ch)
            else:
                moves[-1] += ch
        onX=0
        for i, item in enumerate(moves):
            if(handle_x):
                if(item == "x"):
                    onX += 1
                    moves[i]=""
                elif(item == "x'"):
                    onX -= 1
                    moves[i]=""
                elif(onX != 0):
                    tmp=0 if(onX == 1) else 4
                    if moves[i] in move_pole_perspective:
                        moves[i]=move_pole_perspective[moves[i]][tmp + side]
                    continue
            if(self.optimize and item[0] == "y"):
                if(item == "y"):
                    side=(side + 1) % 4
                else:
                    side=(side - 1) % 4
                moves[i]=""
            if moves[i] in movedata:
                moves[i]=movedata[moves[i]][side]
        return ''.join(moves)

    def __positionMapper(self, target, side, row=None, col=None):
        # position mapper that maps perspective local positions to global positions
        if(type(side) is tuple):
            row=side[1]
            col=side[2]
            side=side[0]
        aside, arow, acol=positionTransformData[target][side][row][col]
        return self.__faces[aside][arow][acol]

    def __move(self, form):
        # applying moves to the cube and then storing it in a list
        if(bool(form)):
            self.cube.doMoves(form)
            self.__forms.append(form)

    def __alignFaces(self):
        # aligns the cube such that green is facing the screen (outwards) and yellow is facing upwards
        if(self.__faces[1][1][1] == "G"):
            self.__move("y")
        elif(self.__faces[2][1][1] == "G"):
            self.__move("y2")
        elif(self.__faces[3][1][1] == "G"):
            self.__move("y'")
        elif(self.__faces[4][1][1] == "G"):
            self.__move("x")
        elif(self.__faces[5][1][1] == "G"):
            self.__move("x'")
        if(self.__faces[1][1][1] == "Y"):
            self.__move("z'")
        elif(self.__faces[4][1][1] == "Y"):
            self.__move("z2")
        elif(self.__faces[3][1][1] == "Y"):
            self.__move("z")

    def __baseCross(self):
        # G O B R
        # find best slot/orientation to use rather than forcing it to a standard orientation
        t_slot=0
        t_score=0
        for i in range(4):
            score=bool(self.__positionMapper(i, 0, 2, 1) == "G" and self.__positionMapper(i, 4, 0, 1) == "W") + bool(self.__positionMapper(i, 1, 2, 1) == "O" and self.__positionMapper(i, 4, 1, 2) == "W") + bool(self.__positionMapper(i, 2, 2, 1) == "B" and self.__positionMapper(i, 4, 2, 1) == "W") + bool(self.__positionMapper(i, 3, 2, 1) == "R" and self.__positionMapper(i, 4, 1, 0) == "W")
            if(score > t_score):
                t_slot=i
                t_score=score
        # if score is 4 then all the white edges are correctly oriented but may not be properly aligned
        if(t_score == 4):
            if(t_slot == 1):
                self.__move("D'")
            elif(t_slot == 2):
                self.__move("D2")
            elif(t_slot == 3):
                self.__move("D")
            return
        #  0
        # 3 1
        #  2
        # find the color slot using the best parent (green as reference) slot
        slotToColorMap={"G": (0 + t_slot) % 4, "O": (1 + t_slot) % 4, "B": (2 + t_slot) % 4, "R": (3 + t_slot) % 4}
        # global slot to local perspective
        slot_to_persp=[[0, 1, 2, 3], [3, 0, 1, 2], [2, 3, 0, 1], [1, 2, 3, 0]]
        possible_moves=[]
        # find all the edges and calculate the moves
        for persp in range(4):
            for pos in whiteEdgePairs.keys():
                if(self.__positionMapper(persp, pos) == "W"):
                    # find the other color on this edge
                    target_other=whiteEdgePairs[pos]
                    target_other_color=self.__positionMapper(persp, target_other)
                    # color to global slot
                    g_slot=slotToColorMap[target_other_color]
                    # global slot to perspective slot
                    p_slot=slot_to_persp[persp][g_slot]
                    # edge move for pos in perspective to perspective slot (as good as the global)
                    edgeMove=whiteEdgeDirectMoves[pos][p_slot]
                    # apply perspective edge move globally
                    possible_moves.append(self.__moveMapper(persp, edgeMove))
        if(len(possible_moves) > 0):
            # find the smallest move and apply it
            smallest_move=""
            for move in possible_moves:
                if(len(move) < len(smallest_move) or smallest_move == ""):
                    smallest_move=move
            self.__move(smallest_move)
        else:
            # if no edge is found, then the miss-oriented edges are on the white face. So we check wrt the global slot
            #  which edge is out of alignment and move it out of the white face
            if(self.__positionMapper(t_slot, 0, 2, 1) != "G"):
                self.__move(self.__moveMapper(t_slot, "F2"))
            elif(self.__positionMapper(t_slot, 1, 2, 1) != "O"):
                self.__move(self.__moveMapper(t_slot, "R2"))
            elif(self.__positionMapper(t_slot, 2, 2, 1) != "B"):
                self.__move(self.__moveMapper(t_slot, "B2"))
            else:
                self.__move(self.__moveMapper(t_slot, "L2"))
        # repeatedly call this function till all the edges are oriented correctly
        self.__baseCross()

    def __getf2lMove(self, section, attrib_corner, attrib_edge, attrib_dist_sign=None, attrib_dist=None):
        # searches the dictionary and retrieves the move if found
        for f2lmove in LyreLookUpSystem["f2ldb"]:
            if(f2lmove[0] == section):
                if(section == "1a" and f2lmove[1] == attrib_corner and f2lmove[2] == attrib_edge and f2lmove[3] == attrib_dist_sign and f2lmove[4] == attrib_dist):
                    return f2lmove[5]
                if((section == "1b1" or section == "1b2") and f2lmove[1] == attrib_corner and f2lmove[2] == attrib_edge):
                    return f2lmove[3]
        return ""

    def __getCornerDetailBreakdown(self, c0, c1, c2):
        # standard corner details breakdown for finding attributes
        if(c0 == "W"):
            cx=0
            e0=c1
            e1=c2
        elif(c1 == "W"):
            cx=1
            e0=c0
            e1=c2
        else:
            cx=2
            e0=c0
            e1=c1
        if((e0 == "G" and e1 == "O") or (e0 == "O" and e1 == "G")):
            face2=0
        elif((e0 == "O" and e1 == "B") or (e0 == "B" and e1 == "O")):
            face2=1
        elif((e0 == "B" and e1 == "R") or (e0 == "R" and e1 == "B")):
            face2=2
        else:
            face2=3
        return cx, e0, e1, face2

    def __firstLayer(self):
        # conditions to check f2l completion
        con1=(self.__faces[0][1][0] == self.__faces[0][1][1] and self.__faces[0][1][1] == self.__faces[0][1][2] and 
        self.__faces[1][1][0] == self.__faces[1][1][1] and self.__faces[1][1][1] == self.__faces[1][1][2] and
        self.__faces[2][1][0] == self.__faces[2][1][1] and self.__faces[2][1][1] == self.__faces[2][1][2] and
        self.__faces[3][1][0] == self.__faces[3][1][1] and self.__faces[3][1][1] == self.__faces[3][1][2])
        con2=(self.__faces[0][2][0] == self.__faces[0][2][1] and self.__faces[0][2][1] == self.__faces[0][2][2] and 
        self.__faces[1][2][0] == self.__faces[1][2][1] and self.__faces[1][2][1] == self.__faces[1][2][2] and
        self.__faces[2][2][0] == self.__faces[2][2][1] and self.__faces[2][2][1] == self.__faces[2][2][2] and
        self.__faces[3][2][0] == self.__faces[3][2][1] and self.__faces[3][2][1] == self.__faces[3][2][2])
        con3=(self.__faces[0][1][1] == self.__faces[0][2][1] and self.__faces[1][1][1] == self.__faces[1][2][1] and
        self.__faces[2][1][1] == self.__faces[2][2][1] and self.__faces[3][1][1] == self.__faces[3][2][1])
        con4=(self.__faces[4][1][1] == self.__faces[4][0][0] and self.__faces[4][1][1] == self.__faces[4][0][2] and
        self.__faces[4][1][1] == self.__faces[4][2][0] and self.__faces[4][1][1] == self.__faces[4][2][2])
        if(con1 and con2 and con3 and con4):
            return
        found=False
        # f2l 1a
        # trying to find a corner-edge pair
        for corner in LyreLookUpSystem["corners"]:
            c0=self.__positionMapper(0, corner[0])
            c1=self.__positionMapper(0, corner[1])
            c2=self.__positionMapper(0, corner[2])
            if(c0 == "W" or c1 == "W" or c2 == "W"):
                cx, e0, e1, face2=self.__getCornerDetailBreakdown(c0, c1, c2)
                # orienting the corner and front face properly
                face2_to_corner=[5, 3, 1, 7]
                diff=int((face2_to_corner[face2] - corner[3]) / 2) % 4
                diff_to_move={0: "", 1: "U", 2: "U2", 3: "U'"}
                orient_move=[["", ""], ["y", "y'"], ["y2", "y2"], ["y'", "y"]]
                # top row edges
                for edge in LyreLookUpSystem["edges"]:
                    te0=self.__positionMapper(0, edge[0])
                    te1=self.__positionMapper(0, edge[1])
                    if((te0 == e0 and te1 == e1) or (te0 == e1 and te1 == e0)):
                        # found a corner-edge pair
                        # attrib_corner: U means up, L means left, R means right
                        attrib_corner="U" if(corner[cx][0] == 5) else ("L" if corner[cx][2] == 0 else "R")
                        attrib_edge=""
                        if(edge[0][0] == 5):
                            top_col_edge=te0
                        else:
                            top_col_edge=te1
                        # attrib_edge: E means same colors, X mean not same colors
                        if(attrib_corner != "U"):
                            if(c0 != "W" and corner[0][0] == 5):
                                top_col_cor=c0
                            elif(c1 != "W" and corner[1][0] == 5):
                                top_col_cor=c1
                            else:
                                top_col_cor=c2
                            attrib_edge="E" if(top_col_edge == top_col_cor) else "X"
                        else:
                            if(c0 != "W" and corner[0][2] == 0):
                                left_col_cor=c0
                            elif(c1 != "W" and corner[1][2] == 0):
                                left_col_cor=c1
                            else: 
                                left_col_cor=c2
                            attrib_edge="E" if(top_col_edge == left_col_cor) else "X"
                        # attrib_dist: manhattan distance between edge and corner
                        # attrib_dist_sign: 1 means clockwise corner to edge, 0 means anti-clockwise
                        if(edge[2] >= corner[3]):
                            attrib_dist=edge[2] - corner[3]
                            if(8 - attrib_dist < attrib_dist):
                                attrib_dist=8 - attrib_dist
                                attrib_dist_sign=0
                            else:
                                attrib_dist_sign=1
                        else:
                            attrib_dist=corner[3] - edge[2]
                            if(8 - attrib_dist < attrib_dist):
                                attrib_dist=8 - attrib_dist
                                attrib_dist_sign=1
                            else:
                                attrib_dist_sign=0
                        if(self.optimize):
                            self.__move(self.__moveMapper(face2, diff_to_move[diff] + self.__getf2lMove("1a", attrib_corner, attrib_edge, attrib_dist_sign, attrib_dist)))
                        else:
                            self.__move(diff_to_move[diff])
                            self.__move(orient_move[face2][0])
                            self.__move(self.__getf2lMove("1a", attrib_corner, attrib_edge, attrib_dist_sign, attrib_dist))
                            self.__move(orient_move[face2][1])
                        found=True
                        break
            if(found):
                break
        # f2l 1b1
        if(not found):
            # trying to find a corner-edge pair
            for corner in LyreLookUpSystem["corners"]:
                c0=self.__positionMapper(0, corner[0])
                c1=self.__positionMapper(0, corner[1])
                c2=self.__positionMapper(0, corner[2])
                if(c0 == "W" or c1 == "W" or c2 == "W"):
                    cx, e0, e1, face2=self.__getCornerDetailBreakdown(c0, c1, c2)
                    # orienting the corner and front face properly
                    face2_to_corner=[5, 3, 1, 7]
                    diff=int((face2_to_corner[face2] - corner[3]) / 2) % 4
                    diff_to_move={0: "", 1: "U", 2: "U2", 3: "U'"}
                    orient_move=[["", ""], ["y", "y'"], ["y2", "y2"], ["y'", "y"]]
                    # middle row edges
                    for edge in LyreLookUpSystem["edges-mid"]:
                        te0=self.__positionMapper(0, edge[0])
                        te1=self.__positionMapper(0, edge[1])
                        if(((te0 == e0 and te1 == e1) or (te0 == e1 and te1 == e0)) and ((te0 == self.__faces[edge[0][0]][1][1] and te1 == self.__faces[edge[1][0]][1][1]) or (te0 == self.__faces[edge[1][0]][1][1] and te1 == self.__faces[edge[0][0]][1][1]))):
                            attrib_corner="U" if(corner[cx][0] == 5) else ("L" if corner[cx][2] == 0 else "R")
                            attrib_edge="E" if (te0 == self.__faces[edge[0][0]][1][1] and te1 == self.__faces[edge[1][0]][1][1]) else "X"
                            if(self.optimize):
                                self.__move(self.__moveMapper(face2, diff_to_move[diff] + self.__getf2lMove("1b1", attrib_corner, attrib_edge)))
                            else:
                                self.__move(diff_to_move[diff])
                                self.__move(orient_move[face2][0])
                                self.__move(self.__getf2lMove("1b1", attrib_corner, attrib_edge))
                                self.__move(orient_move[face2][1])
                            found=True
                            break
                if(found):
                    break
        # f2l 1b2
        if(not found):
            # trying to find a corner-edge pair
            for corner in LyreLookUpSystem["corners-down"]:
                c0=self.__positionMapper(0, corner[0])
                c1=self.__positionMapper(0, corner[1])
                c2=self.__positionMapper(0, corner[2])
                if(self.__faces[corner[0][0]][1][1] in [c0, c1, c2] and self.__faces[corner[1][0]][1][1] in [c0, c1, c2] and self.__faces[corner[2][0]][1][1] in [c0, c1, c2]):
                    cx, e0, e1, face2=self.__getCornerDetailBreakdown(c0, c1, c2)
                    if(self.__faces[face2][1][1] == self.__faces[face2][1][2] and self.__faces[(face2 + 1) % 4][1][0] == self.__faces[(face2 + 1) % 4][1][1]):
                        continue
                    # orienting the corner and front face properly
                    orient_move=[["", ""], ["y", "y'"], ["y2", "y2"], ["y'", "y"]]
                    # # top row edges
                    for edge in LyreLookUpSystem["edges"]:
                        te0=self.__positionMapper(0, edge[0])
                        te1=self.__positionMapper(0, edge[1])
                        if((te0 == e0 and te1 == e1) or (te0 == e1 and te1 == e0)):
                            down_color, down_face=(te0, edge[0][0]) if(edge[0][0] != 5) else (te1, edge[1][0])
                            color_to_face2={"G": 0, "O": 1, "B": 2, "R": 3}
                            diff=down_face - color_to_face2[down_color]
                            diff_to_move={0: "", 1: "U", 2: "U2", 3: "U'", -1: "U'", -2: "U2", -3: "U"}
                            rl_map_face2=[[0, 1], [1, 2], [2, 3], [3, 0]]
                            attrib_corner="D" if(corner[cx][0] == 4) else ("L" if corner[cx][2] == 0 else "R")
                            attrib_edge="L" if(rl_map_face2[face2][0] == color_to_face2[down_color]) else "R"
                            if(self.optimize):
                                self.__move(self.__moveMapper(face2, diff_to_move[diff] + self.__getf2lMove("1b2", attrib_corner, attrib_edge)))
                            else:
                                self.__move(orient_move[face2][0])
                                self.__move(diff_to_move[diff])
                                self.__move(self.__getf2lMove("1b2", attrib_corner, attrib_edge))
                                self.__move(orient_move[face2][1])
                            found=True
                            break
                if(found):
                    break
        # non standard cases
        if(not found):
            # if no possible standard case is found, then the corners and edges need to be moved around
            # so we move the unsolved corners using a score system, which rates the shorter moves and moves which form pairs with higher score
            fmoves=[]
            for i in range(4):
                con1=self.__positionMapper(i, 0, 1, 2) == self.__positionMapper(i, 0, 2, 2) and self.__positionMapper(i, 1, 1, 0) == self.__positionMapper(i, 1, 2, 0) and self.__positionMapper(i, 4, 0, 2) == "W"
                con2=self.__positionMapper(i, 0, 1, 1) == self.__positionMapper(i, 0, 1, 2) and self.__positionMapper(i, 1, 1, 0) == self.__positionMapper(i, 1, 1, 1)
                corvd=[self.__positionMapper(i, 0, 2, 2), self.__positionMapper(i, 1, 2, 0), self.__positionMapper(i, 4, 0, 2)]
                corvu=[self.__positionMapper(i, 0, 0, 2), self.__positionMapper(i, 1, 0, 0), self.__positionMapper(i, 5, 2, 2)]
                if(con1 and con2):
                    continue
                if(con1 and not con2):
                    fmoves.append([10, self.__moveMapper(i, "RUR'")])
                if("W" in corvd):
                    if(self.__positionMapper(i, 0, 0, 1) in corvd and self.__positionMapper(i, 5, 2, 1) in corvd):
                        fmoves.append([6, self.__moveMapper(i, "URU'R'")])
                    fmoves.append([4, self.__moveMapper(i, "RU'R'")])
                if("W" in corvu):
                    if(self.__positionMapper(i, 0, 1, 2) in corvu and self.__positionMapper(i, 1, 1, 0) in corvu):
                        if(self.__positionMapper(i, 0, 0, 2) == "W"):
                            if(self.__positionMapper(i, 5, 2, 2) == self.__positionMapper(i, 0, 1, 2)):
                                fmoves.append([8, self.__moveMapper(i, "U'RU'R'")])
                            else:
                                fmoves.append([8, self.__moveMapper(i, "U2RUR'")])
                        elif(self.__positionMapper(i, 1, 0, 0) == "W"):
                            if(self.__positionMapper(i, 5, 2, 2) == self.__positionMapper(i, 0, 1, 2)):
                                fmoves.append([8, self.__moveMapper((i + 1) % 4, "U2L'U'L")])
                            else:
                                fmoves.append([8, self.__moveMapper((i + 1) % 4, "UL'UL")])
                        else:
                            if(self.__positionMapper(i, 0, 0, 2) == self.__positionMapper(i, 0, 1, 2)):
                                fmoves.append([9, self.__moveMapper(i, "RU'R'")])
                            else:
                                fmoves.append([4, self.__moveMapper(i, "U'RUR'")])
                fmoves.append([1, self.__moveMapper(i, "RU'R'")])
            fmoves=sorted(fmoves, key=lambda x: -x[0])
            self.__move(fmoves[0][1])
        self.__firstLayer()

    def __ollhash(self, values):
        # hashes and searches the dictionary and retrieves the move if found
        shash=""
        for val in values:
            if(val == "Y"):
                shash += "y"
            else:
                shash += "x"
        shash=shash[0: 3] + "-" + shash[3: 8] + "-" + shash[8: 13] + "-" + shash[13: 18] + "-" + shash[18: 21]
        if(shash in ScythePatternMatcher):
            return ScythePatternMatcher[shash]
        else:
            return None

    def __oll(self):
        # performs orientation of last layer
        for i in range(4):
            ocols=[]
            for pos in ScythePatternMatcher["target"]:
                ocols.append(self.__positionMapper(i, pos))
            form=self.__ollhash(ocols)
            if(bool(form)):
                if(self.optimize):
                    self.__move(self.__moveMapper(i, form, handle_x=True))
                else:
                    facemap=["", "y", "y2", "y'"]
                    self.__move(facemap[i])
                    self.__move(form)
                break
    
    def __pllhash(self, values):
        # hashes and searches the dictionary and retrieves the move if found
        for shuffle in RunePatternMatcher['shufflemap']:
            ohash=""
            for val in values:
                ohash += shuffle[val]
            if(ohash in RunePatternMatcher):
                return RunePatternMatcher[ohash]
        return None
    
    def __pll(self):
        # performs permutation of last layer
        for i in range(4):
            ocols=[]
            for pos in RunePatternMatcher["target"]:
                ocols.append(self.__positionMapper(i, pos))
            form=self.__pllhash(ocols)
            if(bool(form)):
                if(self.optimize):
                    self.__move(self.__moveMapper(i, form, handle_x=True))
                else:
                    facemap=["", "y", "y2", "y'"]
                    self.__move(facemap[i])
                    self.__move(form)
                break
        if(self.__faces[0][0][1] == self.__faces[1][1][1]):
            self.__move("U'")
        elif(self.__faces[0][0][1] == self.__faces[2][1][1]):
            self.__move("U2")
        elif(self.__faces[0][0][1] == self.__faces[3][1][1]):
            self.__move("U")


def getScramble(length):
    vMoves=['U', 'D', 'R', 'L', 'F', 'B'] # 'Uw', 'Dw', 'Rw', 'Lw', 'Fw', 'Bw', 'E', 'M', 'S', 'x', 'y', 'z']
    scr=""
    for _ in range(length):
        scr += vMoves[int(random.random() * len(vMoves))]
        if(random.random() > 0.7):
            scr += '\''
    scr=condenseFormula(scr)
    return scr

def condenseFormula(form, advanced=True):
    if(not isValid(form)):
        return "ERROR"
    if(not advanced):
        return rawCondense(form)
    ans=""
    tmp=""
    for ch in form:
        if(ch == '(' or ch == ')'):
            if(len(tmp) > 0):
                ans += rawCondense(tmp)
            tmp=""
            ans += ch
        else:
            tmp += ch
    if(len(tmp) > 0):
        ans += rawCondense(tmp)
    maxlevel=getMaxLevel(ans)
    for level in range(maxlevel, 0, -1):
        ans=parCondense(ans, level)
    return ans

def isValid(form):
    level=0
    valid=True
    validAlpha=['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b', 'w']
    boolAlpha=False
    boolPrime=False
    boolDec=False
    for ch in form:
        if(ch == '('):
            level += 1
            boolAlpha=False
            boolPrime=False
            boolDec=False
        elif(ch == ')'):
            if(level > 0):
                level -= 1
            else:
                valid=False
            boolAlpha=True
            boolPrime=False
            boolDec=False
        else:
            if(ch in validAlpha):
                boolAlpha=True
                boolPrime=False
                boolDec=False
            elif((ch == '\'' or ch == 'P') and boolAlpha and not boolPrime and not boolDec):
                if(boolDec):
                    boolAlpha=False
                    boolDec=False
                else:
                    boolPrime=True
            elif(ch.isdigit() and boolAlpha):
                boolDec=True
            else:
                valid=False
    if(level != 0):
        valid=False
    return valid

def getMaxLevel(form):
    level=0
    maxlevel=0
    for ch in form:
        if(ch == '('):
            level += 1
            if(level > maxlevel):
                maxlevel=level
        elif(ch == ')'):
            level -= 1
    return maxlevel

def parCondense(form, tar):
    form += '@'
    ans=""
    temp=""
    ref=""
    refctr=0
    ctr=0
    for ch in form:
        if(ch == '('):
            ctr += 1
        if(ctr >= tar):
            temp += ch
        else:
            if(len(ref) > 0):
                ans += ref
                ans += str(refctr) if refctr > 1 else ""
                ref=""
                refctr=0
            ans += ch
        if(ch == ')'):
            if(ctr == tar):
                if(temp == ref):
                    refctr += 1
                else:
                    ans += ref
                    ans += str(refctr) if refctr > 1 else ""
                    ref=temp
                    refctr=1
                temp=""
            ctr -= 1
    ans=ans[:-1]
    return ans

def rawCondense(form):
    if(form.isdigit()):
        return form
    # string to 2d count array
    temp=[]
    for i, item in enumerate(form):
        if(form[i].isalpha() and not form[i] == 'P' and not form[i] == 'w'):
            temp.append([form[i], ""])
        else:
            if(form[i].isdigit()):
                temp[-1][1] += form[i]
            else:
                temp[-1][0] += form[i]
    # int() of count
    for i, item in enumerate(temp):
        if(temp[i][1] == ""):
            temp[i][1]=1
        else:
            temp[i][1]=int(temp[i][1])
    # removing anti moves and combining same moves
    while True:
        isChange=False
        for i in range(len(temp) - 1):
            if(isPrimePair(temp[i][0], temp[i + 1][0])):
                minv=min(temp[i][1], temp[i + 1][1])
                temp[i][1] -= minv
                temp[i + 1][1] -= minv
                if(temp[i + 1][1] == 0):
                    temp.pop(i + 1)
                if(temp[i][1] == 0):
                    temp.pop(i)
                isChange=True
                break
            elif(temp[i][0] == temp[i + 1][0]):
                temp[i][1] += temp[i + 1][1]
                temp.pop(i + 1)
                isChange=True
                break
            elif(temp[i][1] % 4 == 0):
                temp.pop(i)
                isChange=True
                break
        if(not isChange):
            break
    # limit count to 2 and inverse moves for 3
    for i, item in enumerate(temp):
        temp[i][1]=((temp[i][1] - 1) % 4) + 1
        if(temp[i][1] == 3):
            if(temp[i][0][-1] == "\'"):
                temp[i][0]=temp[i][0][:-1]
            else:
                temp[i][0] += "\'"
            temp[i][1]=1
        elif(temp[i][1] == 4):
            temp[i][1]=0
    # 2d count array to string
    cform=""
    for i, item in enumerate(temp):
        if(temp[i][1] > 0):
            cform += temp[i][0]
            if(temp[i][1] == 2):
                cform += '2'
    return cform

def isPrimePair(s1, s2):
    if(len(s1) >= len(s2)):
        a=s1
        b=s2
    else:
        a=s2
        b=s1
    if(len(a) - len(b) == 1):
        if(a[:len(b)] == b and a[-1] == "\'"):
            return True
    return False

def parseFormula(form, condense=True):
    if(not isValid(form)):
        return []
    if(condense):
        form=condenseFormula(form)
    moves=[ch for ch in form]
    vwMoves=['U', 'D', 'R', 'L', 'F', 'B']
    # Convert w moves to base moves
    for i, item in enumerate(moves):
        if(moves[i] == 'w'):
            moves.pop(i)
            if(i > 0 and moves[i - 1] in vwMoves):
                moves[i - 1]=moves[i - 1].lower()
    # Convert outprimes to base moves
    vMoves=['U', 'D', 'R', 'L', 'F', 'B', 'E', 'M', 'S', 'x', 'y', 'z', 'u', 'd', 'r', 'l', 'f', 'b']
    cvm=-1
    for i, item in enumerate(moves):
        if(moves[i] in vMoves):
            cvm=i
        if(moves[i] == '\'' or moves[i] == 'P'):
            moves.pop(i)
            if(cvm >= 0):
                moves.insert(cvm + 1, "P")
                cvm=-1
    # Converting the characters into move blocks
    ans=[]
    for i, item in enumerate(moves):
        if(moves[i] in vMoves):
            cm=moves[i]
            ctr=1
            if(i + 1 < len(moves) and moves[i + 1] == 'P'):
                cm += 'P'
                ctr=2
            cnt=1
            if(i + ctr < len(moves) and moves[i + ctr] >= '0' and moves[i + ctr] <= '9'):
                cnt=int(moves[i + ctr])
            for _ in range(cnt):
                ans.append(cm)
    return ans

solution=[]
cb=Cube()
state=input("Start With Scrambled Input For Solved Like (F'LwRS'): ")
state=state.strip()
num_char=0
for char in state:
    if char in ["U","R","F","D","L","B","M","E","S","2","'","w"]:
        num_char+=1
if num_char==len(state):
    #cb.doMoves(getScramble(20))
    cb.doMoves(state)
    solver=Solver(cb)
    solver.solveCube(optimize=True)
    moves=solver.getMoves(decorated=True)
    i=0
    while i<=len(moves)-3:
        try:
            if moves[i+1]+moves[i+2]=="'2":
                moves=moves[0:i+1]+moves[i+2]+moves[i+3:]
        except:
            pass
        if moves[i+1]=="'":
            solution.append(f"{moves[i]}'")
            i+=2
        elif moves[i+1]=="2":
            solution.append(f"{moves[i]}2")
            i+=2
        elif moves[i+1]+moves[i+2]=="w'":
            solution.append(f"{moves[i]}w'")
            i+=3
        elif moves[i+1]=="w":
            solution.append(f"{moves[i]}w")
            i+=2
        else:
            solution.append(moves[i])
            i+=1
    if  i==len(moves)-1:
        solution.append(moves[-1])
    elif  i==len(moves)-2:
        solution.append(moves[-2]+moves[-1])
    solution=" ".join(solution)
    with open("Solution.txt","w") as f:
        f.write(f"Input: {state}\nSolution: {solution}")
    print(f"{solution}\nSolution saved to Solution.txt")