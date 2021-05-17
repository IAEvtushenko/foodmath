from django.shortcuts import render
from .models import *
from django.views import generic


def food_main(request):
    return render(request, 'main/index.html')
# Create your views here.

def food_menu(request):
    data = Product.objects.all()
    products = []
    class Good():
        def __init__(self, title, kcal, protein, carb, fat,
                     fibre, vitC, vitA, vitD, vitE,
                     vitB2, vitB5, vitB6, vitB9, vitB12,
                     fe, k, ca, mg, zn, cost):
            self.title = title
            self.kcal = kcal
            self.protein = protein
            self.carb = carb
            self.fat = fat
            self.fibre = fibre
            self.vitC = vitC
            self.vitA = vitA
            self.vitD = vitD
            self.vitE = vitE
            self.vitB2 = vitB2
            self.vitB5 = vitB5
            self.vitB6 = vitB6
            self.vitB9 = vitB9
            self.vitB12 = vitB12
            self.fe = fe
            self.k = k
            self.ca = ca
            self.mg = mg
            self.zn = zn
            self.cost = cost
        def setPriority(self, curKcal, curProtein, curCarb, curFat,
                     curFibre, curVitC, curVitA, curVitD, curVitE, curVitB2,
                     curVitB5, curVitB6, curVitB9, curVitB12, curFe,
                     curK, curCa, curMg, curZn):
            self.priority = (self.kcal/curKcal + self.protein/curProtein + self.carb/curCarb +
                             self.fat/curFat + self.fibre/curFibre + self.vitC/curVitC +
                             self.vitA/curVitA + self.vitD/curVitD + self.vitE/curVitE +
                             self.vitB2/curVitB2 + self.vitB5/curVitB5 + self.vitB6/curVitB6 +
                             self.vitB9/curVitB9 + self.vitB12/curVitB12 + self.fe/curFe +
                             self.k/curK + self.ca/curCa + self.mg/curMg + self.zn/curZn) / self.cost
    reqKcal = curKcal = 35 * float(request.GET['weight'])
    reqProtein = curProtein = (curKcal * 0.25) / 4.1
    reqCarb = curCarb = (curKcal * 0.55) / 4.1
    reqFat = curFat = (curKcal * 0.20) / 9.1
    reqFibre = curFibre = 35
    reqVitC = curVitC = 90
    reqVitA = curVitA = 900
    reqVitD = curVitD = 10
    reqVitE = curVitE = 15
    reqVitB2 = curVitB2 = 1.8
    reqVitB5 = curVitB5 = 5
    reqVitB6 = curVitB6 = 2
    reqVitB9 = curVitB9 = 400
    reqVitB12 = curVitB12 = 3
    reqFe = curFe = 10
    reqK = curK = 2500
    reqCa = curCa = 1000
    reqMg = curMg = 400
    reqZn = curZn = 12
    totalCost = 0
    for product in data:
        good = Good(product.title, product.kcal, product.protein, product.carb, product.fat, product.fibre,
                    product.vitaminC, product.vitaminA, product.vitaminD, product.vitaminE, product.vitaminB2, product.vitaminB5,
                    product.vitaminB6, product.vitaminB9, product.vitaminB12, product.Fe, product.K,
                    product.Ca, product.Mg, product.Zn, product.cost)
        good.setPriority(curKcal, curProtein, curCarb, curFat, curFibre,
                         curVitC, curVitA, curVitD, curVitE, curVitB2,
                         curVitB5, curVitB6, curVitB9, curVitB12, curFe,
                         curK, curCa, curMg, curZn)
        products.append(good)
        products.append(good)
        products.append(good)
    products.sort(key=lambda x: x.priority)
    lstOfProducts = []
    full = False
    while not full:
        best = products.pop()
        products.sort(key=lambda x: x.priority)
        curKcal -= best.kcal
        curProtein -= best.protein
        curCarb -= best.carb
        curFat -= best.fat
        curFibre -= best.fibre
        curVitC -= best.vitC
        curVitA -= best.vitA
        curVitD -= best.vitD
        curVitE -= best.vitE
        curVitB2 -= best.vitB2
        curVitB5 -= best.vitB5
        curVitB6 -= best.vitB6
        curVitB9 -= best.vitB9
        curVitB12 -= best.vitB12
        curFe -= best.fe
        curK -= best.k
        curCa -= best.ca
        curMg -= best.mg
        curZn -= best.zn
        totalCost += best.cost
        lstOfProducts.append(best)
        for product in products:
            product.setPriority(curKcal, curProtein, curCarb, curFat, curFibre,
                         curVitC, curVitA, curVitD, curVitE, curVitB2,
                         curVitB5, curVitB6, curVitB9, curVitB12, curFe,
                         curK, curCa, curMg, curZn)
        if curKcal < reqKcal * 0.1 and curProtein < reqProtein * 0.1 and curCarb < reqCarb * 0.1\
                and curFat < reqFat * 0.1 and curFibre < reqFibre * 0.1:
            full = True
    total = ['Калории ' + str(reqKcal - curKcal), 'Белки ' + str(reqProtein - curProtein),
             'Жиры ' + str(reqFat - curFat), 'Углеводы ' + str(reqCarb - curCarb), 'Цена ' + str(totalCost)]
    data = {
        'products': lstOfProducts,
        'total': total
    }
    return render(request, 'main/food_menu.html', data)
