class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = []
        columns = []
        boxes = []

        # Create 9 empty sets for rows, columns and boxes
        for i in range(9):
            rows.append(set())
            columns.append(set())
            boxes.append(set())

        for row in range(9):
            for column in range(9):
                value = board[row][column]

                # Ignore empty cells
                if value == ".":
                    continue

                # Calculate which of the 9 boxes this cell belongs to
                box_index = (row // 3) * 3 + (column // 3)

                # Check whether this value has appeared before
                if value in rows[row]:
                    return False

                if value in columns[column]:
                    return False

                if value in boxes[box_index]:
                    return False

                # Record the value
                rows[row].add(value)
                columns[column].add(value)
                boxes[box_index].add(value)

        return True