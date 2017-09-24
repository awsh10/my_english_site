import pickle
from time import time
import os
import glob

# vertic = [str(v) for v in range(max_ - 1, -1, -1)]
# board = [v + ':' + g for v in vertic for g in goriz]
goriz = []
vertic = []
def remove_files_from_folder_func(path):
    files = glob.glob(path)
    for f in files:
        os.remove(f)

def bord_create_func(path, board_size=10000, elements_max=None):
    """
    Creates full board with board_size ** 2 elements
    :param board_size: size of board
    :param elements_max: max quantity of elements in a subboard
    :return:
    """
    remove_files_from_folder_func(path + '*')
    if not elements_max:
        elements_max = board_size
    goriz = [str(g) for g in range(board_size)]
    # board = [v + g for v in vertic for g in goriz]
    elements_total = board_size ** 2
    lines_count = elements_max // board_size
    int_part = board_size // lines_count
    rest = board_size % lines_count

    len_board = 0
    def vert_board_func(value_max, value_min, iteration):
        """
        The function creates subboard from value_max to value_min of the vertical and all values of the gorizontal,
        and inserts the subboard to a file with a special name
        """
        nonlocal len_board
        vertic_part = [str(v) for v in range(value_max, value_min, -1)]
        board = [v + ':' + g for v in vertic_part for g in goriz]
        # len_board += len(board )
        with open('{}{}.pkl'.format(path, iteration), 'wb') as file_my:
            pickle.dump(board, file_my, pickle.HIGHEST_PROTOCOL)
        return board

    if rest:
        value_max = board_size - 1
        value_min = board_size - rest - 1
        board = vert_board_func(value_max, value_min)
        # print(board[0])

    for k in range(int_part * lines_count, 0, -lines_count):
        value_max = k - 1
        value_min = (k - lines_count) -1
        board = vert_board_func(value_max, value_min, k - 1)

def fields_rest_func(field, fields_set):
    """ Creates new rest list of free fields for the given field.  Finds diagonal, vertical and gorizontal fields
        binded with this field and subtracts them from the input board_rest_set """



    goriz_start = goriz.index(field[1])
    vertic_start = vertic.index(field[0])

    goriz_left = goriz[:goriz_start]
    goriz_right = goriz[goriz_start + 1:]
    vertic_up = vertic[vertic_start + 1:]
    vertic_down = vertic[:vertic_start]
    goriz_left.reverse()
    vertic_down.reverse()

    fields_vertical_list = [v + field[1] for v in vertic if v != field[0]]
    fields_gorizontal_list = [field[0] + g for g in goriz if g != field[1]]

    diagonal_left_down = list(v + g for (v, g) in zip(vertic_down, goriz_left))
    diagonal_rigt_down = list(v + g for (v, g) in zip(vertic_down, goriz_right))
    diagonal_rigt_up = list(v + g for (v, g) in zip(vertic_up, goriz_right))
    diagonal_left_up = list(v + g for (v, g) in zip(vertic_up, goriz_left))

    total_fields_list = (diagonal_rigt_down + diagonal_left_down + diagonal_rigt_up + diagonal_left_up +
                         fields_vertical_list + fields_gorizontal_list + [field])

    fields_rest_set = fields_set.difference(set(total_fields_list))

    return fields_rest_set

def point_func(fields_set_path, points_list=[], level=0, points_tuple_set=set()):
    """
    This recursive function finds variants of lacations points on the board with given count of fields
    """

    global points_tuple_list, calls

    calls += 1
    # Recursion
    points_level_list = points_list
    files = glob.glob(fields_set_path + '*')
    for f in files:
        print(f)
        with open(f, 'rb') as file_my:
            fields_set = set(pickle.load(file_my))
            print(fields_set)
            for count, field in enumerate(fields_set):
                points_list = points_level_list + [field]
                fields_rest_set = fields_rest_func(field, fields_set)
                len_set = len(fields_rest_set)
                if len_set <= 1:
                    if len_set == 1:
                        points_list.append(fields_rest_set.pop())
                    points_list.sort()
                    points_tuple_set.add(tuple(points_list))
                    return
                    # points_list_list.append(points_list)
                    # points_list.append(list(fields_set)[0])
                else:
                    # Recorsion
                    point_func(fields_rest_set, points_list, level=level + 1)
                pass
    return

    '''
        

           

            

                # points_tuple_list = sorted(
                #     list(set(tuple(sorted(points_list)) for points_list in points_list_list)))

                # print( points_tuple_list)
                # return points_list_list
    '''
calls = 0
def main_func(board_size = 8, elements_max=None):

    start= time()
    path = './board/'
    bord_create_func(path, board_size)
    time_func_board = time() - start
    point_func(fields_set_path=path, level=0)
    time_func_point = time() - time_func_board
    time_exec = time_func_board + time_func_point
    time_creating_element = time_func_board / board_size / board_size
    return {'time_func_board': '{:.3g}'.format(time_func_board),
            'time_creating_element': '{:.3g}'.format(time_creating_element),
            'time_func_point': '{:.3g}'.format(time_func_point),
            'time_exec': '{:.3g}'.format(time_exec)}

    print(len_board)
#TODO: inserting data to files

if __name__ == '__main__':
    import timeit
    from tools_my import convert_to_exponent_float
    board_size = 4
    elements_max = None
    # time_total = timeit.timeit('board_func({}, {})'.format(board_size, elements_max), setup='from __main__ import board_func', number=1)
    # time_creating_element = time_total / (board_size * board_size)
    d = main_func(board_size, elements_max)
    width = 30
    format_my = '{0:{1}}: {2}'
    print(format_my.format('time_func_board', width, convert_to_exponent_float(d['time_func_board'], digit=0)),
          format_my.format('time_creating_element', width, convert_to_exponent_float(d['time_creating_element'])),
          sep='\n')
    # for k in range(size_max - 1, -1, -1):
    #     with open('./board/board{}.pkl'.format(k), 'rb') as file_my:
    #         print(pickle.load(file_my))