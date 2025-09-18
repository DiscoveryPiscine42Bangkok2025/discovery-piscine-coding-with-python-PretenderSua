def checkmate(board_str):
   
    rows = board_str.strip().split('\n')
    if not rows or not rows[0]:
        print("Fail")
        return

    size = len(rows)
    for r in rows:
        if len(r) != size:
            print("Not A Square")
            return


    king_pos = None
    for r_idx, row in enumerate(rows):
        if 'K' in row:
            c_idx = row.find('K')
            king_pos = (r_idx, c_idx)
            break
    
    if not king_pos:
        print("No King")        
        return
    
#Under this is AI 100% la kub
    k_r, k_c = king_pos

    # ตรวจสอบภัยคุกคามจากตัวหมากที่เดินแบบสไลด์ (เรือ, บิชอป, ควีน)
    # ทิศทาง: แนวนอน, แนวตั้ง, และแนวทแยง
    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  # บน, ล่าง, ซ้าย, ขวา
        (-1, -1), (-1, 1), (1, -1), (1, 1) # แนวทแยง
    ]

    for dr, dc in directions:
        r, c = k_r + dr, k_c + dc
        # เดินทางไปตามทิศทางปัจจุบันจนกว่าจะเจอตัวหมากหรือขอบกระดาน
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece != '.':
                # เจอตัวหมากแล้ว. ตรวจสอบว่าเป็นภัยคุกคามจากทิศทางนี้หรือไม่
                is_straight = (dr == 0 or dc == 0)
                is_diagonal = not is_straight

                if is_straight and piece in 'RQ':
                    print("Success")
                    return
                if is_diagonal and piece in 'BQ':
                    print("Success")
                    return
                
                # ถ้าเป็นตัวหมากอื่น (เช่น เบี้ย) มันจะขวางทาง
                break
            
            r += dr
            c += dc

    # ตรวจสอบภัยคุกคามจากเบี้ย (Pawn)
    # เบี้ยที่ตำแหน่ง (r, c) จะโจมตีในแนวทแยงขึ้นไปที่ (r-1, c-1) และ (r-1, c+1)
    # ดังนั้น เราจะตรวจสอบว่ามีเบี้ยอยู่ด้านล่างคิงของเราหรือไม่
    
    # ตรวจสอบเบี้ยที่อยู่ทางซ้ายล่าง
    pawn_r, pawn_c = k_r + 1, k_c - 1
    if 0 <= pawn_r < size and 0 <= pawn_c < size and rows[pawn_r][pawn_c] == 'P':
        print("Success")
        return

    # ตรวจสอบเบี้ยที่อยู่ทางขวาล่าง
    pawn_r, pawn_c = k_r + 1, k_c + 1
    if 0 <= pawn_r < size and 0 <= pawn_c < size and rows[pawn_r][pawn_c] == 'P':
        print("Success")
        return

    # หากไม่พบภัยคุกคามใดๆ หลังจากการตรวจสอบทั้งหมด
    print("Fail")