def minmax_odd_even(human_choice, is_maximizing, depth):
    if depth==0:
        return -1 if human_choice % 2==0 else 1
    if is_maximizing:
        best_score= -float("inf")
        for comp_choice in range(1,6):
            total=human_choice+comp_choice
            if total %2==0:
                score=minmax_odd_even(comp_choice,False,depth-1)
            else:
                score=minmax_odd_even(comp_choice,True,depth-1)

            best_score=max(best_score,score)
        return best_score
    else:
        best_score=float("inf")
        for comp_choice in range(1,6):
            total=human_choice + comp_choice
            if total % 2==0:
                score=minmax_odd_even(comp_choice,True,depth -1)
            else:
                score=minmax_odd_even(comp_choice,False,depth-1)
            best_score=min(best_score,score)

        return best_score

def best_move_odd_even(human_choice):
    best_score=-float("inf")
    best_move=-1
    for comp_choice in range(1,6):
        score=minmax_odd_even(human_choice+comp_choice,False,3)
        if score>best_score:
            best_score=score
            best_move=comp_choice

    return best_move
print("Odd or Even uyini boshlanmoqda!")
human_choice=int(input("1 dan 5gacha son kiriting:"))
computer_choice=best_move_odd_even(human_choice)
print(f"kampyuter tanladi:{computer_choice}")
total=human_choice+computer_choice
if total % 2==0:
    print(f"yigindi:{total} (juft).Kompyuter yolib!:")
else:
    print(f"yigindi:{total} (toq). siz golibsz!")
