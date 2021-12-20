from django.shortcuts import render

secrets = ['2', '3', '4', '5']

history = []
current_id = 0


def index_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    elif request.method == "POST":
        res = ''
        data = request.POST.get('nums')
        if data:
            nums = data.split()
            bulls, cows = guess_numbers(secrets, nums)
            if bulls == len(secrets):
                res = 'You got it right!!!'
            else:
                res = f'You got {bulls} bulls and {cows} cows.'
            global current_id
            current_id += 1
            history.append({'id': current_id, 'text': data, 'bulls': bulls, 'cows': cows})
        return render(request, "index.html", {"result": res})


def history_view(request):
    if request.method == "GET":
        return render(request, "history.html", {'history': history})


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
    return bulls, cows
