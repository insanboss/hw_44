from django.shortcuts import render

secret_nums = [5, 1, 2, 9]

def validation(secret_nums, nums):
    bulls = 0
    cows = 0
    if len(nums) != 4:
        return f'PLs enter only 4 numbers'

    if len(nums) != len(set(nums)):
        return f'pls enter unique numbers'

    for number in nums:
        if number < 1 or number > 10:
            return f'pls enter numbers in range from 1 to 10'

    for i in range(len(nums)):
        if nums[i] == secret_nums[i]:
            bulls += 1
        elif nums[i] in secret_nums:
            cows += 1
    if bulls == 4:
        return f'You have won!'
    else:
        return f'You have {bulls} bulls and {cows} cows'


def bulls_n_cows(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        try:
            numbers = list(map(int, request.POST.get('numbers').split(' ')))
            message = validation(secret_nums, numbers)
        except ValueError:
            message = f'You entered not numbers, pls enter numbers'

        context = {"result": message}
        return render(request, 'index.html', context)

