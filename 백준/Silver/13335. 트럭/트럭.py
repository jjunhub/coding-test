from collections import deque

n, w, L = map(int, input().split())
cars = list(map(int,input().split()))
cars.reverse()

car_weight_sum = 0
first_car_weight = cars.pop()

on_bridge = deque()
on_bridge.append((first_car_weight, 1))
car_weight_sum += first_car_weight
tick = 1

while cars or on_bridge:
  tick += 1
  if on_bridge and (tick - on_bridge[0][1]) == w:
    out_car_weight, out_car_time = on_bridge.popleft()
    car_weight_sum -= out_car_weight

  if cars and car_weight_sum + cars[-1] <= L:
    in_car_weight = cars.pop()
    on_bridge.append((in_car_weight, tick))
    car_weight_sum += in_car_weight

print(tick)