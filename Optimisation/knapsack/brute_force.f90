program knapsack

    implicit none

    ! define our varibale
    integer, parameter :: num_items = 22, max_weight = 800
    integer :: i, j, k, m, new_weight, new_value, best_value
    integer :: weight(num_items), value(num_items), new_combination(num_items), best_combination(num_items)

    ! initialize our item weights and values
    weight = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220]
    value = [10, 2, 3, 4, 20, 68, 75, 58, 9, 29, 56, 43, 38, 91, 27, 33, 200, 18, 300, 18, 400, 200]

    best_value = 0

    do i = 0, 2**num_items-1  ! iterate through all possible subsets of items

        new_weight = 0
        new_value = 0

        ! convert subset number to binary representation
        k = i
        do j = num_items, 1, -1
            new_combination(j) = mod(k, 2) ! remainder is always 0 or 1, so we can make binary representation
            k = k/2 ! divide by two to shift the bits in 'k' to the right
        end do

        ! calculate total weight and value of items in subset
        do j = 1, num_items
            new_weight = new_weight + weight(j) * new_combination(j)
            new_value = new_value + value(j) * new_combination(j)
        end do

        ! check if subset is valid and update best value if necessary
        if (new_weight <= max_weight .and. new_value > best_value) then
            best_value = new_value
            best_combination = new_combination
        end if

    end do

    ! print the items and their weight and value in the best solution
    write(*,*) "Items in best combination:"
    do j = 1, num_items
        if (best_combination(j) == 1) then
            write(*,*) "Item:", j, "Weight:", weight(j), "Value:", value(j)
        end if
    end do
    write(*,*) "Best value: ", best_value

end program knapsack