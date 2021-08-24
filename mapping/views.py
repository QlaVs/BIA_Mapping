from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import UpdateUser, MassRedact, AddCity, AddUser, AddAC
from .models import *
# from .choices import ch_city, ch_ac, ch_user


local_list_city = []
local_list_ac = []
local_list_nu = []
mass_redact_list = []


def clear_lists():
    local_list_city.clear()
    local_list_ac.clear()
    local_list_nu.clear()


def index(request):
    if request.user.is_authenticated:
        data = Users.objects.all()
        context = {
            "users": data,
        }
        return render(request, "index.html", context)

    else:
        return redirect("login")


def add_new(request):
    if request.user.is_authenticated:
        local_list_city.append(('', '---------'))
        local_list_ac.append(('', '---------'))
        local_list_nu.append(('', '---------'))

        for i in Cities.objects.order_by('city_choice').values():
            local_list_city.append((i['city_choice'], i['city_choice']))

        for i in AC.objects.order_by('ac_choice').values():
            local_list_ac.append((i['ac_choice'], i['ac_choice']))

        for i in NewUser.objects.order_by('nu_choice').values():
            local_list_nu.append((i['nu_choice'], i['nu_choice']))
        if request.method == "POST":
            form = UpdateUser(data=request.POST,
                              city_choices=local_list_city,
                              ac_choices=local_list_ac,
                              nu_choices=local_list_nu)
            clear_lists()
            if form.is_valid():
                data = dict(form.data)
                check_count = Users.objects.filter(city=data['city'][0],
                                                   auto_column=data['auto_column'][0],
                                                   channel=data['channel'][0],
                                                   epic=data['epic'][0],
                                                   user=data['user'][0]).count()
                if check_count > 0:
                    return render(request, 'err.html')
                else:
                    form.save()
                    return redirect('index')

        else:
            form = UpdateUser(city_choices=local_list_city,
                              ac_choices=local_list_ac,
                              nu_choices=local_list_nu)
            clear_lists()
            return render(request, 'new_user.html', {'form': form})

    else:
        return redirect("login")


def edit(request, pk):
    if request.user.is_authenticated:
        for i in Cities.objects.order_by('city_choice').values():
            local_list_city.append((i['city_choice'], i['city_choice']))

        for i in AC.objects.order_by('ac_choice').values():
            local_list_ac.append((i['ac_choice'], i['ac_choice']))

        for i in NewUser.objects.order_by('nu_choice').values():
            local_list_nu.append((i['nu_choice'], i['nu_choice']))

        item = get_object_or_404(Users, pk=pk)
        if request.method == "POST":
            form = UpdateUser(data=request.POST,
                              city_choices=local_list_city,
                              ac_choices=local_list_ac,
                              nu_choices=local_list_nu,
                              instance=item)
            clear_lists()
            if form.is_valid():
                data = dict(form.data)
                check_count = Users.objects.filter(city=data['city'][0],
                                                   auto_column=data['auto_column'][0],
                                                   channel=data['channel'][0],
                                                   epic=data['epic'][0],
                                                   user=data['user'][0]).count()
                if check_count > 0:
                    return render(request, 'err.html')
                else:
                    form.save()
                    return redirect('index')
        else:
            form = UpdateUser(city_choices=local_list_city,
                              ac_choices=local_list_ac,
                              nu_choices=local_list_nu,
                              instance=item)
            clear_lists()
            return render(request, "edit.html", {"form": form})

    else:
        return redirect("login")


