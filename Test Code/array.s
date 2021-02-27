# int array[1000];
# int i;
# int size;
# size = 1000;
# for( i = 0; i < size; i++)
#   array[i] = array[i] * 8;

.data 0x10000000

.text

fill:
    # fill = 0x00400024
    # Initializing the array with default value $s4
    # $s1 has size, $s2 has first pointer, $s3 is the iterator (i), $s4 is the default value to fill
    
    lw      $t0, 0($s2)     # load stored int, $t0 = arr[i]                             0x00400024
    addi    $t0, $s4, -1     # establish default value arr[i] = $s4                      0x00400028
    sw      $t0, 4($s2)     # save result arr[i] = $t0                                  0x0040002C
    addi    $s2, $s2, 4     # increment iterator for next position                      0x00400030
    addi    $s3, $s3, 1     # increment i for size comparison                           0x00400034
    bne     $s1, $s3, -5    # while i != size, fill                                     0x00400038
    addi    $s2, $s0, 0     # save first position of array                              0x0040003C
    addi    $s3, $0, 0      # set $s3 in 0 for iteration (i)                            0x00400040
    j       0x10      # go to loop = 0x00100012 * 4       67108863                        0x00400044

loop:
    # loop = 0x00400048
    # Multiplying values of the array
    # $s1 has size, $s2 has first pointer, $s3 is the iterator (i)

    lw      $t0, 0($s2)     # load stored int, $t0 = arr[i]                             0x00400048
    sll     $t0, $t0, 3     # shift left 3 times arr[i] equivalent to multiply by 8     0x0040004C
    sw      $t0, 0($s2)     # save result arr[i] = $t0                                  0x00400050
    addi    $s2, $s2, 4     # increment iterator for next position                      0x00400054
    addi    $s3, $s3, 1     # increment i for size comparison                           0x00400058
    bne     $s1, $s3, -5  # while i != size, loop = (0x400048-0x40005C)/4 = -5        0x0040005C
    jr      $ra             # return to main after finishing the iteration              0x00400060

main:

    lui     $s0, $s0, 0x1000     # loads upper part of first memory position in $s0          0x00400064
    ori     $s0, $s0, 0x0000     # loads lower part of first memory position  in $s0         0x00400068
    addi    $s1, $0, 1000   # define size $s1 = 1000 positions                          0x0040006C
    addi    $s2, $s0, 0     # save first position of array                              0x00400070
    addi    $s3, $0, 0      # initialize $s3 in 0 for iteration (i)                     0x00400074
    addi    $s4, $0, -1000      # Default number to fill array                              0x00400078
    j       0x00100009            # go to fill = 0x00100009 * 4                               0x0040007C

.end
