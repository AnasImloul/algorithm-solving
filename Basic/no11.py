# 덧셈을 모르는 체셔
# 체셔는 학교에서 덧셈을 배웠습니다. 체셔는 학교에서 배운 덧셈을 집에 와서 동생들에게 알려주려고 합니다.
# 체셔는 자연수 A와 B의 합 A + B를 쓰려고 합니다. 그런데 체셔는 기억력이 나빠서 덧셈 기호(+)를 어떻게 쓰는지 잊어버렸습니다.
# 일단 덧셈 기호 없이 자연수 A와 B만 적은 체셔는 당신에게 대신 문제를 풀어달라고 하였습니다. 공백없이 쓰인 A와 B가 주어졌을 때, A + B의 값을 구하는 프로그램을 작성하세요.

# [입력]
# 자연수 A, B를 첫 번째 줄에 입력합니다. 단, 두 수의 사이에는 공백이 들어가지 않습니다.
# (0 < A, B ≤ 10)
# (0<A,B≤10)
# 두 수의 앞에 불필요한 0이 붙는 경우는 없습니다.

# [출력]
# A + B의 값을 출력합니다.


# ------------------------------------------------------


def sol(nums):
    if len(nums) >= 4:
        return int(nums[:2]) + int(nums[2:])
    elif len(nums) >= 3:
        if nums[1] == '0':
            return int(nums[:2]) + int(nums[2])
        else:
            return int(nums[0]) + int(nums[1:])
    else:
        return int(nums[0]) + int(nums[1])


nums = input()
print(sol(nums))
