from decimal import Decimal
from django.shortcuts import (
    render, redirect, reverse
)
from quote.forms import QuoteForm
from quote.models import Quote


def index(request):
    """ A view to return the index / home page """
    SCOT_SURCHARGE = (
        'AB', 'PA', 'PH', 'FK', 'KA', 'HS', 'IV', 'KW', 'ZE',
        'DD', 'DG', 'EH', 'KY', 'ML', 'TD', 'G1', 'G2', 'G3',
        'G4', 'G5', 'G7', 'G8', 'G9',
    )
    LOCAL = (
        'ME15', 'ME17', 'TN1', 'TN2', 'TN3', 'TN4', 'TN5', 'TN9',
    )
    quote = Quote()
    total_price = Decimal(0)
    v_weight = 0
    a_weight = 0

    if request.method == 'GET':
        quote_form = QuoteForm()
    if request.method == 'POST':
        if 'service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
            }
        elif 'spec_service' not in request.POST:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'service': request.POST['service'],
            }
        else:
            form_data = {
                'd_postcode': request.POST['d_postcode'].upper(),
                'c_postcode': request.POST['c_postcode'].upper(),
                'height': request.POST['height'],
                'length': request.POST['length'],
                'width': request.POST['width'],
                'weight': request.POST['weight'],
                'service': request.POST['service'],
                'spec_service': request.POST['spec_service'],
            }
        
        quote_form = QuoteForm(form_data)
        if quote_form.is_valid():
            v_weight = float(form_data['height']) * float(form_data[
                'width']) * float(form_data['length']) / 6000
            a_weight = float(form_data['weight'])
            height = Decimal(request.POST['height'])
            length = Decimal(request.POST['length'])
            width = Decimal(request.POST['width'])
            total_price = Decimal(8)
            for local in LOCAL:
                if form_data['c_postcode'].startswith((local, )):
                    total_price = Decimal(0)

            for scotland in SCOT_SURCHARGE:
                if form_data['d_postcode'].startswith((scotland, )):
                    total_price += Decimal(9.00)

            if v_weight > a_weight:
                if v_weight <= 1:
                    total_price += Decimal(4.50)
                elif v_weight > 1 and v_weight <= 7:
                    total_price += Decimal(6.50)
                elif v_weight > 7 and v_weight <= 15:
                    total_price += Decimal(8.50)
                elif v_weight > 15:
                    total_price += Decimal(8.50)
                    over_10 = v_weight - 10
                    over_10_cost = Decimal(over_10) * Decimal(0.4)
                    total_price += Decimal(over_10_cost)

            if a_weight > v_weight:
                if a_weight <= 1:
                    total_price += Decimal(4.50)
                elif a_weight > 1 and a_weight <= 7:
                    total_price += Decimal(6.50)
                elif a_weight > 7 and a_weight <= 15:
                    total_price += Decimal(8.50)
                elif a_weight > 15:
                    total_price += Decimal(8.50)
                    over_10 = a_weight - 10
                    over_10_cost = Decimal(over_10) * Decimal(0.4)
                    total_price += Decimal(over_10_cost)

            if 'service' in request.POST:
                if request.POST['service'] == '12am':
                    total_price += Decimal(9.00)
                elif request.POST['service'] == '10am':
                    total_price += Decimal(13.50)
                elif request.POST['service'] == "null":
                    total_price += Decimal(0)

            if 'spec_service' in request.POST:
                if request.POST['spec_service'] == 'Fragile' or request.POST[
                        'spec_service'] == 'Liquid':
                    total_price += Decimal(0.75)
                elif request.POST['spec_service'] == 'Security':
                    total_price += Decimal(1.50)
                elif request.POST['spec_service'] == 'Live Fish':
                    total_price += Decimal(16.50)

            if (
                    height > Decimal(60) and
                    length > Decimal(60) and
                    width > Decimal(60)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(120) and
                    length >= Decimal(55) and
                    width >= Decimal(50)):
                total_price += Decimal(4.00)
            if (
                    height >= Decimal(120) and
                    length >= Decimal(50) and
                    width >= Decimal(55)):
                total_price += Decimal(4.00)
            if (
                    height >= Decimal(55) and
                    length >= Decimal(120) and
                    width >= Decimal(50)):
                total_price += Decimal(4.00)
            if (
                    height >= Decimal(55) and
                    length >= Decimal(50) and
                    width >= Decimal(120)):
                total_price += Decimal(4.00)
            if (
                    height >= Decimal(50) and
                    length >= Decimal(120) and
                    width >= Decimal(55)):
                total_price += Decimal(4.00)
            if (
                    height >= Decimal(50) and
                    length >= Decimal(55) and
                    width >= Decimal(120)):
                total_price += Decimal(4.00)

            if (
                    height >= Decimal(160) and
                    length + width >= Decimal(120)):
                total_price += Decimal(8.00)
            if (
                    length >= Decimal(160) and
                    height + width >= Decimal(120)):
                total_price += Decimal(8.00)
            if (
                    width >= Decimal(160) and
                    height + length >= Decimal(120)):
                total_price += Decimal(8.00)

            quote = quote_form.save()
            quote.quote = total_price
            quote.volume_weight = v_weight
            quote.save()

            return redirect(reverse('partial_quote', args=[quote.quote_ref]))

    context = {'quote_form': quote_form, }

    return render(request, 'home/index.html', context)


def covid(request):
    """ A view to return the covid page """
    return render(request, 'home/covid.html')
