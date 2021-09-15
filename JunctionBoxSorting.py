from typing import List


def duplicate(lst: List) -> List:
    duplicate_list: List = []
    seen: set = set()
    item: str
    lst = [item[-1] for item in lst]

    for item in lst:
        if item in seen and item not in duplicate_list:
            duplicate_list.append(item)
        seen.add(item)
    return duplicate_list


def junction_box_sort(boxes: List) -> List:
    # split the boxes list in to new and old box
    old_boxes: List = []
    new_boxes: List = []

    box: str
    for box in boxes:
        # split the box to identify and version
        temp: List = box.split(' ', 1)
        if temp[1][0].isdigit():
            new_boxes.append(temp)
        elif temp[1][0].isalpha():
            old_boxes.append(temp)

    # print(f"new_boxes: {new_boxes}\nold_boxes: {old_boxes}")
    # sort the boxes by version first
    old_boxes.sort(key=lambda x: x[1])

    # sort by id if the version is the same
    # find is there any duplicates
    duplicate_version = duplicate(old_boxes)

    # find the index pos of the duplicates
    for i in range(0, len(duplicate_version)):
        index_pos_list: List = []
        for j in range(0, len(old_boxes)):
            if old_boxes[j][-1] == duplicate_version[i]:
                index_pos_list.append(j)

        # sort the boxes with specific range. add the front and back
        start_index: int = index_pos_list[0]
        end_index: int = index_pos_list[-1]
        old_boxes = old_boxes[:start_index] + sorted(old_boxes[start_index:end_index + 1], key=lambda x: x[0]) \
                    + old_boxes[end_index + 1:]

    # combine the id and version. add old_boxes and new_boxes tgt
    old_boxes = [(box[0] + ' ' + box[1]) for box in old_boxes]
    new_boxes = [(box[0] + ' ' + box[1]) for box in new_boxes]
    result: List = old_boxes + new_boxes

    return result


# ---------------------- Main ----------------------
junction_boxes = ['a1 9 2 3 1', 'g1 Act car', 'zo4 4 7', 'ab1 off KEY dog', 'a8 act zoo', 'f2 ab ac ad', 'f1 ab ac ad',
                  'f3 ab ac ad', 'h8 gg hh kk', 'h6 gg hh kk']
print(junction_box_sort(junction_boxes))
