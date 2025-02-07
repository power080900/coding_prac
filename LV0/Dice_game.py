# 6면체 주사위 4개를 던져서 나온 숫자가 a,b,c,d일 때 얻은 점수를 return하는 함수를 작성하시오.
# 제한사항
# 1. a,b,c,d는 1~6사이의 자연수
# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111*p점을 얻는다.
# 네 주사위에서 나온 숫자 중 세개만 p로 같다면 (10 * p + q)**2점을 얻는다.
# 네 주사위에서 나온 숫자 중 두개씩 같다면 (p + q) * |p - q|점을 얻는다.
# 네 주사위에서 나온 숫자 중 두개만 p로 같다면 q * r점을 얻는다.
# 네 주사위에서 나온 숫자가 모두 다르다면 가장 작은 숫자의 점수를 얻는다.

def solution(a,b,c,d):
    nums = [a,b,c,d]
    if len(set(nums)) == 1:
        return 1111 * a
    elif len(set(nums)) == 4:
        return min(nums)
    
    for num in nums:
        if nums.count(num) == 3:
            p = num
            q = [x for x in nums if x != p][0]
            return (10 * p + q) ** 2
    
    for num in nums:
        if nums.count(num) == 2 and len(set(nums)) == 2:
            nums.remove(num)
            nums.remove(num)
            return (num+nums[0]) * abs(num-nums[0])
        elif nums.count(num) == 2:
            nums.remove(num)
            nums.remove(num)
            return nums[0] * nums[1]
    
    return min(nums)

        
    
print(solution(1,2,3,4)) # 1
print(solution(1,1,1,1)) # 1111
print(solution(4,1,4,4)) # 1681
print(solution(6,3,3,6)) # 27
print(solution(2,5,2,6)) # 30
print(solution(1,2,2,3)) # 3