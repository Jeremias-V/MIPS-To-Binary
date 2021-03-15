fill: 
    lw      $t0, 0($s2)     
    addi    $t0, $s4, 0
    add     $t0, $t1, $t2     
    sw      $t0, 0($s2)     
    addi    $s2, $s2, 4     
    addi    $s3, $s3, 1     
    bne     $s1, $s3, 1  
    addi    $s2, $s0, 0     
    addi    $s3, $0, 0      
    j       0xb            
loop: 
    lw      $t0, 0($s2)     
    sll     $t0, $t0, 3     
    sw      $t0, 0($s2)     
    addi    $s2, $s2, 4     
    addi    $s3, $s3, 1     
    bne     $s1, $s3, 2  
    jr      $ra             
main: 
    lui     $s0, 0x1000     
    ori     $s0, $s0, 0x0000     
    addi    $s1, $0, 1000   
    addi    $s2, $s0, 0     
    addi    $s3, $0, 0      
    addi    $s4, $0, 1      
    j       0xa            
