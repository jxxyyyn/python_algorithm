# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 내가 작성한 코드
def closest_pair(coordinates):
    shortest = distance(test_coordinates[0], test_coordinates[1])
    for a in range((0), len(coordinates)):
        for b in range((a + 1), len(coordinates)):
            if distance(coordinates[a], coordinates[b]) < shortest:
                shortest_coordinates = [coordinates[a], coordinates[b]]
                shortest = distance(coordinates[a], coordinates[b])

    return shortest_coordinates

# 모범답안
def closest_pair(coordinates):
    pair = [coordinates[0], coordinates[1]]
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair


# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

# 테스트 코드
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))