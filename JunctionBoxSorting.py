from typing import List


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
    # i: List
    # duplicate: bool = False
    # for i in old_boxes:
    #     duplicate: bool = []

    old_boxes = [(box[0] + ' ' + box[1]) for box in old_boxes]
    new_boxes = [(box[0] + ' ' + box[1]) for box in new_boxes]

    result: List = old_boxes + new_boxes
    return result


junction_boxes = ['a1 9 2 3 1', 'g1 Act car', 'zo4 4 7', 'ab1 off KEY dog', 'a8 act zoo', 'f2 ab ac ad', 'f1 ab ac ad']
print(junction_box_sort(junction_boxes))
