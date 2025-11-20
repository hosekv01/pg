from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        if self.color == 'white':
            if self.is_position_on_board((row + 1, col)):
                moves.append((row + 1, col))
            if row == 2 and self.is_position_on_board((row + 2, col)):
                moves.append((row + 2, col))
        else:  # black pawn
            if self.is_position_on_board((row - 1, col)):
                moves.append((row - 1, col))
            if row == 7 and self.is_position_on_board((row - 2, col)):
                moves.append((row - 2, col))
        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        # Směry: diagonály
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        # Směry: horizontální a vertikální
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        # Směry: horizontální, vertikální a diagonály
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.is_position_on_board((r, c)):
                moves.append((r, c))
                r += dr
                c += dc
        return moves
    
    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'
    

class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        # Směry: horizontální, vertikální a diagonály (1 pole)
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dr, dc in directions:
            new_pos = (row + dr, col + dc)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
        return moves
    
    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    print("--- Knight Test ---")
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())

    print("\n--- Pawn Test (White) ---")
    pawn = Pawn("white", (2, 2))
    print(pawn)
    print(pawn.possible_moves())

    print("\n--- Bishop Test ---")
    bishop = Bishop("white", (4, 4))
    print(bishop)
    print(bishop.possible_moves())

    print("\n--- Rook Test ---")
    rook = Rook("black", (1, 1))
    print(rook)
    print(rook.possible_moves())

    print("\n--- Queen Test ---")
    queen = Queen("white", (4, 4))
    print(queen)
    print(queen.possible_moves())

    print("\n--- King Test ---")
    king = King("white", (5, 5))
    print(king)
    print(king.possible_moves())
