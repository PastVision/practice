from math import ceil


class BusService:
    def __init__(self) -> None:
        self.RATE = 5/1000
        self.busStops = ['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA']
        self.path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

    def getFare(self, src: str, dst: str):
        src_idx = self.busStops.index(src.upper())
        dst_idx = self.busStops.index(dst.upper())
        if src_idx < dst_idx:
            dist = sum(self.path[src_idx:dst_idx])
            return ceil(dist*self.RATE)
        if src_idx > dst_idx:
            dist = sum(self.path[src_idx:]) + sum(self.path[:dst_idx])
            return ceil(dist*self.RATE)
        return 0


if __name__ == '__main__':
    service = BusService()
    print(f"Fare: Rs.{service.getFare('NI', 'TH')}/-")
