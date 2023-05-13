program knapsack

    implicit none
    
    integer, parameter :: n = 17
    integer, parameter :: max_weight = 800
    integer :: i, j, k, m
    integer :: weight(n), value(n), subset(n), best_solution(n)
    integer :: total_weight, total_value, best_value

    ! initialize item weights and values
    weight = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170]
    value = [10, 2, 3, 4, 20, 68, 75, 58, 9, 29, 56, 43, 38, 91, 27, 33, 200]

    best_value = 0

    do i = 0, 2**n-1  ! iterate through all possible subsets of items

        total_weight = 0
        total_value = 0

        ! convert subset number to binary representation
        k = i
        do j = n, 1, -1
            subset(j) = mod(k, 2) ! remainder is always 0 or 1, so we can make binary representation
            k = k/2 ! divide by two to shift the bits in 'k' to the right
        end do

        ! calculate total weight and value of items in subset
        do j = 1, n
            total_weight = total_weight + weight(j) * subset(j)
            total_value = total_value + value(j) * subset(j)
        end do

        ! check if subset is a valid solution and update best value if necessary
        if (total_weight <= max_weight .and. total_value > best_value) then
            best_value = total_value
            best_solution = subset
        end if

    end do

    ! print the items and their weight and value in the best solution
    write(*,*) "Items in best solution:"
    do j = 1, n
        if (best_solution(j) == 1) then
            write(*,*) "Item:", j, "Weight:", weight(j), "Value:", value(j)
        end if
    end do

    write(*,*) "Best value found: ", best_value

end program knapsack