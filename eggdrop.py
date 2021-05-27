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
        self.step_size = self.__calc_step_size()
        # print(self.step_size)
        self.egg = egg

    def __calc_step_size(self):
        a = 0
        n = self.floors
        while n > 0:
            n -= a
            a += 1
        return a-1

    def find_threshold(self):
        low = 1
        step = 0
        for i in range(self.step_size):
            step += self.step_size - i
            if self.egg.drop_test(step) == 'dead':
                for floor in range(low, step):
                    if self.egg.drop_test(floor) == 'dead':
                        return floor, self.egg.drop_count
                return step, self.egg.drop_count
            low += step
        return 'extinct', 'extinct'

    def __find_threshold(self):  # BINSEARCH
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
    threshold, drops = building.find_threshold()
    print(f'Break Threshold of {threshold} found in {drops} drops.')
