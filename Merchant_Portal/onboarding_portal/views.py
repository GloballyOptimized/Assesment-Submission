from django.shortcuts import render

#.............................................................


def vendor_onboarding(request):
    if request.method == 'POST':
        owner = request.POST.get('owner')
        firm_name = request.POST.get('firm_name')
        mobile_number  = request.POST.get('mobile_number')
        pan = request.POST.get('pan')
        upi = request.POST.get('upi')
        aadhar_number = request.POST.get('aashar_number')
        address_block_1 = request.POST.get('address_block_2')
        address_block_2 = request.POST.get('address_block_2')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        

        


    return render(request,'merchant_onboarding.html')
