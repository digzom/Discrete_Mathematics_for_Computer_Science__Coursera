chess_len = int(input("Chess length: "))

if chess_len >= 4 and chess_len % 6 != 2:
    for i in range(0, chess_len):
        if ((2 * i + 1) > chess_len):
            break
        else:
            print([i, 2 * i + 1])
            
    for j in range(0, chess_len):
            if 2 * j >= chess_len:
                break
            else:
                print([chess_len/2 + j, 2 * j])

else:
    print("It is impossible.")
