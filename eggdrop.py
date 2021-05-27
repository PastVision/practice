# Google Interview Ques
# Author: PastVision

class Egg:
    def __init__(self, threshold: int) -> None:
        self.threshold = threshold
        self.drop_count = 0

    def drop_test(self, floor: int) -> str:
        self.drop_count += 1
        if floor >= self.threshold:
            return 'dead'
        return 'alive'


class Building:
    def __init__(self, floors: int, egg: Egg) -> None:
        self.floors = floors
        self.egg = egg

    def find_thresold(self):
        lb = 1
        ub = self.floors
        while lb < ub:
            mid = (lb + ub)//2
            egg_status = self.egg.drop_test(mid)
            if egg_status == 'alive':
                lb = mid + 1
            elif egg_status == 'dead':
                ub = mid
        return lb, self.egg.drop_count


if __name__ == '__main__':
    floor_count = int(input('Num floors: '))
    break_threshold = int(input('Egg break threshold: '))
    if break_threshold > floor_count:
        print('Error! BreakThreshold > FloorCount')
        exit(1)
    building = Building(floor_count, Egg(break_threshold))
    threshold, drops = building.find_thresold()
    print(f'Break Threshold of {threshold} found in {drops} drops.')
