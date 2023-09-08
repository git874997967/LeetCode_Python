def minMovesToSeat(seats, students):
    result = 0
    seat_sort,sutdents_sort = sorted(seats) ,sorted(students)
    for idx in range(len(seat_sort)):
        result += abs(seat_sort[idx] - sutdents_sort[idx])
        
    return result
seats = [2,2,6,6]
students = [1,3,2,6]

seats = [4,1,5,9]
students = [1,3,2,6]
seats = [3,1,5] 
students = [2,7,4]
print(minMovesToSeat(seats, students))