def add_new_city(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddCity(request.POST)
            if form.is_valid():
                data = dict(form.data)
                check_count = Cities.objects.filter(city_choice=data['city_choice'][0]).count()
                if check_count > 0:
                    return render(request, 'err.html')
                else:
                    form.save()
                    return redirect('index')

        else:
            form = AddCity()
            context = {"usage": "City",
                       'form': form}
            return render(request, 'new_user.html', context)
    else:
        return redirect("login")


def add_new_ac(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddAC(request.POST)
            if form.is_valid():
                data = dict(form.data)
                check_count = AC.objects.filter(ac_choice=data['ac_choice'][0]).count()
                if check_count > 0:
                    return render(request, 'err.html')
                else:
                    form.save()
                    return redirect('index')

        else:
            form = AddAC()
            context = {"usage": "AC",
                       'form': form}
            return render(request, 'new_user.html', context)
    else:
        return redirect("login")


def add_new_user(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddUser(request.POST)
            if form.is_valid():
                data = dict(form.data)
                check_count = NewUser.objects.filter(nu_choice=data['nu_choice'][0]).count()
                if check_count > 0:
                    return render(request, 'err.html')
                else:
                    form.save()
                    return redirect('index')

        else:
            form = AddUser()
            context = {"usage": "User",
                       'form': form}
            return render(request, 'new_user.html', context)
    else:
        return redirect("login")

# def mass_redact(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = MassRedact(request.POST)
#             if form.is_valid():
#                 item = Users.objects.filter(city=form.data['city'],
#                                             auto_column=form.data['auto_column'],
#                                             channel=form.data['channel'])
#                 if not item:
#                     # TODO: показать сообщение пользователю
#                     print("Nothing Changed")
#                     return redirect('index')
#                 else:
#                     item.update(user=form.data['user'])
#                     return redirect('index')
#
#         else:
#             form = MassRedact()
#             return render(request, "mass_redact.html", {"form": form})
#
#     else:
#         return redirect("login")


def mass_redact(request):
    if request.user.is_authenticated:
        mass_redact_list.append(('', '---------'))
        for i in NewUser.objects.order_by('nu_choice').values():
            mass_redact_list.append((i['nu_choice'], i['nu_choice']))
        if request.method == "POST":
            form = MassRedact(data=request.POST, redact_choices=mass_redact_list)
            if form.is_valid():
                usernames = dict(form.data)
                item = Users.objects.filter(user=usernames['user'][0])
                if not item:
                    # TODO: показать сообщение пользователю
                    return render(request, 'err.html')
                else:
                    item.update(user=usernames['user'][1])
                mass_redact_list.clear()
                return redirect('index')

        else:
            form = MassRedact(redact_choices=mass_redact_list)
            mass_redact_list.clear()
            return render(request, "mass_redact.html", {"form": form})

    else:
        return redirect("login")


def delete(request, pk):
    if request.user.is_authenticated:
        Users.objects.filter(id=pk).delete()

        # item = Users.objects.all()

        # return render(request, 'index.html', {"items": item})
        return redirect('index')

    else:
        return redirect("login")


# def delete_city(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = AddCity(request.POST)
#             if form.is_valid():
#                 data = dict(form.data)
#                 item = Cities.objects.filter(city_choice=data['city_choice'][0]).delete()
#                 return redirect('index')
#
#         else:
#             form = AddUser()
#             return render(request, 'delete.html', {'form': form})
#
#     else:
#         return redirect("login")
#
#
# def delete_ac(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = AddAC(request.POST)
#             if form.is_valid():
#                 data = dict(form.data)
#                 item = Cities.objects.filter(ac_choice=data['ac_choice'][0]).delete()
#                 return redirect('index')
#
#         else:
#             form = AddUser()
#             return render(request, 'delete.html', {'form': form})
#
#     else:
#         return redirect("login")
#
#
# def delete_user(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = AddUser(request.POST)
#             if form.is_valid():
#                 data = dict(form.data)
#                 item = Cities.objects.filter(nu_choice=data['nu_choice'][0]).delete()
#                 return redirect('index')
#
#         else:
#             form = AddUser()
#             return render(request, 'delete.html', {'form': form})
#
#     else:
#         return redirect("login")


@csrf_exempt
def get_json(request, pk=None):
    if pk is not None:
        data = Users.objects.filter(pk=pk).values()
        return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        data = Users.objects.filter().values()
        return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def get_specific_user(request):
    city = request.GET.get('city')
    auto_column = request.GET.get('ac')
    local_channel = request.GET.get('ch')
    local_epic = request.GET.get('epic')
    user = Users.objects.filter(city=city,
                                auto_column=auto_column,
                                channel=local_channel,
                                epic=local_epic).values('user')
    if not list(user):
        return JsonResponse({"error": "There is no user for this params",
                             "params": {"city": city,
                                        "ac": auto_column,
                                        "ch": local_channel,
                                        "epic": local_epic,
                                        }
                             }, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(list(user), safe=False, json_dumps_params={'ensure_ascii': False})


# @csrf_exempt
# def parse(request, city, auto_column, channel, epic, user):
#     if '%2F' in auto_column:
#         auto_column = auto_column.replace('%2F', '/')
#     if '%2F' in epic:
#         epic = epic.replace('%2F', '/')
#     user = Users.objects.create(city=city, auto_column=auto_column,
#                                 channel=channel, epic=epic,
#                                 user=user)
#     return user, redirect('index')

# def parse(request):
#     # for i in ch_user:
#         # item = Cities.objects.create(city_choice=i[0])
#     #     print(i[0])
#     for row in NewUser.objects.all().reverse():
#         if NewUser.objects.filter(nu_choice=row.nu_choice).count() > 1:
#             row.delete()
#             print('deleted')
#     print("all_done")
#     return redirect('index')
