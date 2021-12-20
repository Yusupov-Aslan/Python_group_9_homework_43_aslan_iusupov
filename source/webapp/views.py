from django.shortcuts import render


# Create your views here.


def index_view(request):
    return render(request, "index.html")


secrets = ['2', '3', '4', '5']
history = []


def result_view(request):
    if request.method == "POST":
        nums = request.POST.get('nums').split()
        res = guess_numbers(secrets, nums)
        print(nums)
        return render(request, "result.html", {"result": res})
    else:
        return render(request, "result.html")


def history_view(request):
    if request.method == "GET":
        return render(request, "history.html")


def guess_numbers(secret, numbers):
    bulls = 0
    cows = 0
    res = 'Wrong numbers...'
    if len(numbers) != len(secret) or len(numbers) != len(secret):
        return res
    for i in range(len(secret)):
        if numbers[i] == secret[i]:
            bulls += 1
        elif numbers[i] in secret:
            cows += 1
    if bulls == len(secret):
        res = 'You got it right!!!'
    else:
        res = f'You got {bulls} bulls and {cows} cows.'
    return res
